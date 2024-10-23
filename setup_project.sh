#!/bin/bash

mkdir -p bioinformatics_project

cd bioinformatics_project

mkdir -p data scripts results

touch scripts/generate_fasta.py
touch scripts/dna_operations.py
touch scripts/find_cutsites.py

touch results/cutsite_summary.txt

touch data/random_sequence.fasta

cat <<EOL > README.md
# Bioinformatics Project

This project directory structure is organized as follows:

- **data/**: This has the input data
  - `random_sequence.fasta`: Generated from problem 2

- **scripts/**: This has scripts for all the problems
  - `generate_fasta.py`: Problem 2
  - `dna_operations.py`:Problem 3
  - `find_cutsites.py`: Problem 4
- **results/**: This has the results
  - `cutsite_summary.txt`: Output of problem 4

EOL


