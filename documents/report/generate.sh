#!/bin/bash

pdflatex final.tex
bibtex final.aux
pdflatex final.tex
pdflatex final.tex