#This program returns the sum of the given kth number from num1 and num2

def sumnum(num1, num2, k):
    sum = pow(num1, k)
    for i in range(num1, num2):
        sum = sum + ((i+1) ** k)
    return sum

def mainsum():
    a = 50
    b = 150
    k = 2
    print("The sum of kth power of numbers from a to b is: ", (k,a,b,sumnum(a, b, k)))

mainsum()