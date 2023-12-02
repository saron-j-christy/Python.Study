# Program to perform arithmetical operations using Default Arguments
"""you need to place parameters with the default values after other parameters.
Otherwise, we’ll get a syntax error."""

def sum(n1,n2=2):

    return n1+n2

def sub(n1=10,n2=2):

    return n1-n2

def prod(n1,n2):

    return n1 * n2

def div(n1,n2):

    return n1/n2

number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))
result1 =sum(number1)
result2=sub()
result3=prod(number1,number2)
result4=div(number1,number2)
print ("Addition Result " + str(result1))
print ("Subtraction Result " + str(result2))
print ("Multiplication Result " + str(result3))
print ("Division Result " + str(result4))
