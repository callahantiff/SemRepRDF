# SemRepRDF
This repository contains code used to transform the National Library of Medicine’s Semantic Representation (SemRep) predications into open semantically-linked annotations.

The schema used to convert the data to triples is shown below.
<img src="https://github.com/callahantiff/SemRepRDF/blob/master/images/SemRep_PA_triples_v5.jpg">


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

Running program from the command line
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

## Collaboration

* [callahantiff](https://github.com/callahantiff)
* [bill-baumgartner](https://github.com/bill-baumgartner)
* Olivier Bodenreider
* [jdkim](https://github.com/jdkim)


## License

This project is licensed under 3-Clause BSD License - see the [LICENSE.md](https://github.com/callahantiff/SemRepRDF/blob/master/LICENSE) for details.

## Acknowledgments

* Project completed as part of the 4th annual Biomedical Linked Annotation Hackathon ([BLAH](http://blah4.linkedannotation.org)) held in Kashiwa, Japan.

* README was generated from a modified markdown template originally created by **Billie Thompson [PurpleBooth](https://github.com/PurpleBooth)**.

