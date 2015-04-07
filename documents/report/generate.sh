#!/bin/bash

pdflatex x.tex
bibtex x.aux
pdflatex x.tex
pdflatex x.tex