num = -1
counter = 0
answer = 0
anyNumber = int(input("Enter any number: "))
while anyNumber > num:
    counter += 1
    answer += anyNumber
    anyNumber = int(input("Enter another number: "))
if (counter==0): print (answer) #in case the first number entered was -1
else:
    print (answer/counter) #print average
print ("Good bye!")