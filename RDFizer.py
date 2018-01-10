##########################################################################################
# RDFizer.py
# Purpose: convert SemRep predications into RDF triples
# version 1.0.0
# date: 12.19.2017
# Python 2.7.13
##########################################################################################

##NEEDS:
#1. Dockers for triples and docker that can download SemMedDB instance
#2. autmoatic build
#3. add github topics to repo/create a wikipage for it
#4. write testing
#5. think through combining with PubAnnotation - and or the way that we will map the UMLS concepts to other
# terminologies

# install needed libraries
import argparse
import base64
from functools import partial
import hashlib
import multiprocessing
from mysql.connector import Error, errorcode
import MySQLdb
import os
import sys
from rdflib import Namespace
from rdflib.namespace import RDF, DCTERMS, RDFS
from rdflib import Graph
from rdflib import URIRef, Literal





def DBConnect(host, username, password, db):
    """
    Function takes several strings and an integer that contain information on how to connect to a MySQL database
    containing the SemMedDB database instance. The function returns a string representing the cursor object necessary
    for querying the database as well as a string that stores the database connection (needed to close the connection
    to the database after querying is complete).

    :param host: string representing the database host name
    :param username: string representing the database username
    :param password: string representing the database password
    :param db: string representing the database name

    :return: strings representing the cursor object necessary for querying the database and the database object
    """

    try:
        cnx = MySQLdb.connect(host=host,
                              user=username,
                              passwd=password,
                              db=db)
    # verify that connection to database is valid
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx



def QueryRunner(db_info, query):
    """
    Function takes a list storing information needed to access MySQL database and a string storing an SQL query as
    input. The query is then processed against the database via the cursor. Prior to returning results, the function
    verifies that query returned data, otherwise an exception is raised. The function returns a list of lists where
    each list contains one row of output.

    :param db_info (list): list of information needed to connect to a database
    :param query (str): string storing an SQL query

    :return: list of lists where each list contains one row of output
    """

    # execute query against a MySQL DB
    db_cnx = DBConnect(db_info[0], db_info[1], db_info[2], db_info[3])
    cursor = db_cnx.cursor()
    cursor.execute(query)

    # verify that query returned results
    if int(cursor.rowcount) > 0:
        return cursor.fetchall()
    else:
        raise Exception("Query returned no results")



def SentenceSpan(db_info, sentence_id):
    """Function takes a list storing information needed to access MySQL database and a string storing an identifier. The
    function uses this information to run a query against the database. The query uses the string identifier to retrieve
    all start and end indices for the given identifier. Prior to returning results, the function verifies that the
    returned start and stop indices for the sentence make sense (i.e., that the stop index is equal to or larger
    than the start index, otherwise an exception is raised. The function returns a list of start and stop indexes.

    :param db_info (list): list of information needed to connect to a database
    :param sentence_id (str): sentence identifier

    :return: a list of start and stop indices for the input sentence identifier
    """

    sent_span = QueryRunner(db_info,
                            ("select p.SENTENCE_ID, "
                             " MIN(LEAST(pa.PREDICATE_START_INDEX, pa.SUBJECT_START_INDEX, pa.OBJECT_START_INDEX)),"
                             " MAX(GREATEST(pa.PREDICATE_END_INDEX, pa.SUBJECT_END_INDEX, pa.OBJECT_END_INDEX))"
                             " from SemMedDB.PREDICATION p "
                             " inner join SemMedDB.PREDICATION_AUX pa on pa.PREDICATION_ID = p.PREDICATION_ID"
                             " where p.SENTENCE_ID = " + "'" + str(sentence_id) + "'" +
                             " GROUP BY p.SENTENCE_ID"))

    # verify that query returned results
    if int(sent_span[0][2]) >= int(sent_span[0][1]):
        return str(sent_span[0][1]), str(sent_span[0][2])
    else:
        raise Exception("Sentence start and end indices are incorrect")



def TripleMaker(pmid, db_info):
    """

    :param pmid:
    :param db_info:
    :return:
    """

    ## GET DATA FOR TRIPLES ##
    # run query to get results needed for generating triples
    res = [map(str, x) for x in QueryRunner(db_info,
                                            ("select *"
                                             " from SemMedDB.PREDICATION p" 
                                             " inner join SemMedDB.SENTENCE s on s.SENTENCE_ID = p.SENTENCE_ID" \
                                             " inner join "
                                             "SemMedDB.CITATIONS c on c.PMID = p.PMID" \
                                             " inner join SemMedDB.PREDICATION_AUX pa on pa.PREDICATION_ID = "
                                             "p.PREDICATION_ID" \
                                             " where p.PMID = " + "'" + str(pmid) + "'"
                                             " order by p.PREDICATION_ID"))]

    # get database version information
    vers = [map(str, x) for x in QueryRunner(db_info, ("select * from SemMedDB.METAINFO"))]
    version = base64.b64encode(hashlib.sha1("semrep" + str(vers[0][1])).digest())

    ##CREATE TRIPLES

    # add namespaces
    nlm = Namespace("https://skr3.nlm.nih.gov/")
    oa = Namespace("http://www.w3.org/ns/oa#")
    oa_ext = Namespace("http://www.weneedaurl.now/")
    obo = Namespace("http://purl.obolibrary.org/obo/")
    prov = Namespace("http://www.w3.org/ns/prov#")
    sep = Namespace("http://purl.obolibrary.org/obo/sep/")
    swo = Namespace("http://purl.obolibrary.org/obo/swo/")
    tao = Namespace("http://pubannotation.org/ontology/tao.owl#")
    umls = Namespace("http://uts-ws.nlm.nih.gov/rest/content/current/CUI/")

    # add identifiers
    prj = "http://pubannotation.org/projects/semrep/"
    doc = "http://pubannotation.org/docs/sourcedb/PMC/sourceid/" + str(pmid) + "/divs/0"
    sent = "http://pubannotation.org/projects/sentences/PMC-" + str(pmid) + "-0-sentence_"
    span = "http://pubannotation.org/docs/sourcedb/PMC/sourceid/" + str(pmid) + "/divs/0/spans/"
    concept = "http://pubannotation.org/projects/sentences/PMC-" + str(pmid) + "-0-T_"

    # create graph
    g = Graph()
    annot_graph = base64.b64encode(hashlib.sha1(str(pmid)).digest())

    # document provenance
    g.add((URIRef(str(prj) + str(annot_graph)), URIRef(str(oa) + 'has_source'), URIRef(str(doc))))
    g.add((URIRef(str(doc)), DCTERMS.published, Literal(str(res[0][21]))))
    g.add((URIRef(str(doc)), RDF.type, URIRef(str(obo) + "IAO_0000310")))
    g.add((URIRef(str(doc)), DCTERMS.identifier, Literal(str(pmid))))

    # annotation description triples
    g.add((URIRef(str(prj) + str(annot_graph)), URIRef(str(prov) + 'atTime'), URIRef(str(vers[0][2]))))
    g.add((URIRef(str(prj) + str(annot_graph)), URIRef(str(prov) + 'wasGeneratedBy'), URIRef(str(nlm) + str(version))))
    g.add((URIRef(str(prj) + str(annot_graph)), RDF.type, URIRef(str(prov) + 'Activity')))
    g.add((URIRef(str(prj) + str(annot_graph)), RDF.type, URIRef(str(oa_ext) + 'OA_Concept_Annotation')))
    g.add((URIRef(str(nlm) + str(version)), URIRef(str(sep) + 'SEP_00065'), Literal(str(vers[0][1]))))
    g.add((URIRef(str(nlm) + str(version)), RDF.type, URIRef(str(swo) + 'SWO_0000001')))
    g.add((URIRef(str(nlm) + str(version)), RDFS.label, Literal("SemRep")))


    # loop over predications and add annotations to graph
    for annot in res:

        # get sentence span information
        sent_span = SentenceSpan(db_info, annot[1])

        # resource description
        sents = str(sent) + str(annot[1])
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'belongs_to'), URIRef(str(doc))))
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'begins_at'), Literal(str(sent_span[0]))))
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'ends_at'), Literal(str(sent_span[1]))))
        g.add((URIRef(str(sents)), DCTERMS.source, Literal(str(annot[14]))))
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'has_text'), Literal(str(annot[16]))))
        g.add((URIRef(str(sents)), RDF.type, URIRef(str(tao) + 'Text_span')))

        # subject
        span1 = str(span) + str(annot[27]) + "-" + str(annot[28])
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'contains'), URIRef(str(span1))))
        g.add((URIRef(str(span1)), URIRef(str(tao) + 'begins_at'), Literal(str(annot[27]))))
        g.add((URIRef(str(span1)), URIRef(str(tao) + 'ends_at'), Literal(str(annot[28]))))

        if '|' in annot[4]:
            for con in annot[4].split('|'):
                concept1 = str(concept) + str(con)
                g.add((URIRef(str(span1)), URIRef(str(tao) + 'denotes'), URIRef(str(concept1))))
                g.add((URIRef(str(concept1)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
                g.add((URIRef(str(concept1)), RDF.type, URIRef(str(RDF) + 'Subject')))
                g.add((URIRef(str(RDF) + 'Subject'), DCTERMS.identifier, URIRef(str(umls) + str(annot[4]))))
                g.add((URIRef(str(RDF) + 'Subject'), RDFS.label, Literal(str(annot[5]))))
        else:
            concept1 = str(concept) + str(annot[4])
            g.add((URIRef(str(span1)), URIRef(str(tao) + 'denotes'), URIRef(str(concept1))))
            g.add((URIRef(str(concept1)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
            g.add((URIRef(str(concept1)), RDF.type, URIRef(str(RDF) + 'Subject')))
            g.add((URIRef(str(RDF) + 'Subject'), DCTERMS.identifier, URIRef(str(umls) + str(annot[4]))))
            g.add((URIRef(str(RDF) + 'Subject'), RDFS.label, Literal(str(annot[5]))))

        # predicate
        span2 = str(span) + str(annot[31]) + "-" + str(annot[32])
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'contains'), URIRef(str(span2))))
        g.add((URIRef(str(span2)), URIRef(str(tao) + 'begins_at'), Literal(str(annot[31]))))
        g.add((URIRef(str(span2)), URIRef(str(tao) + 'ends_at'), Literal(str(annot[32]))))

        if '|' in annot[3]:
            for con in annot[3].split('|'):
                concept2 = str(concept) + str(con)
                g.add((URIRef(str(span2)), URIRef(str(tao) + 'denotes'), URIRef(str(concept1))))
                g.add((URIRef(str(concept2)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
                g.add((URIRef(str(concept2)), RDF.type, URIRef(str(RDF) + 'Predicate')))
                g.add((URIRef(str(RDF) + 'Predicate'), DCTERMS.identifier, URIRef(str(umls) + str(annot[3]))))
                g.add((URIRef(str(RDF) + 'Predicate'), RDFS.label, Literal(str(annot[3]))))
        else:
            concept2 = str(concept) + str(annot[3])
            g.add((URIRef(str(span2)), URIRef(str(tao) + 'denotes'), URIRef(str(concept1))))
            g.add((URIRef(str(concept2)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
            g.add((URIRef(str(concept2)), RDF.type, URIRef(str(RDF) + 'Predicate')))
            g.add((URIRef(str(RDF) + 'Predicate'), DCTERMS.identifier, URIRef(str(umls) + str(annot[3]))))
            g.add((URIRef(str(RDF) + 'Predicate'), RDFS.label, Literal(str(annot[3]))))

        # object
        span3 = str(span) + str(annot[36]) + "-" + str(annot[37])
        g.add((URIRef(str(sents)), URIRef(str(tao) + 'contains'), URIRef(str(span3))))
        g.add((URIRef(str(span3)), URIRef(str(tao) + 'begins_at'), Literal(str(annot[36]))))
        g.add((URIRef(str(span3)), URIRef(str(tao) + 'ends_at'), Literal(str(annot[37]))))

        if '|' in annot[8]:
            for con in annot[8].split('|'):
                concept3 = str(concept) + str(con)
                g.add((URIRef(str(span3)), URIRef(str(tao) + 'denotes'), URIRef(str(concept3))))
                g.add((URIRef(str(concept3)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
                g.add((URIRef(str(concept3)), RDF.type, URIRef(str(RDF) + 'Object')))
                g.add((URIRef(str(RDF) + 'Object'), DCTERMS.identifier, URIRef(str(umls) + str(annot[8]))))
                g.add((URIRef(str(RDF) + 'Object'), RDFS.label, Literal(str(annot[9]))))
        else:
            concept3 = str(concept) + str(annot[8])
            g.add((URIRef(str(span3)), URIRef(str(tao) + 'denotes'), URIRef(str(concept3))))
            g.add((URIRef(str(concept3)), RDF.type, URIRef(str(tao) + 'Concept_entity')))
            g.add((URIRef(str(concept3)), RDF.type, URIRef(str(RDF) + 'Object')))
            g.add((URIRef(str(RDF) + 'Object'), DCTERMS.identifier, URIRef(str(umls) + str(annot[8]))))
            g.add((URIRef(str(RDF) + 'Object'), RDFS.label, Literal(str(annot[9]))))

        # graph-level triples
        g.add((URIRef(str(span1)), URIRef(str(tao) + 'follows'), URIRef(str(span2))))
        g.add((URIRef(str(span2)), URIRef(str(tao) + 'follows'), URIRef(str(span3))))

    # serialize annotation graph for pmid
    out = "RDF_output/semrep_" + str(pmid)
    g.serialize(destination=str(out) + ".xml", format='xml')




def main():
    parser = argparse.ArgumentParser(description='SemRepRDF: This program is designed to ')
    parser.add_argument('-h', '--host', help='MySQL host information', required=True)
    parser.add_argument('-u', '--user', help='MySQL username information', required=True)
    parser.add_argument('-p', '--passwd', help='MySQL root information', required=True)
    parser.add_argument('-d', '--db', help='MySQL password information', required=True)
    args = parser.parse_args()

    # set default encoding to utf8
    reload(sys)
    sys.setdefaultencoding('utf8')  # needed to parse article titles

    # connect to database
    # db_info = [args.host, args.user, args.passwd, args.db]
    db_info = ['', 'root', 'YRUS9bjb', 'SemMedDB']

    # retrieve all pubmed ids to facilitate parallel processing
    pmids = [str(id[0]) for id in QueryRunner(db_info, ("select PMID from SemMedDB.CITATIONS"))]

    # configure multiprocessing settings
    pool = multiprocessing.Pool()  # set up pool
    func = partial(TripleMaker, db_info)
    triples = pool.map(func, pmids)

    # close and join pool
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()


