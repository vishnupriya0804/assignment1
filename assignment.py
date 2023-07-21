#question1

#1.Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500

"""l=[]
for i in range(2000,2500):

    if (i%5==0) and (i%8==0):
        x=l.append(i)
print(l)"""


#2Write a Python program to create the table (from 1 to 10) of a number getting input from the user

"""n=int(input("enter number:"))
for i in range(0,11):
    ans=n*i
    print(i,"*",n, "=",ans)"""

#5.	Python program to print odd numbers & even numbers separately in al list of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""l=[1,2,3,4,5,6,7,8,9,10]
a=[]
b=[]
for i in l:
    if i%2==0:
        x =a.append(i)

    elif i%2==1:
        x=b.append(i)
print(a)
print(b)

# 7Program to print all odd numbers from 1-50


a=int(input("enter value:"))
b=[]
for i in range(0,a+1):
    if i%2==1:
        x=b.append(i)
print(b)"""


#6.Program for Reversing a list
'''
a=[1,2,3,4,5,6,7]
print(a[::-1])

#3.	sort the list in ascending order and print first element

l=[1,4,6,2,8,5]
l.sort()
print(l)
print(l [0] )

#4.Python program to find second largest number in a list

a=int(input("enter number:"))
l=[]
for i in range(a):
     l.sort()
     l.append(i)
print() 
#8.Program to count Even and odd numbers in a list

n=int(input("enter number:"))
a=[]
b=[]
for i in range(0,n+1):
    if i%2==0:
        x=a.append(i)
        even_count=len(a)
    elif i%2==1:
        y=b.append(i)
        odd_count=len(b)nd(i)
print(even_count)
print(odd_count)

#10Write a Python program that matches a string that has an 'a' followed by anything, ending s
import re
input=input("enter string")
matching=re.match('a+[A-Za-z]+s',(input))
if matching:
    print("matches")
else:
    print("not match")

#9 Write a python program to remove zeros from an IP address("216.08.094.196")
import re
n=("216.08.094.196")
a=re.sub('\.[0]*',',',n)
print(a)

#11 Replace all occurences of 6 with 'six' and 10 with 'ten' for the given string '
# They ate 6 apples and 10 banana'


n=("They ate 6 banana and 10 apple")
a=n.replace("6","six")
b=a.replace("10","ten")
print(b)


#12.Write a program to check whether a person is eligible for voting or not. (accept age from user)



n=int(input("enter age:"))
if n>=18:
    print("person is eligible for vote")

else:
    print("person is not eligible for vote")

#13Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
  #           Unit                                                     Price
#First 100 units                                               no charge
#Next 100 units                                              Rs 5 per unit
#After 200 units                                             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)


a=int(input("enter no of units:"))
if a<=100 and a>=0:
    print("current bill is zero ")
elif a>100 and a<5:
    b=100*5
    print("current bill is ",b," rupees")
elif a>=200:
    c=200*10
    print("current bill is ",c,"rupees")
else:
    print("invaild")
#14.Write a program to accept percentage from the user and display the grade according to the following criteria:

    #     Marks                                    Grade
	 #    > 90                                         A
      #    > 80 and <= 90                             B
       #     >= 60 and <= 80                          C
        #below 60



a=int(input("enter marks:"))
if a> 90 :
    print(" grade A")
elif a> 80 and a<= 90 :
    print(" grade B")
elif a>= 60 and a<= 80:
    print(" grade C")
else:
    print("grade D")'''