# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:18:23 2022

@author: Grant Huang

Assignment 2-2 for Smoothstack
"""
#Question 1.

mixedList = [1, "Hello", 3.14]
print(mixedList)

#%%
#Question 2.

#nestedList = [1, 1[1, 2]] <- syntax error

#%%
#Question 3.

lst = ['a', 'b', 'c']
print("lst = " + str(lst))
print("lst[1:] = " + str(lst[1:]))

#%%
#Question 4.

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekIndexes = [n for n in range(1, 54)]

weeks = {k:weekIndexes for k in weekDays}
print(weeks)

#%%
#Question 5.

D = {"k1" : [1, 2, 3]}
#print(d[k1][1]) <- error message

#%%
#Question 6.

numberList = [1, [2, 3]]
numberTuple = (numberList[0], numberList[1])
print(numberTuple)

#%%
#Question 7.

word = "Mississippi"
letters = set(word)
distinctCharWord = "".join(letters)
print(word)
print(distinctCharWord)

#%%
#Question 8.

word = "Mississippi"
letters = set(word)
print(letters)
letters.add("X")
print(letters)

#%%
#Question 9-0

print(set([1, 1, 2, 3]))

#%%
#Question 9-1

numbers = [str(n) for n in range(2000, 3201) if n%7 == 0 and n%5 != 0]
numberString = ",".join(numbers)
print(numberString)

#%%
#Question 9-2

inputedNumbers = input("Input comma separated numbers:")
numbers = inputedNumbers.split(",")
products = []

#finding factorials of each number
for n in numbers:
    num = int(n)
    product = 1

    #n! = n*(n-1)*(n-2)*...*2*1 for n > 0
    for k in range(1, num + 1):
        product *= k
        
    products.append(str(product))
    
print(",".join(products))

#%%
#Question 9-3
    
number = int(input("Input integer: "))
squares = {i:i**2 for i in range(1, number + 1)}
print(squares)

#%%
#Question 9-4

numbers = input("Input comma separated numbers: ")
numberList = numbers.split(",")
print(numberList)
numberTuple = tuple(numberList)
print(numberTuple)

#%%
#Question 9-5

class Message:
    #constructor
    #@param msg - string containing message. empty string by default
    def __init__(self, msg=""):
        self.msg = msg
        
    #sets string from console input as message
    def getString(self):
        self.msg = input("Input message: ")
    
    #prints out stored message
    def printString(self):
        print(self.msg)
        
#tests out Message class by running all it's methods
def messageTest():
    announcement = Message()
    announcement.getString()
    announcement.printString()
    
messageTest()
        

        