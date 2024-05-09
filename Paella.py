Personal = float(input("¿Cuántas personas comeran?:"))
Arroz = float(input("¿Cuál es el precio del kilo de arroz?:"))
Gambas = float(input("¿Cuál es el precio del kilo de gambas?:"))

Arroz_total = Personal*0.5/4
Gambas_total = Personal*0.25/4

Precio_total = Arroz_total*Arroz+Gambas_total*Gambas

print('La cantidad utilizada para esta comida será:', Arroz_total, 'kilos de arroz y', Gambas_total, 'kilos de gambas')
print('El coste total será:', Precio_total)