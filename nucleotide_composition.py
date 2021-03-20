# set the name of input DNA sequence file
seq = 'nad4L.txt'
# open the input file
infile = open(seq,'r')
dna_sequence = infile.read().rstrip()
seqlen = len(dna_sequence)
freqA = dna_sequence.count('A')/seqlen
freqG = dna_sequence.count('G')/seqlen
freqT = dna_sequence.count('T')/seqlen
freqC = dna_sequence.count('C')/seqlen
GCcon = freqG + freqC
check = freqA + freqG + freqC + freqT
print("This is to check that the sum of all AGCT is", str(check))
infile.close()
outfile = open('STDOUT','w')
outfile.write('Sequence length:'+ str(seqlen) + 'nt' + "\n" 
'Freq of A:' + str(freqA) + "\n"
'Freq of C:' + str(freqC) + "\n"
'Freq of G:' + str(freqG) + "\n"
'Freq of T:' + str(freqT) + "\n"
"G+C content:" + str(GCcon)
)
outfile.close()
