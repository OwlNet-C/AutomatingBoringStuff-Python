
#Common python technique using range(len(list))
#Allows you to iterate through the whole list 
#Lets you identify index of list values using I
#While also allowing you to call the INDEX NAME using I

Supplies = ['pen','calc','eraser','rubber']
for i in range(len(Supplies)):
    print( "index " + str(i) + ' in supplies is ' + Supplies[i])
