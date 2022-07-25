myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

## The keys of this dictionary type are Size, Color , Disposition
## Can access these values through their keys

print(myCat['size'])
print ("This is the value for key 2 (Color): ", myCat['color'] ,"\nWhile This is the value for key 3  (Disposition):" , myCat['disposition'])

print("My cat has " + myCat['color'], "Fur")

## Dictionaries can still use Integer values as Keys

spam_numerical = {12345: 'Luggage Combination', 42: 'The Answer'}

##Exercise 1 
## Understanding that the order of dictionaries does not matter. a list variable assigned to SPAM, SPAM[0] will always return the same value

print(" ============================================================= \n")

# These 2 lists will not equate eachother as the order is MUMBLED
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print( spam == bacon) 

#These 2 DICITONARYS will equate to eachother as they contain the exact same key-value pairs 
#DESPITE a mumbeled order
eggs = {'name':'Romeo', 'Species':'cat' , 'Age':'5'}
ham = { 'Species':'cat', 'Age':'5', 'name':'Romeo' }
print (eggs == ham)

#Trying to access a key not in a dictionary will results in a KeyError