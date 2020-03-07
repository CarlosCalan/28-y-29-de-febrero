# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:44:32 2020

@author: CEC
"""

#import math
#x=float(input("Enter x:"))
#y=math.sqrt(x)
#print ("The square root", x, "equals to", y)

#try:
#    print("1")
#    x=1/0
#    print("2")
#except:
#    print("something went wrong")
#    
#print ("3")

try:
    x=int(input("Enter: "))
    y=1/x
    print(y)
    
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter a integer value")
except:
    print("something went wrong")
    
print("END")