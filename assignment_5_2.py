#This function returns the sum of functions from num1 to num2 (both inclusive)
def sumnum(num1, num2):
    sum = num1
    for i in range(num1, num2):
        sum = sum + (i+1)
    return sum

def mainsum():
    a = 50
    b = 150
    print("The sum of numbers from a to b is:", (a, b, sumnum(a, b)))

mainsum()
