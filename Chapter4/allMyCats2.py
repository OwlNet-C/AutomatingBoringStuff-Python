
cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1)+
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break # As they entered nothing the ENTIRE  while Loop breaks
    cat_names = cat_names + [name] #list concatenation
print("the cat names are ")
for name in cat_names:
 print("->",name)