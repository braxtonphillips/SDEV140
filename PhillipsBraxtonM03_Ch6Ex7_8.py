#Braxton Phillips
#SDEV 140
#M03 Chapter 6 Exercise 7 & 8
#Random number file writer and reader

#importing the random module to utilize the randit function
import random
def main():
    try:
        total = 0 #used to accumulate the total the numbers are processed by the control loop
        number_file = open('randoms.txt','w') #by opening the randoms text file in write mode, i can call it from the other funcs as a parameter 
        print('Hello, this program will creat a list of random number and write them to a file before reading them back to you.')
        userInt = int(input('Please indicate how many random numbers you would like to create.\n'))

        for count in range(0, userInt):
            number = random.randint(1,500)
            count += 1
            total += number
            writer(number_file, number)
        number_file.close

        #excerise 8
        print('\nBelow are the numbers from the randoms.txt file:')
        number_file = open('randoms.txt','r')
        for line in number_file:
            reader(line)
        print('There were ', userInt, ' numbers listed in the randoms.txt file. Their total is ', total,'!', sep='')
    except Exception as err:
        print(err)

#fucntion for  excerise 7
def writer(number_file, number):
    number_file.write(str(number) + '\n')

#function for excerise 8 although it prints the variables as a string unstead of int
def reader(line):
    line = line.rstrip('\n')
    print(line)
    
main()