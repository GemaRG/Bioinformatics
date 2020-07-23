# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:05:47 2020

@author: grojas
"""


file = open('C:/Users/grojas/Desktop/Rosalind/rosalind_rna.txt', 'r')
output = open('C:/Users/grojas/Desktop/Rosalind/Solutions/rosalind_rna.txt', 'w+')

sequence = file.readlines()[0]
rna = sequence.replace('T', 'U')
output.write(rna)

file.close()
output.close()