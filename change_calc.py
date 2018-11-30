from decimal import Decimal

denominations = {'10 pesewas': Decimal('0.10'), '20 pesewas': Decimal('0.20'), '50 pesewas': Decimal('0.50'),
                 '1 cedi': Decimal('1.00'),
                 '2 cedi': Decimal('2.00'),
                 '5 cedi': Decimal('5.00'), '10 cedi': Decimal('10.00'), '20 cedi': Decimal('20.00'),
                 '50 cedi': Decimal('50.00')}

amount = Decimal(input('Enter amount: '))

price = Decimal(input('Enter price of the item: '))
ans = amount - price

for den in denominations.items():
    if den[1] == ans:
        print('change: {}'.format(den[0]))
        break
    else:
        pass
        #sort denominations in descending order
        #do ans% denominations (finding the modulus)
        #There you go bingo!!
        
