#Braxton Phillips
#SDEV 140
#M01 Chapter 2 Example 14
#This program will be used to calculate compount intreset on an account. The user will input
# the principal, intrest rate, yearly number of times it is compunded, and the amount of years. 

print("""Hello, this program is a compound intrest calculator. Using the data you will input, the 
program will determine the amount of intrest your account will accrue.\n""")

#user input for data
principalAmount = float(input('Please enter the prinicpal amount in the account. '))
rateOfInterest = float(input('Please enter the intrest rate on the account. For example 2% would just be entered as \'2\'. '))
numberOfCompounds = int(input("""Please enter the number of times per year the intresr is compounded. For example, 12 for monthly, 
 4 for quarterly, et. Only use whole numbers. """))           #used triple quoutes to utilize multi-line for presentation
timeInYears = float(input('Please enter the amount of years the account will be left to earn intrest. '))

#the calculation will now be performed using the compunt intrest formula
moneyFromIntrest = format((principalAmount * (1 + ((rateOfInterest/100) / numberOfCompounds))**(numberOfCompounds * timeInYears)),'.2f')
#formatting to a precision of 2 to properly simulate a bank account

print('\nAfter ', timeInYears, ' year(s), at an intrest rate of ', rateOfInterest, '% and ', numberOfCompounds, ''' compound(s) per year,
your intital principal of $''', principalAmount, ' has grown to $', moneyFromIntrest, '!', sep='')