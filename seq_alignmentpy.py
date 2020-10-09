#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:18 2020

@author: sanjeev
"""
import numpy as np


s1 = 'MAPFVADV'
s2 = 'AAPFVDLV'
gap = -3
#match = 1
#mismatch = 0

    


""" Building PAM250 matrix"""

#rows = [0, 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']

#columns = [0, 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']

pam250 = [[0, 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*'],
          ['A', 2,	-2,	0,	0,	-2,	0,	0,	1,	-1,	-1,	-2,	-1,	-1,	-3,	1,	1,	1,	-6,	-3,	0,	0,	0,	0,	-8], 
          ['R', -2,	6,	0,	-1,	-4,	1,	-1,	-3,	2,	-2,	-3,	3,	0,	-4,	0,	0,	-1,	2,	-4,	-2,	-1,	0,	-1,	-8], 
          ['N', 0,	0,	2,	2,	-4,	1,	1,	0,	2,	-2,	-3,	1,	-2,	-3,	0,	1,	0,	-4,	-2,	-2,	2,	1,	0,	-8], 
          ['D', 0,	-1,	2,	4,	-5,	2,	3,	1,	1,	-2,	-4,	0,	-3,	-6,	-1,	0,	0,	-7,	-4,	-2,	3,	3,	-1,	-8], 
          ['C', -2, -4,	-4,	-5,	12,	-5,	-5,	-3,	-3,	-2,	-6,	-5,	-5,	-4,	-3,	0,	-2,	-8,	0,	-2,	-4,	-5,	-3,	-8], 
          ['Q', 0,	1,	1,	2,	-5,	4,	2,	-1,	3,	-2,	-2,	1,	-1,	-5,	0,	-1,	-1,	-5,	-4,	-2,	1,	3,	-1,	-8], 
          ['E', 0,	-1,	1,	3,	-5,	2,	4,	0,	1,	-2,	-3,	0,	-2,	-5,	-1,	0,	0,	-7,	-4,	-2,	3,	3,	-1,	-8], 
          ['G', 1,	-3,	0,	1,	-3,	-1,	0,	5,	-2,	-3,	-4,	-2,	-3,	-5,	0,	1,	0,	-7,	-5,	-1,	0,	0,	-1,	-8], 
          ['H', -1,	2,	2,	1,	-3,	3,	1,	-2,	6,	-2,	-2,	0,	-2,	-2,	0,	-1,	-1,	-3,	0,	-2,	1,	2,	-1,	-8], 
          ['I', -1,	-2,	-2,	-2,	-2,	-2,	-2,	-3,	-2,	5,	2,	-2,	2,	1,	-2,	-1,	0,	-5,	-1,	4,	-2,	-2,	-1,	-8], 
          ['L', -2,	-3,	-3,	-4,	-6,	-2,	-3,	-4,	-2,	2,	6,	-3,	4,	2,	-3,	-3,	-2,	-2,	-1,	2,	-3,	-3,	-1,	-8], 
          ['K', -1,	3,	1,	0,	-5,	1,	0,	-2,	0,	-2,	-3,	5,	0,	-5,	-1,	0,	0,	-3,	-4,	-2,	1,	0,	-1,	-8], 
          ['M', -1,	0,	-2,	-3,	-5,	-1,	-2,	-3,	-2,	2,	4,	0,	6,	0,	-2,	-2,	-1,	-4,	-2,	2,	-2,	-2,	-1,	-8], 
          ['F', -3,	-4,	-3,	-6,	-4,	-5,	-5,	-5,	-2,	1,	2,	-5,	0,	9,	-5,	-3,	-3,	0,	7,	-1,	-4,	-5,	-2,	-8], 
          ['P', 1,	0,	0,	-1,	-3,	0,	-1,	0,	0,	-2,	-3,	-1,	-2,	-5,	6,	1,	0,	-6,	-5,	-1,	-1,	0,	-1,	-8], 
          ['S', 1,	0,	1,	0,	0,	-1,	0,	1,	-1,	-1,	-3,	0,	-2,	-3,	1,	2,	1,	-2,	-3,	-1,	0,	0,	0,	-8], 
          ['T', 1,	-1,	0,	0,	-2,	-1,	0,	0,	-1,	0,	-2,	0,	-1,	-3,	0,	1,	3,	-5,	-3,	0,	0,	-1,	0,	-8], 
          ['W', -6,	2,	-4,	-7,	-8,	-5,	-7,	-7,	-3,	-5,	-2,	-3,	-4,	0,	-6,	-2,	-5,	17,	0,	-6,	-5,	-6,	-4,	-8],
          ['Y', -3,	-4,	-2,	-4,	0,	-4,	-4,	-5,	0,	-1,	-1,	-4,	-2,	7,	-5,	-3,	-3,	0,	10,	-2,	-3,	-4,	-2,	-8], 
          ['V', 0,	-2,	-2,	-2,	-2,	-2,	-2,	-1,	-2,	4,	2,	-2,	2,	-1,	-1,	-1,	0,	-6,	-2,	4,	-2,	-2,	-1,	-8],
          ['B', 0,	-1,	2,	3,	-4,	1,	3,	0,	1,	-2,	-3,	1,	-2,	-4,	-1,	0,	0,	-5,	-3,	-2,	3,	2,	-1,	-8], 
          ['Z', 0,	0,	1,	3,	-5,	3,	3,	0,	2,	-2,	-3,	0,	-2,	-5,	0,	0,	-1,	-6,	-4,	-2,	2,	3,	-1,	-8], 
          ['X', 0,	-1,	0,	-1,	-3,	-1,	-1,	-1,	-1, -1,	-1,	-1,	-1,	-2,	-1,	0,	0,	-4,	-2,	-1,	-1,	-1,	-1,	-8], 
          ['*', -8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	-8,	1]]


def seq_alignment(s1, s2, pam250, gap):

    """ Creatint empty score matrix"""
    matrix = [[[]for i in range(len(s1)+1)] for i in range(len(s2)+1)]
    
    for i in range(len(s1)+1):
        matrix[i][0].append((0, i))
        matrix[i][0].append((i)*gap)
    
    for j in range(len(s2)+1):
        matrix[0][j].append((j, 0))
        matrix[0][j].append((j)*gap)
    
    
    
    rows = pam250[:][0]
    columns = pam250[0]
    
    pam250 = np.array(pam250)
    
    
    
    """ Filling the score matrix """    
    for i in range(len(s1)):
        for j in range(len(s2)):
        
            A1 = s1[i]
            A2 = s2[j] 
            # if A1 == A2:
            #     S = match
            # else:
            #     S = mismatch
           
            S = pam250[rows.index(A1)][rows.index(A2)]
            #print(i,j, matrix[i][j][1], A1, A2, S, matrix[i][j][1]+int(S))
            score_list =  [matrix[i][j][1]+int(S), matrix[i][j+1][1]+gap, matrix[i+1][j][1]+gap]
            prev_index_list = [(i,j), (i,j+1), (i+1, j)]
            prev_index = score_list.index(max(score_list))
            prev_index = prev_index_list[prev_index]
            score = max(score_list)
            matrix[i+1][j+1].append(prev_index)
            matrix[i+1][j+1].append(score)
    
    
    matrix = np.array(matrix)
    
    
    """ Tracking back alignment path and best alignmet score"""
    indexes_s1 = []
    indexes_s2 = []
    index = (len(s1), len(s2))
    best_score = matrix[index][1]
    n = len(s1)
    
    
    while n >=0:       
        indexes_s1 = [index[0]] + indexes_s1
        indexes_s2 = [index[1]] + indexes_s2
        index = matrix[index[0]][index[1]][0]    
        n -=1
    
    
    """ Finding alignment sequence """
    seq1 = ''
    seq2 = ''
    m = len(indexes_s1)-1
    while m>=0:
        if m == len(indexes_s1)-1:
            prev_ind1 = indexes_s1[m]
            prev_ind2 = indexes_s2[m]
            m -=1
        else:
            curr_ind1 = indexes_s1[m]
            curr_ind2 = indexes_s2[m]
    
            if curr_ind1 == prev_ind1:
                seq1 = '_'+seq1
            else:
                seq1 = s1[prev_ind1-1] + seq1
                
            if curr_ind2 == prev_ind2:
                seq2 = '_'+seq2
            else:
                seq2 = s2[prev_ind2-1] + seq2
            
            prev_ind1 = curr_ind1
            prev_ind2 = curr_ind2
    
            m -=1
    
    if curr_ind1 >=1:
        seq1 = s1[:curr_ind1]+seq1
        
    if curr_ind2 >=1:
        seq2 = s2[:curr_ind2]+seq2
    
    print(f'seq1: {seq1}')
    print(f'seq2: {seq2}')
    print(f'best score: {best_score}')
    
    return seq1, seq2, best_score
    
    
seq1, seq2, best_score = seq_alignment(s1, s2, pam250, gap)











