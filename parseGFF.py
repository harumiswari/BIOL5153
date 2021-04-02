#! /usr/bin/env python3

import csv
import argparse
# from Bio import SeqIO

# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description = 'this script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument('gff', help ='name of the GFF file')
parser.add_argument('fasta', help ='name of the FASTA file')

# parse the arguments
args = parser.parse_args()
# print(args.gff)

'''
# read in GFF file
gff_input = 'c:/Users/harum/OneDrive/Documents/scripts/watermelon.gff'

# fasta filename
fasta_input = 'c:/Users/harum/OneDrive/Documents/scripts/watermelon.fsa'
'''

# open and read in FASTA file (with open(gff_input,'r') as gff_in:)
with open(args.gff,'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object of the parse file
    for line in reader:
        print(line)
        start = line[3]
        end = line[4]
        strand = line[6]
        print(start)
'''
genome = seqIO.read(args.fasta,'fasta')
print(genome)
print(genome.id)
print(len(genome.seq))
'''

# unused code but saved as a memory on how to split the line
'''
    for l in gff_in:
        columns = l.split('\t')
        print(columns[3], columns[4])
'''


