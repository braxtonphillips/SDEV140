#Braxton Phillips
#SDEV 140
#M01 Chapter 2 Example 10
#In this program a user will input a desired amount of cookies and the program will
# adjust the recipe based on the desired amount.

print('Hello and welcome to this Recipe Adjusting Tool or RAT for short.')
desiredAmount = int(input('Please input the desired amount of cookies you would like to make. Use whole numbers.\n'))

#This portion of the code finds how many ingredients it takes to make 1 cookie
sugarAmount = float(1.5 / 48) 
butterAmount = float(1 / 48)
flourAmount = float(2.75 / 48)
#multiplying the amount to make 1 cookie by the desired amount to determine whta the recipe calls for
adjustedSugarNeeded = float(sugarAmount * desiredAmount)
adjustedButterNeeded = float(butterAmount * desiredAmount)
adjustedFlourNeeded = float(flourAmount * desiredAmount)

print('The amount of sugar you will need for this recipe is', adjustedSugarNeeded, 'cup(s).\n', 
'The amount of butter you will need for this recipe is ', adjustedButterNeeded, 'cup(s).\n',  
'The amount of flour you will need for this recipe is ', adjustedFlourNeeded, 'cup(s).', sep='' )