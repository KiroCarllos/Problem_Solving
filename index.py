# 1- print Hello World
# employee = input('Enter Your Employee');
# print("Hello, "+ employee);
###################################
# 2- DataTypes
# ints,longs,chars,floats,doubles = input().split();
# print(int(ints))
# print(longs)
# print(str(chars))
# print(float(floats))
# print(doubles);
###################################
# 3- Simple Calculator
# x,y = input().split();
# z = int(x) + int(y);
# c = int(x) * int(y);
# b = int(x) - int(y);
# print(str(x)+" + "+str(y) +" = " + str(z))
# print(str(x)+" * "+str(y) +" = " + str(c))
# print(str(x)+" - "+str(y) +" = " + str(b))
###################################
# 4- D. Difference
# A,B,C,D = input().split();
# X = (int(A) * int(B)) - (int(C) * int(D));
# print("Difference"+"  = ",int(X));
###################################
# 5- Area Of Circle
# R = input();
# Area = 3.141592653 * float(R) * float(R);
# print(Area)
###################################
# 6- F. Digits Summation
# A,B = input().split();
# x = int(A)  % 10;
# y = int(B)  % 10;
# z = x + y;
# print(z)
###################################
# 7- G. Summation from 1 to N
# 641009859
# num = int(input())
# sum =0
# while num > 0:
#     sum = sum + num
#     num = num - 1;
# print(sum)
# n = int(input())
# sum = (n*(n+1)/2)
# print(int(sum))
###################################
# 8 - Tow Numbers Floor - Ceil - Round
# import math
# x,y = (input()).split()
# z= float(x) / float(y);
# print ("floor",x,"/",y ,"=",math.floor(z))
# print ("ceil",x,"/",y ,"=",math.ceil(z))
# print ("round",x,"/",y ,"=",(round(z)))
###################################
# 9- Welcome for you with Conditions
# x,y = (input()).split()
# if(int(x) >= int(y)):
#     print("Yes")
# else:
#     print("No")
###################################
# 10- J. Multiples
# x,y = input().split()
# if((int(x) % int(y)) == 0 or (int(y) % int(x)) == 0):
#     print("Multiples")
# else:
#     print("No Multiples")
###################################
# 11- Min Vs Max
# x,y,z = input().split()
# if(int(x) <= int(y) and int(x) <= int(z) and int(y) >= int(z)):
#     print(x,y)
# elif (int(x) <= int(y) and int(x) <= int(z) and int(z) >= int(y)):
#     print(x, z)
# elif (int(y) <= int(x) and int(y) <= int(z) and int(z) >= int(x)):
#     print(y, z)
# elif (int(y) <= int(x) and int(y) <= int(z) and int(x) >= int(z)):
#     print(y,x)
# elif (int(z) <= int(x) and int(z) <= int(y) and int(y) >= int(x)):
#     print(z, y)
# elif (int(z) <= int(x) and int(z) <= int(y) and int(x) >= int(y)):
#     print(z,x)
###################################
# 12- M. Capital or Small or Digit
# x = (input())
# try:
#     val = int(x)
#     print("IS DIGIT")
# except ValueError:
#     try:
#         val = float(x)
#         print("IS DIGIT")
#     except ValueError:
#         if(x.isupper()== True):
#             print("ALPHA")
#             print("IS CAPITAL")
#         else:
#             print("ALPHA")
#             print("IS SMALL")
###################################
# 13- Calculator
# x,s,y = input().split(" ")
# if(str(s) == "+"):
#     print(int(x[0]) + int(y[0]))
# elif(str(s) == "-"):
#     print(int(x) - int(y))
# elif(str(s) == "*"):
#     print(int(x) * int(y))
# elif(str(s) == "/"):
#     print(int(x) / int(y))
###################################
# 14- First digit !
# x = input().split()[0]
# if(int(x[0]) % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")
###################################
# 15- Q. Coordinates of a Point
# x,y = input().split()
# if(float(x) > 0 and float(y) > 0):
#     print("Q1")
# elif (float(x) < 0 and float(y) > 0):
#     print("Q2")
# elif(float(x) > 0 and float(y) < 0):
#     print("Q4")
# elif (float(x) < 0 and float(y) < 0):
#     print("Q3")
# elif(float(x) > 0  and float(y) == 0):
#     print("Eixo X")
# elif(float(y) > 0  and float(x) == 0):
#     print("Eixo Y")
# elif(float(x) < 0  and float(y) == 0):
#     print("Eixo X")
# elif(float(y) < 0  and float(x) == 0):
#     print("Eixo Y")
# elif(float(y) ==0  and float(x) == 0):
#     print("Origem")
###################################
# 16- Q. R. Age in Days
# x = input()
# year = int(x) / 365;
# monthes = ((int(x)) - int(year)*365)/30
# days = int(x) - ((int(year)*365) + int(monthes) * 30)
# print(int(year) ,"years")
# print(int(monthes) ,"months")
# print(int(days) ,"days")
###################################
# 17- S. Interval
# x = input()
# if(float(x) >= 0 and float(x) <= 25):
#     print("Interval [0,25]")
# elif(float(x) >= 25 and float(x) <= 50):
#     print("Interval (25,50]")
# elif(float(x) >= 50 and float(x) <= 75):
#     print("Interval (50,75]")
# elif(float(x) >= 75 and float(x) <= 100):
#     print("Interval (75,100]")
# else:
#     print("Out of Intervals")
###################################
# 18- U. Float or int
# x = input().split(".")
# if(int(x[1]) == 0 ):
#     print("int "+x[0])
# else:
#     print("float " + x[0]+" 0."+x[1])
###################################
# 19- V. Comparison
# A,s,B = input().split()
# if(str(s) == ">" and int(A) > int(B)):
#     print("Right")
# elif(str(s) == "<" and int(A) < int(B)):
#     print("Right")
# elif(str(s) == "=" and int(A) == int(B)):
#     print("Right")
# else:
#     print("Wrong")
###################################
# 20- W. Mathematical Expression
# A,s,B,Q,C = input().split(" ")
# x = 0
# if(str(s) == "+"):
#     x= (int(A) + int(B))
# elif(str(s) == "-"):
#     x= (int(A) - int(B))
# elif(str(s) == "*"):
#     x= (int(A) * int(B))
# elif(str(s) == "/"):
#     x= (int(A) / int(B))
# else:
#     print("Operator Not Suported")
#
# if(int(C) == int(x)):
#     print("Yes")
# else:
#     print(int(x))
###################################
# 21- X. Two intervals
# A,B,C,D = input().split()
# if(int(C) > int(A) and int(D) < int(B)):
#     print((C) + " " + (D))
# elif(int(B) - int(C) > 0):
#     print((C) + " " + (B))
# elif(int(B) - int(C) == 0):
#     print((C) + " " + (B))
# elif(int(C) < int(A) and int(D) <= int(B)):
#     print((C) + " " + (A))
# else:
#     print("-1")
# ##################################### Complete Level A
# Get Start With Level B
# 1- A. 1 to N
# x= input()
# for i in range(1,int(x)+1):
#     print(i)
###################################
# 2- B. Even Numbers
# x= input()
# for i in range(1,int(x)+1):
#     if(i % 2 == 0):
#         print(i)
###################################
# 3- C. Even, Odd, Positive and Negative
# y= input()
# x= input().split(" ",int(y))
# Even = 0
# Odd = 0
# Positive= 0
# Negative= 0
# i =0
# for i in x:
#     if(int(i) % 2 == 0 and int(i) > 0):
#         Even+=1
#         Positive += 1
#     if(int(i) == 0 ):
#         Even+=1
#     if(int(i) % 2 == 0 and int(i) < 0):
#         Even+=1
#         Negative += 1
#     if(int(i) % 2 and int(i) >= 0):
#         Odd+=1
#         Positive += 1
#     if(int(i) % 2 and int(i) <= 0):
#         Odd+=1
#         Negative += 1
# print("Even:",Even)
# print("Odd:",Odd)
# print("Positive:",Positive)
# print("Negative:",Negative)
###################################
# 4- D. Fixed Password
# d= input()
# y= input()
# a= input()
# b= input()
# c= input()
# x = [int(d),int(y),int(a),int(b),int(c)]
# correct_Pass = 1999;
# for i in x:
#     if( int(i) == correct_Pass):
#         print("Correct")
#         break
#     if (int(i) != correct_Pass):
#         print("Wrong")
###################################
# 5- F. Multiplication table
# x= input()
# for i in range(1,13):
#     z = int(x) * int(i)
#     print(int(x),"*",int(i),"=",int(z))
###################################
# 6- E. Max
# y= input()
# x= input().split(" ",int(y))
# for i in range(0, len(x)):
#     x[i] = int(x[i])
# print(max(x))
###################################
# 7- G. Factorial
# y= input()
# x =[]
# factorial =1
# for i in range(0,int(y)):
#     x+=input()
# for a in x:
#     if int(a) >= 1:
#         for j in range(1, int(a) + 1):
#             factorial = factorial * j
#         print(factorial)
#         factorial = 1
#     if(int(a) == 0):
#         print("1")
###################################
# 8- G. Factorial
# x= input()
# if int(x) > 1:
#     # check for factors
#     for i in range(2, int(x)):
#         if (int(x) % i) == 0:
#             print("NO")
#             break
#     else:
#         print("YES")
# else:
#     print("NO")
###################################
# 9- I. Palindrome



