#!/usr/bin/python

import string #string manipulation
import collections #string manipulation

def ceasar(rotate_string, number_to_rotate_by):#fucntion
    
    upper = collections.deque(string.ascii_uppercase) #['A','B','C','D', ...]
    lower = collections.deque(string.ascii_lowercase) #['a','b','c','d', ...]
    
    upper.rotate(number_to_rotate_by) #occurs the rotation uppercases
    lower.rotate(number_to_rotate_by) #occurs the rotation lowercases
    
    upper = ''.join(list(upper)) #join letters for the upper
    lower = ''.join(list(lower)) #join letters for the lower
    
    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))


our_string = "This is string" #string to convert

for  i in range(len(string.ascii_uppercase)):
    print(i, "|", ceasar(our_string,i)[::-1]) #Ceasaer cipher with reverse