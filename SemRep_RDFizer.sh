#!/bin/bash

if ! [[ -e README.md ]]; then
    echo "Please run from the root of the project."
    exit 1
fi

# run python script to create a visual graph of each Clojure rule
python /Users/tiffanycallahan/Dropbox/Papers-Conferences-Projects/Hackathons/BLAH 2018/SemRep_RDF.py -h "$path" -u
"$path" -p "$path" -d "$path"