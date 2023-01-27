#!/usr/bin/env python3
"""
A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. 
In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, 
plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that 
were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th month, 
then we obtain the Fibonacci sequence having terms Fn that are defined by 
the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). 
Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to 
generate terms for progressively larger values of n. This problem introduces us to the 
computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces 
a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset: 5 3
Sample Output: 19
"""

n = 5
k = 3
seq = {'b':1, 'a':0} # Container for rabbit pair population
pairs_count = [seq['b'] + seq['a']] # Track total pair count

for i in range(n - 1): # Account for off-by-one error
    b_prev = seq['b'] # Store previous baby and adult counts
    a_prev = seq['a']
    seq['b'] = a_prev * k # Each previous adult has k-sized litter
    seq['a'] = b_prev + a_prev # Each previous baby becomes adult. Previous adults persist.
    pairs_count += [seq['b'] + seq['a']] # Track total pair count

print(pairs_count[-1])