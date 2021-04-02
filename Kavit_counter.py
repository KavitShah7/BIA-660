# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:21:11 2021

@author: shahk
"""

#defining a new function
def counter(path,word1,word2):
    freq={}
# Setting up the frequency counter  
    freq[word1]=0
    freq[word2]=0
# Open file along with the path     
    fin=open('C:\Kavit\Stevens Institute of Technology\SEM 4\Web Mining\week 2\week 2\california.txt')
    for line in fin:
#making the word atomic for the line to read and spliting and stripping them         
        words=line.lower().strip().split(' ')
        
#counter created for words to be counted
        for word in words:
            if word==word1:
                freq[word1]=freq[word1]+1
            elif word==word2:
                freq[word2]=freq[word2]+1
# Closing the file 
    fin.close()
    
#returning the wrods 
    return freq[word1],freq[word2]

#Calling out the functions
print(counter('california','california','yellow'))
print(counter('california','is','america'))
                
                
                
    