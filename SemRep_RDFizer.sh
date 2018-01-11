#!/bin/bash

if ! [[ -e README.md ]]; then
    echo "Please run from the root of the project."
    exit 1
fi

# run python script
python /Users/tiffanycallahan/Dropbox/Papers-Conferences-Projects/Hackathons/BLAH 2018/SemRep_RDF.py -h "$path" -u
"$path" -p "$path" -d "$path"
