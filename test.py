cost = float(input('Cost: '))
amount_paid = float(input('Amount paid: '))
penny = 0.01
dime = 0.10
quarter = 0.25
dollar_1 = 1.00
dollar_5 = 5.00
dollar_10 = 10.00
dollar_20 = 20.00
dollar_50 = 50.00
dollar_100 = 100.00
changeTypes = {dollar_100: 0, dollar_50: 0, dollar_20: 0, dollar_10: 0, dollar_5: 0, dollar_1: 0, quarter: 0, dime: 0,
               penny: 0}
change = amount_paid - cost
if amount_paid < cost:
    print('Error: InsufficientFunds')
for changeType in changeTypes:
    numAmount = max(0, change // changeType)
    change -= numAmount * changeType
    changeTypes[changeType] = int(numAmount)

print(changeTypes)
