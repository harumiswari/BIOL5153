#! /usr/bin/env python3

import csv
import re
import argparse
from Bio import SeqIO
from collections import defaultdict

# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

def get_seq(s, e, str):
    # rxtract the sequence
    fragment = gene.seq[int(s):int(e)]
    #check for + or - strand and returns as is for reverse complement
    if(str == '+'):
        return fragment
    else:
        return fragment.reverse_complement()

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

# create dictionoary for genes with intron/multiple exons
# key = gene name, value = list of exon sequences
exons_dict = defaultdict(dict)

# open and read in FASTA file (with open(gff_input,'r') as gff_in:)
with open(args.gff,'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')
    # loop over all the lines in our reader object of the parse file
    for line in reader:
        species         = line[0].replace(' ','_')
        feature_type    = line[2]
        start           = line[3]
        end             = line[4]
        strand          = line [6]

        #split the attribute fields in a list
        attr_fields = line[8].split()
        gene_name = attr_fields[1]

        if(feature_type == 'CDS'):

            # search for exon annotation
            match = re.search("exon\s+(\d)", line[8])
            # test for whether there are multiple exons
            if(match):
                #create fasta header which allso nbe our dictionary key for exons
                header              = species + "_" + gene_name
                #get the exon number
                exon_number         = (match.group(1))
                #get the sequence for this exon
                exon                = get_seq(int)start)-1, int(end), strand)
                
                if(header in exons_dict):
                    exons_dict[header][exon_number] = exon
                
                else:
                    exons_dict[header] = defaultdict(dict)
                    exons_dict[header][exon_number] = exon
            # just print genes that don't have intron
            #else:
                #print the FASTA header
                print(">" + species + "_" + gene_name)
                # extract the sequence
                print(get_seq(int(start)-1, int(end), strand))
        #skip all other feature type
        else :
            continue

# loop over expns dictionary(h=header, j=list of exons)
for i, j in exons_dict.items():
    #print the header
    print(">" + i)
    # loop over the dictionary of exons, and print them
    for k in sorted(j):
        # print the individual exon
        print(j[k], end='')
    print()
            

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



