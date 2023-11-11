contador = 0
numero_varitas = 0
sauco = 0 
espino = 0
sauce = 0 
acebo = 0

cliente = input("¿Hay algún cliente? (si/no)")

while cliente == "si":
    contador += 1
    varita = input("¿Se ha vendido una varita? (si/no)")
    if varita == "si":
       print("1. Varita de Saúco 2. Varita de Espino 3. Varita de Sauce 4. Varita de Acebo")

    tipo_de_varita = int(input("Qué varita se ha comprado?"))
    if tipo_de_varita == 1:
        sauco += 1
        cliente = input("¿Hay algún cliente? (si/no)")
    elif tipo_de_varita == 2:
        espino += 1
        cliente = input("¿Hay algún cliente? (si/no)")
    elif tipo_de_varita == 3:
        sauce += 1
        cliente = input("¿Hay algún cliente? (si/no)")
    elif tipo_de_varita == 4:
        acebo += 1
        cliente = input("¿Hay algún cliente? (si/no)")
    else:
        print("No se ha encontrado el tipo de varita")
        cliente = input("¿Hay algún cliente? (si/no)")
        break

print(f"Hoy vinieron {contador} clientes")
print(f"Número de varitas de Saúco vendidas: {sauco}")
print(f"Número de varitas de Sauce vendidas: {sauce}")
print(f"Número de varitas de espino vendidas: {espino}")
print(f"Número de varitas de Acebo vendidas: {acebo}")
