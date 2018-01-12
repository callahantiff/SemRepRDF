# SemRepRDF
This repository contains code used to transform the National Library of Medicine’s Semantic Representation (SemRep) predications into open semantically-linked annotations. Please see the Wiki for more details.


## Getting Started

To obtain an RDFized version of SemRep, download the zip file or fork the project repository. Additional instructions can be found under [*Installation*](Installation).


### Installation

This program was written on a system running OS X Sierra. Successful execution of this program requires Python version 2.7.

  * Python 2.7.13 modules
    * Native Modules: base64, hashlib, multiprocessing, MySQLdb, os, sys
    * To download needed modules run the following from the working directory of the project folder:

  ```
  pip install -r requirements.txt
  ```

  * Semantic MEDLINE Database
    * If using SemRepRDF-UMLS you will need to obtain a free [UMLS license](https://www.nlm.nih.gov/research/umls/)
    * Download and configure the latest SemMedDB MySQL data dump [SemMedDB](https://skr3.nlm.nih.gov/SemMedDB/dbinfo.html)

  * Although not a requirement, the program has been written to run in parallel on a super computer.


## Running Program

The program can be run from the command line via argparse arguments.

```
# from project directory - find help menu
tiffanycallahan$ python RDFizer.py -h



# to run the program
tiffanycallahan$ python RDFizer.py

```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Testing
We are in the process of developing tests for each module. We will create documentation as they are created.

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.  

This repository generates two different kinds of output that are subject to two different kind of licensing (see details regarding these representations on the [Wiki](https://github.com/callahantiff/SemRepRDF/wiki/Licensing)):
  1. The SemRep representation uses concepts that are part of the UMLS Metathesaurus and are thus subject to the [UMLS license agreement](https://uts.nlm.nih.gov/license.html).
  2. The open SemRepRDF version has been generated in such a way that all annotated concept identifiers come only from terminologies, vocabularies, and ontologies with open license agreements. Minor modifications to the original SemRep predications include the mapping of UMLS CUIs to open resource concept identifiers.  
  
 #### SemRepRDF-Open Resources and Tools
 
 Table of UMLS Metathesaurus vocabularies and NLM tools used when generating SemRepRDF-Open.  
  
<table>
  <tr>
   <td><b>Source</b></td>
   <td><b>Version</b></td>
   <td><b>License</b></td>
   <td><b>Terms of Use</b></td>
  </tr>
  <tr>
   <td colspan="5"><b>RESOUCES</b></td>
  </tr>
 
   <tr>
    <td> Anatomical Therapeutic Chemical (ATC)</td>
    <td> 2017AB</td>
    <td> Non-Commercial</td>
    <td> Use of all or parts of the material requires reference to the WHO Collaborating Centre for Drug Statistics Methodology. Copying and distribution for commercial purposes is not allowed. <a href="https://www.whocc.no/copyright_disclaimer/">Additional Information</a>. Changing or manipulating the material is not allowed.</td>
  </tr>
  
   <tr>
   <td> DrugBank</td>
   <td> 2017AB</td>
   <td> CC BY-NC 4.0</td>
   <td> DrugBank is offered to the public as a freely available resource. Use and re-distribution of the data, in whole or in part, for commercial purposes (including internal use) requires a license. <a href="https://www.drugbank.ca/about"> Additional Information</a></td>
 </tr>
 
 <tr>
  <td> Gene Ontology (GO)</td>
  <td> 2017AB</td>
  <td> CC-BY 4.0</td>
  <td> The GOC wishes the users and consumers of GO data publicly display the date(s) and/or version number(s) of the relevant GO files, data, or software version. The GO is evolving and changes regularly--this information is critical to downstream consumers and users. <a href="http://www.geneontology.org/page/use-and-license"> Additional Information</a></td>
</tr>

<tr>
 <td> HUGO Gene Nomenclature Committee (HGNC)</td>
 <td> 2017AB</td>
 <td> It is a condition of our funding from NIH and the Wellcome Trust that the nomenclature and information we provide is freely available to all.</td>
 <td> Anyone may use the HGNC data, but we request that they reference the "HUGO Gene Nomenclature Committee at the European Bioinformatics Institute" and the website where possible. <a href="https://www.genenames.org/about/overview"> Additional Information</a></td>
</tr>

<tr>
 <td> Human Phenotype Ontology (HPO)</td>
 <td> 2017AB</td>
 <td> The HPO vocabularies, annotation files, tools and documentation are freely available.</td>
 <td> The HPO is copyrighted to protect the integrity of the vocabularies, which means that changes to the HPO vocabularies need to be done by HPO developers. However, anyone can download the HPO and use the ontologies or other HPO files under three conditions:
<ul>
<li>That the Human Phenotype Ontology Consortium is acknowledged and cited properly.</li>
<li>That any HPO Consortium file(s) displayed publicly include the date(s) and/or version number(s) of the relevant HPO file(s).</li>
<li>That neither the content of the HPO file(s) nor the logical relationships embedded within the HPO file(s) be altered in any way. (Content additions and modifications have to be suggested using our issue tracker).</li>
<li>We suggest that you follow standard scientific citation practice if you use the HPO in publications.<br>5)Services and products have to display a short acknowledgement statement, that makes clear that the service/product is using HPO.</li>
</ul>
<a href="http://human-phenotype-ontology.github.io/license.html"> Additional Information</a></td>
</tr>

<tr>
 <td> The International Classification of Diseases, Ninth Revision, Clinical Modification (ICD9-CM)</td>
 <td> 2017AB</td>
 <td> Not specified in readme when downloaded</td>
 <td> Availible for download via ftp through the CDC. <a href="https://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/codes.html"> Additional Information</a></td>
</tr>

<tr>
 <td> The International Classification of Diseases, Tenth Revision (ICD10)</td>
 <td> 2017AB</td>
 <td> WHO is able to issue internal licences to organizations wishing to incorporate WHO
classifications into their internal information systems for use by employees for use for
administrative purposes eg. health records management". </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="http://www.who.int/about/licensing/Internettext_FAQ.pdf"> Additional Information</a></td>
</tr>

<tr>
 <td> The International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD10-PCS)</td>
 <td> 2017AB</td>
 <td> WHO is able to issue internal licences to organizations wishing to incorporate WHO
classifications into their internal information systems for use by employees for use for
administrative purposes eg. health records management.</td>
 <td> For more information regarding guidelines for using resource, see link. <a href="http://www.who.int/about/licensing/Internettext_FAQ.pdf"> Additional Information</a></td>
</tr>

<tr>
 <td> The Logical Observation Identifiers Names and Codes terminology (LOINC)</td>
 <td> 2017AB</td>
 <td> Licensed and Copyrighted, free to use</td>
 <td> The Terms of Use are very detailed, see link. <a href="https://loinc.org/license/"> Additional Information</a></td>
</tr>

<tr>
 <td> NCBI Taxonomy</td>
 <td> 2017AB</td>
 <td> Databases of molecular data on the NCBI Web site include such examples as nucleotide sequences (GenBank), protein sequences, macromolecular structures, molecular variation, gene expression, and mapping data. They are designed to provide and encourage access within the scientific community to sources of current and comprehensive information. Therefore, NCBI itself places no restrictions on the use or distribution of the data contained therein. Nor do we accept data when the submitter has requested restrictions on reuse or redistribution. </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="https://www.ncbi.nlm.nih.gov/home/about/policies/"> Additional Information</a></td>
</tr>

<tr>
 <td> National Drug File - Reference Terminology</td>
 <td> 2017AB</td>
 <td> UMLS Category 0 license; but vocabulary can be downloaded from NCI without license or registration. </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="https://evs.nci.nih.gov/ftp1/NDF-RT/"> Additional Information</a></td>
</tr>

<tr>
 <td> Foundational Model of Anatomy (FMA)</td>
 <td> 2017AB</td>
 <td> Licensed through the University of Washington, which states "The Foundational Model of Anatomy ontology (FMA) is OPEN SOURCE and available for general use". </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="http://sig.biostr.washington.edu/projects/fm/AboutFM.html"> Additional Information</a></td>
</tr>

<tr>
 <td> The Healthcare Common Procedure Coding System (HCPCS)</td>
 <td> 2017AB</td>
 <td> Subject to same licensing as Current Procedural Terminology (CPT) codes. The AMA licenses thousands of organizations to use CPT data in a broad array of applications. The AMA’s licensing model for CPT is based on individual users. In each of these cases, organizations that utilize CPT in one of these systems are required to obtain a license for each system and for each Individual user—regardless of the number of codes they use. </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="https://www.ama-assn.org/practice-management/cpt-licensing-health-care-delivery-organizations"> Additional Information</a></td>
</tr>

<tr>
 <td> Online Mendelian Inheritance in Man (OMIM)</td>
 <td> 2017AB</td>
 <td> License prevents redistribution. </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="https://www.omim.org/help/agreement"> Additional Information</a></td>
</tr>

 <tr>
 <td colspan="5"><b>TOOLS</b></td>
 </tr>

<tr>
 <td> Semantic Knowledge Representation</td>
 <td> 2017AB;<br>v 1.7</td>
 <td> SKR resources are available to all applicants at no charge, both within and outside the United States. </td>
 <td> Redistributions of SKR resources in source or binary form must include the following list of conditions in the documentation and other materials provided with the distribution.
 <ul>
<li>In any publication or distribution of all or any portion of the SKR resources: (1) the user must attribute the source of the tools as SemRep and SemRep Tools with the release number and date; (2) the user must clearly annotate within the source code any modification made to SemRep and SemRep Tools; and (3) any subsequent distribution of the program, tools, or material based on SemRep and SemRep Tools, must be accomplished within the context of an open source set of terms and conditions such as the GNU General License.</li>
<li>Bugs, questions, and/or issues relating to an SKR resource should be directed to the most recent in the chain of entities that may have modified and re-distributed this code.</li>
<li>Users shall not assert any proprietary rights to any portion of an SKR resource, nor represent it or any part thereof to anyone as other than a United States Government product.</li>
<li>The name of the U.S. Department of Health and Human Services, National Institutes of Health, National Library of Medicine, and Lister Hill National Center for Biomedical Communications may not be used to endorse or promote any products derived from an SKR resource without specific prior written permission.</li>
<li>Neither the United States Government, the U.S. Department of Health and Human Services, the National Institutes of Health, the National Library of Medicine, the Lister Hill National Center for Biomedical Communications, nor any of their agencies, contractors, subcontractors, or employees make any warranties, expressed or implied, with respect to the SKR resources, and furthermore, they assume no liability for any party's use, or the results of such use, of any part of these tools.</li>
<li>These Terms and Conditions are in effect as long as the user retains any part of the SKR resources.</li>
</ul>
<a href="https://skr3.nlm.nih.gov/TermsAndCond.html"> Additional Information</a></td>
</tr>

<tr>
 <td> Semantic Network</td>
 <td> 2017AB;<br>v 54</td>
 <td> The following Terms and Conditions apply for use of the UMLS Semantic Network. Using the UMLS Semantic Network indicates your acceptance of the following Terms and Conditions. These Terms and Conditions apply to all the UMLS Semantic Network files, independent of format and method of acquisition. </td>
 <td> For more information regarding guidelines for using resource, see link. <a href="https://semanticnetwork.nlm.nih.gov/TermsAndConditions.html"> Additional Information</a></td>
</tr>


</table>

## Acknowledgments

* Project completed as part of the 4th annual Biomedical Linked Annotation Hackathon ([BLAH](http://blah4.linkedannotation.org)) held in Kashiwa, Japan.

* README was generated from a modified markdown template originally created by **Billie Thompson [PurpleBooth](https://github.com/PurpleBooth)**.

