#Braxton Phillips
#SDEV 140
#M02 Chapter 4 Exercise 14
#Replicating pattern

print('Hello, this program will be used to replicate the pattern in no. 14.')
asteriskNumber = int(input('Please input the amount of asterisks you would like to start with.\n'))
x = 0
y = 0

for x in range( asteriskNumber, 0, -1):
    for y in range( 0, x): 
        print('*', end='')
    print('\n') #prints new line