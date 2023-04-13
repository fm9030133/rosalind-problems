#!/usr/bin/env python3
"""
https://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output: MAMAPRTEINSTRING
"""

# Could be streamlined: split table entries by whitespace. Join into str. One move.

rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
table = dict()

sent_list = []
split_list = []

with open('rna_codon_table.txt', 'r') as f:
    # Each is composed of 4 key:value pairs seperated by whitespace. Newline stripped.
    table_str = [line.rstrip('\n') for line in f] 
    for sent in table_str:
        sent_list.append(sent)

# Split each line
for sent in sent_list:
    split_list.append(sent.split())

uni_list = []

# Unify entries into one list
for entry in split_list:
    uni_list += entry

for i in range(0, len(uni_list), 2):
    table[uni_list[i]] = uni_list[i+1]

codon_seq = []

for i in range(0, len(rna), 3):
    codon_seq.append(table[rna[i:i+3]])

stop_i = codon_seq.index('Stop')
stopped_protein = ''.join(codon_seq[:stop_i])

print(stopped_protein)

