#Braxton Phillips
#SDEV 140
#M02 Chapter 3 Exercise 12
#This purpuse of this program is to calculate the amount a discount,
# if any, based on quantity of packages being purchased.

print('Hello, this progam will read user input to determine if a discount is applicable based on order quantity.')
packageQuantity = int(input('Please enter the amount of packages you will be purchasing. \n'))

#I read ahead some in the book. This while loop is used as defensive programming to stop the user from entering
#Non-positive integers. 
while packageQuantity <= 0:
    print('Error. Please enter a valid number.')
    packageQuantity = int(input('Please enter the amount of packages you will be purchasing. \n'))
#Selection strucure used to determine which paclage is approriate based on used input 
if packageQuantity < 10:
    totalAmount = float(format(packageQuantity * 99, '.2f')) 
    print('Your total for this order will be $',totalAmount, sep='') 
elif packageQuantity < 20:
    totalAmount = float(format((packageQuantity * 99)*.9, '.2f')) #chose to multiply by .9 rather than the diff of totalAm from 10% of totalAm
    print('For ordering ',packageQuantity,' packages, you have recieved a 10% discount! This brings your total for this order to $', totalAmount, sep='')
elif packageQuantity < 50:
    totalAmount = float(format((packageQuantity * 99)*.8, '.2f'))
    print('For ordering ',packageQuantity,' packages, you have recieved a 20% discount! This brings your total for this order to $', totalAmount, sep='')
elif packageQuantity < 100:
    totalAmount = float(format((packageQuantity * 99)*.7, '.2f'))
    print('For ordering ',packageQuantity,' packages, you have recieved a 30% discount! This brings your total for this order to $', totalAmount, sep='')
else:
    packageQuantity >= 100
    totalAmount = float(format((packageQuantity * 99)*.6, '.2f'))
    print('For ordering ',packageQuantity,' packages, you have recieved a 40% discount! This brings your total for this order to $', totalAmount, sep='')