"""
https://rosalind.info/problems/revc/

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, 
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s

Sample Dataset: AAAACCCGGT
Sample Output: ACCGGGTTTT
"""

comp_pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} # Dictionary mapping each base pair to its complement

'''
Replaces each nucleotide in ss with its complement.
'''
def comp(ss): # Pass single strand ss
    comp_str = '' # Container for finished complement
    for nt in ss: # Iterate through each nucleotide nt in single strand ss
        comp_str += comp_pairs[nt] # Pull appropriate complement from dictionary
    return comp_str

sstrand_dna = 'AAAACCCGGT'
revc = comp(sstrand_dna[::-1])
print(revc)