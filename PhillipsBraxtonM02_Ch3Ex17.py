#Braxton Phillips
#SDEV 140
#M02 Chapter 3 Exercise 17
#Use selcetion strucutre to replicate wifi diagnostic tree

print('Hello and welcome to the Diganostic Instructional Replication Tree, or DIRT, for Wi-fi Troubleshooting.\n\n')
print('If you are having and issue, reboot the computer and try to connect again.')
userAns = input('Did that fix the problem? Please enter yes or no. \n')
#if previous input for userAns is no, the if-statement will execute and prompt user to see if issue is fixed. If fixed program will print thank you message.
#If not fixed, code will execute necxt branch of if statement
if userAns == 'no' or userAns == 'No' or userAns == 'NO': #defensive prgraming if user uses 
    print('Reboot the router and try to connect.')
    userAns = input('Did that fix the problem? Please enter yes or no.\n')
    if userAns == 'no' or userAns == 'No' or userAns == 'NO':
        print('Make sure hte cales between the router and modem are plugged in firmly.')
        userAns = input('Did that fix the problem? Please enter yes or no.\n')
        if userAns == 'no' or userAns == 'No' or userAns == 'NO':
            print('Move the router to a new location and try to connect.')
            userAns = input('Did that fix the problem? Please enter yes or no.\n')
            if userAns == 'no' or userAns == 'No' or userAns == 'NO':
                print('Get a new router.')
print('\nThank you for using the DIRT program!')