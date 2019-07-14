# Project Title: The Genome Project

## Objective
To store the Ecoli gene sequence fasta files, test their validity and to find
some important parameters.

## What I did
I started with the independent modules in each task. These were built
and tested separately. Finally I combined everything, built the main
software and tested it.

## How it works
The software starts with a GUI, where I have to select the fasta file that
contains the gene info. Next, I choose th fasta file if I want to save the output file
that the software generates or just go ahead with the program. Next, I
save the data which I find into a database.

## Tools Used
The entire program was done using the following software tool(s)/language(s):
- Python 3.5
- PySimpleGUI for the graphical user interface
- MySQL for maintaining the database

## Editors used
- IDLE
- Atom


## Problem Definition:

### Task 1
i) Create an interface to upload a fasta file
ii) Once uploaded, validate the file with the following checks:
a) The information line starts with a ‘>’ symbol only.
b) The information is contained in one single line and is not continued to the next line.
c) There is no blank line between information line and gene sequence.
d) The gene sequence contains only 4 characters ‘A’, ‘T’, ‘G’ and ‘C’.
iii) If validated, display the file contents in a format in ‘Output file’.

### Task 2
i) Connect your GUI to database
ii) Information that should be contained in the database are: Sl_No, Gene Information, Gene sequence, Count_A, Count_T, Count_G, Count_C, length, (G+C)%.
where, (G+C)% is calculated as: (G+C)% = (Count_G + Count_C) / (Count_A + Count_T + Count_G + Count_C)*100

### Task 3
Along with these 9 fields, add all those fields given in Gene Detail List to the database
Checks: If the location field of a gene in a gene sequence file contains:
a) 1798...1800, 1919…2020
If there is a comma separating locations, it means the gene is joined from two segments, you can ignore this gene and do not add it to your database.
b) c1666…17000
Here ‘c’ means, the gene is present in the complementary strand. So any location starting with ‘c’ will be stored as 17000…1666 ( in the  reverse order) in the Gene Detail List. So while checking the location, please check it in the reverse order in the Gene Detail List.

### Task 4
Convert the gene sequence into protein sequence.
Checks: If any stop codon appears within a gene sequence, the generate a
warning message stating “Stop codon found in gene gene_name”. Gene_name you will get from Task 3.

### Task 5
Find the effective number of codons for every gene.
