bill_amount = float(input('How much was the bill? '))
tip_amount = float(input('How much do you want to tip (1-100)?')) / 100
print('Your tip amount is:')
print(bill_amount * tip_amount)
