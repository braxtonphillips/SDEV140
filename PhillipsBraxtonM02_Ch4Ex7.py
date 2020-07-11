#Braxton Phillips
#SDEV 140
#M02 Chapter 4 Exercise 7
#This program is used to calculate how much a person would make if they start with 1 penny and their compensation doubles everyday after.

print('Hello, this program will be used to calaculate a salary paid in pennies that doubles everyday.')
daysWorked = int(input('Please input the amount of days you worked.\n'))
#Using a while loop as a defensive measure to stop the user from entering negative numbers.
while daysWorked < 0:
    print('Error. You can only enter positive integers.')
    daysWorked = int(input('Please input the amount of days you worked.\n'))
salary = int(1)

if daysWorked > 0: #For when the user enter a positive integer, the program executes the block statment under the if clause
    print('\nDay\tSalary')
    print('*******************')

    for daysWorked in range(1,daysWorked + 1):
        print(daysWorked, '\t $', salary/100)
        salary *= 2
else: #for if the user enters 0 
    print('Since you worked 0 days, you will have earned $0.00')