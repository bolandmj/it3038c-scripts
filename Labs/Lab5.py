# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:27:24 2022

@author: maxwe
"""

#https://www.programiz.com/python-programming/datetime/current-datetime
#Found date time function here
from datetime import date

today = date.today()

currentYear = int(today.year)
currentMonth = int(today.month)
currentDay = int(today.day)


userYear = input("What year were you born: ")
userYear = int(userYear)

if userYear < 0 or userYear > 9999:
    userYear = input("Please input in four digit format(0000): ")
    
userMonth = input("What month were you born: ")
userMonth = int(userMonth)

if userMonth < 0 or userMonth > 12:
    userMonth = input("Please input in two digit format 1-12 (00): ")
    
userDay = input("What day were you born: ")
userDay = int(userDay)

if userDay < 0 or userDay > 31:
    userDay = input("Please enter a valid day of the month in two digit format (00): ")
    
#Seconds in day 86400

calcYear = currentYear - userYear
calcDay = userDay
calcMonth = userMonth

if currentMonth > userMonth:
    calcMonth = currentMonth - userMonth

calcDay = (calcMonth * 32) + calcDay
calcDay = (calcYear * 365) + calcDay

calcSec = (calcDay * 24 * 60 * 60)

print("You have been alive for ", str(calcSec), " seconds")    
    


    