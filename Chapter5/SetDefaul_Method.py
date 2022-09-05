######################################################################################################
'''                 Understanding and USING the SetDefault() Method                    '''
#######################################################################################################


#If i want to set a value for a key not in a dictionary id have to do it like this which can be computationaly intensive and inefficient

example = {'name': 'Pooka', 'age' :5 }
if 'colour' not in example:
    example['colour'] = 'black'

spam = {'name':'Pooka' , 'age':5}
print("First itteration of Spam lacking colour:", spam)

#Using the setdefault menu , establishing a new key value pair in one line 
print(" Now applying the set default menu i am able to add the colour key+value:\n")
spam.setdefault('color', 'black')
print(spam)

# The set defualt method however CAN NOT OVERWRITE an established key value pair
spam.setdefault('color', 'white')
print("The is no change tot he Colour key of Spam : ", spam)