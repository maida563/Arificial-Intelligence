# Task 1
for i in range(1500,2701):
     if(i %7==0 and i%5==0 ):
          print(i)
print("These are the numbers that are divisible by 7 and multiples of 5")

# Task 2
def convert_temp():
    temperature=float(input("Enter temperature: "))
    type=input("Enter C or F: ")
    if type =='c'or type=='C':
          result = (temperature/5)*9+32 
          print(f"{temperature} celsius in fahrenheit is {result}")
    elif type=='F' or type=='f':
          result=(temperature-32)/9*5 
          print(f"{temperature} fahrenheit in celsius is {result}")
    else:
        print("Wrong Input!!")

convert_temp()        

#Task 3
# Guess number
import random
hidden=random.randint(1,9)
while True:
    user=int(input("Enter your guess: "))
    if(user==hidden):
        print("Weldone!You guessed right.")
        break
    else:
        print("You guessed wrong!")    


# Task 4
# Print 5x9
ch ='*'
for i in range(1,6):
    print(ch * i)
for j in range(4,0,-1):
    print(ch*j)

# Task 5
user= input("Enter any string: ")
l=len(user)
for i in range(len(user),0,-1):
    print(user[::-1])

# TAsk 6
num=[]
for i in range(5):
    user=int(input("Enter a series of numbers"))
    num.append(user)
i=0
j=0
for u in num:
    if(u%2==0):
        i+=1
    elif (u%2!=0):
        j+=1 
    else:
        print("Invalid Input")    

print(f"Even numbers: {i}")
print(f"Odd numbers: {j}")    

# Task 7
list=[[1,2,3,4],"Apple",'Q',1.345,100,True]
for i in list:
    print(i, "is of ",type(i)," type")

# Task 8
num=[0,1,2,3,4,5,6]
for i in num:
    if i==3 or i==6:
        continue
    print(i)

# Task 9
# Fibonacci Series
a=0
b=1
c=1
while c<51:
    print(c)
    c=a+b
    a=b
    b=c

for i in range(1,51):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)

# Task 10
m= int(input("Rows= "))
n= int(input("columns: "))
arr=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(i*j)
    arr.append(row)    

print (arr)    

# Task 11
# Accept sequence of lines
lines = []
print("Enter your lines: ")
while True:
    s=input()
    if s=="":
        break
    lines.append(s)
for line in lines:
    print(line.lower())    

# Task 12
# Comma separated 4 digit numbers
data = input("Enter binary numbers: ").split(',')

result = []
for binary in data:
    if int(binary, 2) % 5 == 0:
        result.append(binary)

print("Expected output: ")
print(','.join(result))

# Task 13
s = input("Enter string: ")
letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print(f"Letters {letters}")
print(f"Digits {digits}")



# Task 14
import re

password = input("Enter password: ")

if (6 <= len(password) <= 16 and
    re.search("[a-z]", password) and
    re.search("[A-Z]", password) and
    re.search("[0-9]", password) and
    re.search("[$#@]", password)):
    print("Valid Password")
else:
    print("Invalid Password")