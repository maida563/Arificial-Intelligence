print("\nList Iteration")
l=["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i) 

# String Iteration
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)


list= ["geeks", "for", "geeks"]
for index in range (len(list)):
    print (list[index])    

# continue takes control to the start of the loop body
for letter in 'Geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print("Current letter: " ,letter)

# break takes control out of the loop body
for letter in 'Geeks for geeks':
    if letter=='s' or letter=='e':
        break
print("Current letter: " ,letter)

#   Defining and calling functions
def my_function(fname): 
    print(fname + " Refsnes") 

my_function("Emil") 
my_function("Tobias") 
my_function("Linus") 

def my_function(country = "Norway"):
     print("I am from " + country) 

my_function("Sweden")  
my_function("India")  
my_function()  
my_function("Brazil")

# Passing parameters as a list
def my_function(food): 
    for x in food: 
        print(x) 

fruits = ["apple", "banana", "cherry"] 
my_function(fruits) 

                                    # Insertion Sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]
print("My list is: ",mylist)

for i in range(1,len(mylist)):
    key= mylist[i]
    j=i-1
    while j>=0 and mylist[j]>key:
        mylist[j+1] =mylist[j]
        j=j-1
    mylist[j+1] =key

print("Sorted list: ", mylist)    
