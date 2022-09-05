import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

#Setting count as a dictionary, NOT a value or an array
count = {}
for character in message:
 count.setdefault(character, 0) #Create key value pairs for each letter identified in the string
 count[character] = count[character] + 1 # for each character key seen in the sentence add 1 on to the value assigned to that character
print(count) 

#import pprint to better visualise how the dictionary shows the character counts
pprint.pprint(count)