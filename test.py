# An integer  is input through keyboard.write a program to find whether it is 
# odd or even.

n=int(input("enter number"))
if n%2==0:
    print("even number")
else:
    print("odd number")

# if cost price and selling price of an item is input through keyboard.write a program to determine
# how much profit he made or how much loss he got.
x=float(input("enter cost price"))
y=float(input("enter selling price"))
profit=y-x
if profit>0:
    print(profit," is profit")
elif profit==0:
    print(("no loss no profit"))
else:
    ("invalid value")

# wap to test number is divisible by 3 and 5 both.
num=int(input("enter number:"))
if num%5==0 and num%3==0:
    print("num is divisible by both 3 and 5")
elif num%3==0:
    print("number is divisible by 3")
elif num%5==0:
    print("number is divisible by 5")
else:
    print("num is not divisibleby 3 or 5")

# wap to find a greatest of three  number entered through keyboard.
a=float(input("enter 1st number:"))
b=float(input("enter 2nd number:"))
c=float(input("enter 3rd number:"))
if a>b and a>c:
print("1st>2nd>3rd")
    
# Admission to professional course in a college according to following condition:
# marks in mathematics are greater than or equal to 60 and marks in physics  is greater
# than or equal to 50 and marks in chemistry is greater than or equal to 40
#         or
#total marks in mathematics ,physics, and chemistry is greater than or equal to 200
#        or
#total marks in mathematics ,physics are greater than or equal to 150
# marks of all three subjects will be enterd through the keyboaed.
# WAP to tell wheather a subjects is qualifying for admission or not.
n= int(input("Enter a number: "))
sum=0
for d in str(n):
    sum= sum+d
if s