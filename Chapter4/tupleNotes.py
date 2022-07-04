#Exploring Tuples shell commands

#==============================Section 1
#Tuples use parentheses () instead of the LIST'S  square []

eggs = ('Hello', 45,0.3)
print(eggs[0])
print(eggs[1:3])

# =============================Section 2
#Tuples do not support item assignment/ are IMMUTABLE
#Tuples can not have their values modified

#eggs[1] = 99       X not gona work

#=============================Section 3

#If you only have one value in a tuple you need to declare that it is STILL a tuple with a trailing comma

names = ("joy",) #Keeps it a tuple in python
print(type(names))
names = ("joy") #This becomes a string value
print(type(names))

#============================Section 4 
#Possible to convert types of information using tuple function(and list / str)
print("===========================")
x_val = ["joy", 54, 0.5]
print(tuple(x_val))
print(list(x_val))

#============================Section 5
#The dynamism of List 
#when you assign INTERGERS and STRINGS to a variable, they do not change unless changes are made to the variable
print("===================S5========================")
ham = 45
print(ham)
jam = "strawberry"
ham = jam # This has now been turned in to strawberry as the variable has been augmented
print(ham,jam)

##But this is different with lists. When you assign a variable a LIST
#You are assigning a LIST REFRENCE to that variable

spam = [0,1,2,3,4,5]
cheese = spam  #ASSIGNING A LIST REFRENCE TO THE WORD CHEESE OF SPAM
spam[0] ="IVE CHANGED THIS WORD IN SPAM"
print(cheese)