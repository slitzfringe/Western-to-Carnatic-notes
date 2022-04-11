# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:32:53 2021

@author: Revanth C
"""
# Western to Carnatic Notes converter

def Western_carnatic_compare(note):
     my_dict = {'e':'sa','f':'ri1','f#':'ri2','g':'ga1','g#':'ga2','a':'ma1','a#':'ma2','b':'pa','c':'da1','c#':'da2','d':'ni1','d#':'ni2'}
     
     
     note = note.casefold()
     note_c = note.split()
     
     
     
     strlen = len(note_c)
     
     for _ in range(0,strlen):
         print(my_dict[note_c[_]], end= " ")
'''     note_=""
     note = note.casefold()            #making the recived text lower case!
     
     note_copy = note
     
     note_list = ['e','f','f#','g','g#','a','a#','b','c','c#','d','d#']
     
     space_at = note.find(' ')
     
     for _ in range(0,space_at):
         note_ = note_ + note[_]
     
'''    
     
while(1):
    i = input()
    Western_carnatic_compare(i)
    i = input()
    if (i=='1'):
        break
    
         
        
         