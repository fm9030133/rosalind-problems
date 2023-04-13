#!/usr/bin/env python3
"""
https://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""

a_str = 'GAGCCTACTAACGGGAT'
b_str = 'CATCGTAATGACGGCCT'
hamm_count = 0


for i in range(len(a_str)):
    if a_str[i] != b_str[i]:
        hamm_count += 1

print(hamm_count)