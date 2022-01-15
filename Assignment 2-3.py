# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:15:03 2022

@author: Grant Huang
Assignment 2-3 for Smoothstack
"""

#Three is a Crowd

#tests if a room is crowded
#@param people - list containing names of all people in area
#prints "It's crowded in here!" if number of people are 3 or more
def crowd_test(people):
    if len(people) >= 3:
        print("It's crowded in here!")

people = ["Mario", "Luigi", "Peach", "Toad"]
print(people)
crowd_test(people)
    
del people[2:]
print(people)
crowd_test(people)

#%%
#Three is a Crowd Part-2

#tests if a room is crowded
#@param people - list containing names of all people in area
#prints message based on whether there are 3 or more people
def crowd_test(people):
    if len(people) >= 3:
        print("It's crowded in here!")
    else:
        print("It's not crowded right now.")

people = ["Mario", "Luigi", "Peach", "Toad"]
print(people)
crowd_test(people)
    
del people[2:]
print(people)
crowd_test(people)

#%%
#Six is a Mob

#tests if a room is crowed
#@param people - list containing names of all people in area
#prints a messages for 0, 1-2, 3-5, and >5 people
def crowd_test(people):
    #prints messages based on number of people
    if len(people) > 5:
        print("There's a mob in here!")
    elif len(people) >= 3:
        print("It's crowded in here!")
    elif len(people) >= 1:
        print("It's not crowded right now.")
    else:
        print("It's empty in here.")

people = ["Mario", "Luigi", "Peach", "Toad", "Wario", "Yoshi"]

#checking crowd removing one person at a time
for n in range(len(people) + 1):
    print(people)
    crowd_test(people)
    
    #shortening list if possible
    if len(people) > 0:
        people.pop()

