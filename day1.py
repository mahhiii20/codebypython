# sum
# a = 2
# b = 3

# sum = a + b
# print("sum=",sum)
# tup = (1,2,32)
# print(type(tup) , tup)

# Variable store

# name = "Mahi"
# age = "20"

# print(name)
# print(age)

# Data Types
# x  = 20
# y = 20.3
# name = "Mahi"
# Statement = True

# print (name)

# Input lena (User se)

# name = input("Enter the name : ")
# print("HELLO",name)

# Opertors

# a = 10
# b = 20

# print(a + b)
# print(a - b)
# print(a / b)
# print(a * b)

# If-else

# age = int(input("Enter the age : "))
# if age >= 20:
#     print("Adult")
# else:
#     print("bachaa hai tu")

# basic questions;

# a = 10
# b = 3
# print (a//b)    

# print(8<5)   true false batata hai

# print ("7"=="7")  agr same string ya int rahe tho true ho jayega

# check even or odd

# a = int(input("Enter the value: "))

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# take a num biger num

# a = int(input("enter the value: "))
# b = int(input("enter the value: "))

# if a >= b :
#     print("a is bigger")
# else:
#     print ("b is greater")

# find the value 

# a = int(input("enter the value: "))
# b = int(input("enter the value: "))
# c = int(input("enter the value: "))

# if a == 0 :
#     print("zero")

# elif  a > 0:
#         print ("positive")

# else:
#         print("Negative")

# 3 number find largest

# a =int(input("enter the value :"))
# b =int(input("Enter the value :"))
# c =int(input("Enter the value :"))

# if a > b and a > c :
#     print("A is greater")

# elif b > a and b > c :
#     print("B is greater")

# else:
#     print("C is greater")        

# Grade System

# Marks = int (input("Enter the marks :"))

# if Marks >= 90 :
#     print("A")

# elif Marks >= 50 :
#     print ("B")

# else :
#     print("Fail")       

# a = 20
# b = 5
# c = 7
# print(a + b /c)

# a = int(input("Enter the value :"))

# if a % 2==0 and a > 10:
#     print("valid number ")

# elif a % 2==0 and a <= 10:
#     print("Small even number ")

# else :
#     print("odd number")        

# FizzBuzz type question

# a = int(input(" Enter the number"))

# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")

# elif a % 3 == 0 :
#     print("FIzz") 

# elif a % 5 == 0:
#     print("Buzz") 

# else:
#     print("invaild")         

# age question

# a = int(input("Enter the age :"))

# if a == 18 and a <= 60:
#     print("Working age ")

# else:
#     print("Not Working") 

# list

# list= [11,2,5,4,32,6,2,5]
# print(list.index(32))
# print(list)

# Match case

# x = int (input("Enter the value of x :"))

# match x:

#     case 0:
#         print("X is zero")

#     case 2:
#         print("case is 2")
#     case _ if x!=90:
#         print("x is not equal 90")
#     case _ if x!=60:
#         print("x is not equal to 60")
#     case  _ :
#         print(x)            

# loops 

# for i in range(6):
#     print("*")

# for i in range(1):
#     print("******")  ( or )

# for i in range(50):
#     print("*",end ="")

# for i in range(6):
#     print(i)

# for i in range(6):
#     print(i, end = "")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end = " ")
#     print()        

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end = " ")
#     print()   

# Recursion

# n = int(input("Enter the value :"))

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(n))

# print 1 to n num using recursion

def printnum(n):
    if n==0:
        return
    print(n)
    printnum(n - 1)
    # print(n)

n = int(input("enter the num:"))
printnum(n)