# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:19:34 2020

@author: grojas
"""


file = open('C:/Users/grojas/Desktop/Rosalind/rosalind_revc.txt', 'r')
output = open('C:/Users/grojas/Desktop/Rosalind/Solutions/rosalind_revc.txt', 'w+')

sequence = file.readlines()[0].rstrip()
dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
complement = ''
for i in sequence:
    complement += dic[i]
output.write(complement[len(complement)::-1])

file.close()
output.close()

# Alternative
# sequence[::-1].translate(str.maketrans('ACGT', 'TGCA'))