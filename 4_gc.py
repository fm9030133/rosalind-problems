#!/usr/bin/env python3
"""
https://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""

with open('gc_database.txt', 'r') as f:
    lines_list = [line.rstrip('\n') for line in f] # List of lines. Ommit newlines.

# Return GC content as percentage
def gc_content(dna):
    size = len(dna) # Total bp
    gc_count = dna.count('G') + dna.count('C') # Total bp that are either G or C
    gc_percent = gc_count / size * 100 # Percentage of entire dna str that is either G or C
    return gc_percent

data_dict = dict()
id = None

# Single dna strs are found split by newlines in text file.
# This for-loop consolidates each dna str into a single str
# Each str is associated to its label (a dict key)
for i in range(len(lines_list)):
    if lines_list[i][0] == '>':
        data_dict[lines_list[i][1:]] = ''
        id = i
    else:
        data_dict[lines_list[id][1:]] += lines_list[i]

gc_dict = dict()

# (key:value) dna label: gc content of respective dna str 
for i in data_dict:
    gc_dict[i] = gc_content(data_dict[i])

# Get key value of maximum gc content
max_key = max(gc_dict, key = gc_dict.get)

print(max_key) 
print(gc_dict[max_key])
