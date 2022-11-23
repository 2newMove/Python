# This challanges are taken from hacker Rank  website.

#################### 1st challenge
print("Hello  World")  

#################### 2nd challenge
# Task
# Given an integer, n , perform the following conditional actions:

# If  n is odd, print Weird
# If  n  is even and in the inclusive range of  2 to 5, print Not Weird
# If  n  is even and in the inclusive range of  6 to 20, print Weird
# If  n  is even and greater than 20 , print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1<= n <= 100
print("Please Enter a positive integer from 0 to 100 ")  
n = int(input())

# for int in n <= 100 and n >= 0  :     <----useless statement
if n % 2 != 0 and n != 0:
         print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
            print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20 :
            print("Weird")
elif n % 2 == 0 and n >= 20 and n <= 100 :
            print("Not Weird")
else:
           print("invalid number")


#################### 3rd challenge


