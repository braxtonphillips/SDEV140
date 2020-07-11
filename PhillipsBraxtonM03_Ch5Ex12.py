#Braxton Phillips
#SDEV 140
#M03 Chapter 5 Exercise 12
#Write a function that ouputs the maximum of 2 values put finds the value in a function called 'max'


def main():
    answer = 'y' #makes sure loop runs
    print('\nHello, this program finds the maximum of 2 integer values that you will input.')
    while answer == 'y' or answer == 'Y': #condition controlled loop allows user to keep running program multiple times
        answer = max()
    print('Thank you for using the program!')
   

def max():
    firstNumber = int(input('Please enter the first of two integers that will be tested.\n'))
    secondNumber = int(input('Please enter the second of two integers that will be tested.\n'))
    if firstNumber > secondNumber: #selection structure evalutes user input and displays proper message 
        print(firstNumber,'is the greater of the two values.')
    elif firstNumber < secondNumber:
        print(secondNumber,'is the greater of the two values.')
    else:
        print('The values are equal.')
    answer = input('Would you like to run the program again? Put \'Y\' for yes.')
    print('') #for formatting when output ids displayed
    return answer #by returning 'answer' to the main, the block will read the answer variable and determine if it needs to keep running or not
main()