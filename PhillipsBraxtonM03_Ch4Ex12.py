#Braxton Phillips
#SDEV 140
#M02 Chapter 4 Exercise 12
#This program will use loops to compute a the factorial of a number.

print('Hello and welcome to the factorial calculation program.')
n = int(input('Please enter a number you would like to know the factorial of.\n'))
factorial = 1 #initalizing facortical variable to 1 
#Loop keeps the user from entering negative numbers
while n < 0:
    print('Error. You can only enter positive integers.')
    n = int(input('Please enter a positive number you would like to know the factorial of.\n'))

for n in range(1, n + 1):
    factorial = factorial * n #here the factorial value is "storing" the product from the previous number and the incremented value
print(n,'!=', factorial)