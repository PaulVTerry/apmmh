#a/p money market hedge

AP = 400000.0
ForeignBorrowRate = .09
SpotRate = 1.48
DomesticInvestmentRate = .08

MMHtest = (AP/ (1 + ForeignBorrowRate) * SpotRate) * (1 + DomesticInvestmentRate)

print "test", MMHtest


#use code above to check accuracy of code below
#-------------------------------------------------------------------------------
#use code below in CLI

AP = float(input("What are the Account Payables?"))
ForeignBorrowRate = input("What is the foreign borrow/interest rate?")
SpotRate = input("What is the spot rate?")
DomesticInvestmentRate = input("What is the domestic investment rate?")

MMH = (AP/ (1 + ForeignBorrowRate) * SpotRate) * (1 + DomesticInvestmentRate)

print "Okay! Your Money Market Hedge for Accounts Payable is:", MMH
