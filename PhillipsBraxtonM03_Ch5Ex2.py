#Braxton Phillips
#SDEV 140
#M03 Chapter 5 Example 2
#This assignment is using Ch2 Ex 6 as a basis to implement a modular design with functions.

#declaration of global constants
STATE_TAX_AMT = 0.05
COUNTY_TAX_AMT = 0.025
purchaseAmount = 0 #using this to initialize the purchase amount value

#In this main function the user will input the purchase amount. the purchaseAmount variable is passed through the taxesFunc as an argument
#and the be evaluated at the taxesFunc as a parameter
def main():
    print('Hello, this program is used to calculate sales tax.')
    global purchaseAmount
    purchaseAmount = float(input('Please input the purchese amount. Do not include a dollar sign($).\n'))
    tax1, tax2, taxSum = taxesFunc(purchaseAmount)
    print('\nThe purchase amount you entered was: $',purchaseAmount, sep='')
    print('The County sales tax is: $', tax2, ', the State sales tax is: $', tax1, ' and the combined total of both sales taxes is: $', taxSum, sep='')
    print('The combined total of both sales taxes is: $', taxSum, sep='')
    purchaseAmount += taxSum #adds tax sum and purchase amount to equal order total
    purchaseAmount = float(format(purchaseAmount,'.2f'))
    print('Your final total for the sale is: $', purchaseAmount, sep='')
   
def taxesFunc(amount):
    stateTax = amount * STATE_TAX_AMT
    countyTax = amount * COUNTY_TAX_AMT
    taxesTotal = stateTax + countyTax
    return stateTax, countyTax, taxesTotal

main()