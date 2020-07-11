#Braxton Phillips
#SDEV 140 
#M02 Chapter 3 Exercise 16
#THis program will be used to determine if the user entered year is a leap year and will display the amount of days in february

print('Hello, this program will read user input to determine if the year in question is a leap year or not and the number of days in February')
#Decided to put in a while so so i dont have to debug whole program if i want to put in a new year.
keepGoing = 'y' #declaration of variable used to determine if loop will keep going
while keepGoing == 'y': #pre-test loop
    year = int(input('Please enter a year.\n'))
    #Here we use the modulous operator % to check if there is a remainder. If there is, the condition is not met and the year is checked in the elif clause
    if year % 400 == 0: 
        print('In the year,', year, ', February has 29 days and is thus a leap year.')
    elif year % 100 != 0  and year % 4 == 0: #Here the 'AND' logigcal oporator is used to determine if the compound condition true
        print('In the year,', year, ', February has 29 days and is thus a leap year.')
    else:
        print('In the year', year, ', February only has 28 days and is not a leap year.')
    keepGoing = input('Please enter \'y\' to perform operation again or any other key to exit. ')
    print('\n') #for formatting