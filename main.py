 #write a prg  tht accepts a sentence and calculate the number of
 #of letters and digits.suppose the following input is supplied
 #to the prgm:hello world!123
#then the output should be :
#LETTERS 10
#DIGITS 3


"""a=input("enter a string")
count1=count2=0
for count in a:
   if count.isdigit():
       count1+=1
   if count.isalpha():
        count2+=1
   print("digits-",count1)
   print("letters-",count2)"""


#write a prg that reads in a string on the command line and returns a  tables of the frequency
#of each word.ignore the case .A sample run of the program would look ths
#Enter some letters >>>
   # The -2
  #  Cat-1
   # In-1
  #  Hat-1#This should involve writing a fnction that takes in a string an retun a dicitionary with these
#letters and count.



"""sentence=input("enter the string").lower()
x=sentence.split(" ")
y=[]
for i in x:
    if y.count(i)==0:
        y.append(i)
        print(i.title(),"-",sentence.count(i))#print the details"""



#write a python prgm to check the validity of a password input by the user.the password should
#satisfy the following conditions:



import re
a=(input("enter a string"))
if int(len(a)<6 or len(a)<=12):
   if(re.search("[A-Z]",a) and re.search("[a-z]",a)and re.search("[0-9]",a)and re.search("[@#s]",a)):
       print("it is a valid password")
  else:
        print("it is an invaild password")
else:
     print("The password you entered is wrong")





#question 5


"""a=input("enter the string")
target word=input("enter the target word")
word=a.split()
index=0
position=[]
for word in words:
    if word=target word
    position.appends(index)
    index+1"""


#question1

a=int(input("enter the input:"))
b=int(input("enter the input:"))
c=int(input("enter the input"))
x= y= 0
if(a==0):
    print("error")
else:
    discriminant=b ** 2 -4 * a * c
    if(discriminant<0):
        print("error")
    else:
        x=((-b+(discriminant **0.5 ))/ 2 * a)
        y=((-b-(discriminant **0.5 ))/ 2 * a)
print(x)
print(y)



  

