#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:50:42 2020

@author: sdodlapa
"""

import numpy as np


s1 = 'MAPFVADV'
s2 = 'AAPFVDLV'

match = 1
mismatch = 0
gap = -3

def simple_seq_alignment(s1, s2, match, mismatch, gap):
    """ Creatint empty score matrix"""
    matrix = [[[]for i in range(len(s1)+1)] for i in range(len(s2)+1)]
    
    for i in range(len(s1)+1):
        matrix[i][0].append((0, i))
        matrix[i][0].append((i)*gap)
    
    for j in range(len(s2)+1):
        matrix[0][j].append((j, 0))
        matrix[0][j].append((j)*gap)
        
    
    
    """ Filling the score matrix """    
    for i in range(len(s1)):
        for j in range(len(s2)):
        
            A1 = s1[i]
            A2 = s2[j] 
            if A1 == A2:
                S = match
            else:
                S = mismatch
           
            #S = pam250[rows.index(A1)][rows.index(A2)]
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
    


seq1, seq2, best_score = simple_seq_alignment(s1, s2, match, mismatch, gap)
    
    
    
    
    
    