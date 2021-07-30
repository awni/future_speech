#!/bin/bash

for f in `ls *.tex` 'references.bib' 'main.bbl' `ls figures/*.pdf`
do
    zip -u arxiv.zip $f
done
