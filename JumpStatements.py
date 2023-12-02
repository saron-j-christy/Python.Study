#Program to sum only positive numbers in the input

limit = 5

start = 1

sum = 0

flag = True 

while(flag) :

    if start == limit :

        break
    
    number = int (input ("Enter the number"))

    if ( number < 0) :
        continue 
    else :

        sum = sum + number

    start = start + 1

print (" sum of positive numbers " + str(sum))

print (" Program End ")


