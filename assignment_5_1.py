#This program finds the sum of numbers from 1 to 100.
def sumnum():
    sum = 1
    for i in range(1,100):
        sum= sum + (i+1)
    return sum

print("The sum of numbers from 1 to 100 = ", sumnum())



