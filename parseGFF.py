#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

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

# open and read in the FASTA file
gene.seq = SeqIO.read(args.fasta, 'fasta')

# function for reverse complements:
def rev_comp(rev_gene):
    return rev_gene.reverse_complement()

whole_exons = ''
files = 'exon' + ''.fasta'
outfile = open(files, 'w')
# open and read in FASTA file (with open(gff_input,'r') as gff_in:)
with open(args.gff,'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object of the parse file
    for line in reader:
        if 'exon' in reader[-1]:
            start = int(line[3])
            end = int(line[4])
            exons = str(gene.seq[start:end])
            whole_exons+=exons
       
        # print header
        print('>' + gene.id, line[-1])
        print(whole_exons)

outfile.close()
'''
        # check in reverse complement
        if strand == '-':
            anti_seq = gene.seq[start-1:end].reverse_complement()
            print(anti_seq)
        # print the sequence of sense strand
        else:
            sense_seq = gene.seq[start[-1:end]]
            print(sense_seq)
        
        print()
'''



