# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:43:57 2020

@author: grojas
"""


file = open('C:/Users/grojas/Desktop/Rosalind/rosalind_dna.txt', 'r')
output = open('C:/Users/grojas/Desktop/Rosalind/Solutions/rosalind_dna.txt', 'w+')

sequence = file.readlines()[0]
A = sequence.count('A')
C = sequence.count('C')
T = sequence.count('T')
G = sequence.count('G')
output.write(str(A)+' '+str(C)+' '+str(G)+' '+str(T))

file.close()
output.close()