# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:13:00 2022

@author: Grant Huang

Assignment 2-1 for Smoothstack
"""

print("Hello World")
print("Hello World"[-3])

#%%

word = "thinker"
print(word)
print(word[2:5])

S = "hello"
#print(h[1]) <- output is error message

#%%

S = "Sammy"
#print(s[2:]) <- output is error message

#%%

word = "Mississippi"
letters = set(word)
distinctCharWord = "".join(letters)
print(word)
print(distinctCharWord)

#%%

alphabet = set("abcdefghijklmnopqrstuvwxyz")
palindromes = []
numPhrases = int(input("input data:\n"))

#checking if each phrase is a palindrome
for n in range(numPhrases):
        phrase = input()
        phraseLetters = [s.lower() for s in phrase if s.lower() in alphabet]
        reversePhrase = phraseLetters[::-1]
        
        #found a palindrome!
        if phraseLetters == reversePhrase:
            palindromes.append("Y")
        else:
            palindromes.append("N")
      
print("\nanswer: ")
print(" ".join(palindromes))
        
