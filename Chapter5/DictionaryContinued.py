#The are 3 main dictionary methods 
'''
Keys()
Values()
Items()
'''

'''                 VALUES              '''
spam = {'Color':'red','age':42}
for v in spam.values():
    print(v)

#Will print out the Value pairs 
#So in this case will print out "red" and "42"

'''                 KEYS                     '''
spam = {'Color':'red','age':42}
for v in spam.keys():
    print(v)
#Will print out the Key pairs 
#So in this case will print out "Color" and "age"

'''                 Items                   '''
spam = {'Color':'red','age':42}
for v in spam.items():
    print(v)

#Will print Out the entire dictionary values
#('color', 'red')
#('age', 42)

print("################################################################")
'''         Returning the TUPLE of items as a list can be done          '''
#This will return it in a true List format
print(list(spam.items()))

#You can also use multiple assignment to make it look nicer and assigned in to seprate variables
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

'''                 Checking whether a key or value exists in a dictionary                  '''
print("Checking whether a key or value exists in a dictionary:\n")

spam = {'name': 'Zophie', 'age': 7}
#Using IN we can check if values are inside a dictionary, should print TRUE or FALSE
print("name" in spam.keys())  #TRUE Checking the KEY first
print("Zophie" in spam.values()) #Checking to NOW see the Value
print("color" in spam.keys()) #FALSE
print("color" in spam) # This way is shorter way of writing spam.KEYS STILL LOOKING AT KEYS
######################################################################################################
'''                 Understanding and USING the GET() Method                    '''
#######################################################################################################
print("\nUnderstanding the GET() Method:\n" )
#It is tedious to first check if a key exists in dictionary THEN AGAIN accessing the keys value.
#The GET method takes TWO arguments. First the KEY and then a DEFAULT(MADEUP) Value to RESORT back to if no VALUE is found

picnicItems = {'apples': 5, 'cups': 2, 'bread':2}
#APPLES 5      CUPS 2 
print("Checking to see if there is a value:")
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.\n')
#This is accessing the CUPS key, THE DEFAULT value will be 0 IF IF IF IF IF It does not find a value
#When this line is executed , it returns 2 as it was able to find the are 2 cups in the dictionary
# Thinking of this in a real life scenario , if NO CUPS were found, the default value would be 0

print("No Key present:")
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.\n')
#Eggs is not a valid key, so will also return 0 , just as the default value states

#Separate attempt
print("Mum the is only " +str(picnicItems.get('bread',1)) + " loaves of bread.\n")




