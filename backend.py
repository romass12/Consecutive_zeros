# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:13:46 2017

@author: Roma
"""

import math
test_cases = raw_input('Enter number of test cases: ')  #tells user to enter number of test cases
for d in range(int(test_cases)):
    length = raw_input('Enter length of string: ')    #tells user to enter string length
    ind=[]    # ind list contains indices of the tuples where consecutive zeros are found
    fin_ind=[]   #fin_ind list contains range of indices considering all possible combinations for example if length=2 , fin_ind=[0,1,2,3]
    output=list(product(range(2), repeat=int(length)))   #this creates all possible combinations of bits 1 and 0 of particular length 
    for i in range(len(output)):    #this is to access a tuple from list
        outpu=output[i]
        for j in range(int(length)-1):    #this is to access elements inside that tuple
            if outpu[j] == 0 and outpu[j + 1] == 0:    #this checks consecutive zeros
                ind.append(i)
                break
    fin_ind=[h for h in range(int(math.pow(2, int(length))))]    
    fin_ind=set(fin_ind)-set(ind)     #this gives remaining indices of tuples having non-consecutive zeros
    print len(fin_ind)
                 
        
        
        
        
        
        
        
        
        
        
        
        
