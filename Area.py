Base = float(input('Enter the base of your Triangle:'))
Height = float(input('Enter the height of your Triangle:'))

A = (Base*Height)/2
c = (Base**2+Height**2)**0.5
P = c + Base + Height
print('The Area of your triangle is:', A)
print('The Perimeter of your triangle is:', P)
