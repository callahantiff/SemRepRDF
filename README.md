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
    * Obtain a free [UMLS license](https://www.nlm.nih.gov/research/umls/)
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
This repository generates two different kinds of output that are subject to two different kind of licensing (see details regarding these representations on the [Wiki](https://github.com/callahantiff/SemRepRDF/wiki/Licensing)):
  1. The SemRep representation uses concepts that are part of the UMLS Metathesaurus and are thus subject to the [UMLS license agreement](https://uts.nlm.nih.gov/license.html).
  2. The open SemRepRDF version has been generated in such a way that all annotated concept identifiers come only from terminologies, vocabularies, and ontologies with open license agreements. <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This representation is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Acknowledgments

* Project completed as part of the 4th annual Biomedical Linked Annotation Hackathon ([BLAH](http://blah4.linkedannotation.org)) held in Kashiwa, Japan.

* README was generated from a modified markdown template originally created by **Billie Thompson [PurpleBooth](https://github.com/PurpleBooth)**.

