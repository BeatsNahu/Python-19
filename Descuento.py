print('Enter the initial price')
inicial = float(input())

print('Enter the final price')
Final = float(input())

Bills = (Final*100)/inicial
Discount = round((100-Bills),2)
print('You get a discount of', Discount,'%')