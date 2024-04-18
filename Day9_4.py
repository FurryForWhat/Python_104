shop = ['motor',30000]
# / // %
tax = int(input('Tax Rate')) #1
tax_price  = (tax*shop[1]) / 100   #30000 /  1
print('Tax-Price is',tax_price)
total_price = tax_price + shop[1] #33000
print("Total cost is",total_price)