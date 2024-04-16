opc=0

while(opc !=4):
    print("***Bienvenido a PokeCards***")
    print("1. Detalle cartas Pokemon")
    print("2. Comprar cartas Pokemon")
    print("3. Visualizar resumen de compra realizada")
    print("Salir")
    try:
        opc= int(input("Ingrese opcion → \t"))
    except:
        print("Debe ingresar sólo números")
# if(opc==1):
#     print("Detalle Cartas Pokemon")
#     print("Carta comun, VALOR $ 5000")
#     print("Carta Rara VALOR $10000")
#     print("Carta Legendaria VALOR $20000")
#     print("Tenemos nuestra opción Set Entrenador por $50000 (incluye una selección especial de cartas foil)")
#     print("Deseas información de otros servicios, presiona una tecla para continuar")
#     print("Por la compra de compra más de 5 cartas en una sola transacción, recibirá un descuento del 10% sobre el total")
#     print("Si la compra es realizada en efectivo recibirá un 5% adicional.")
#     print("Si eliges delivery se le hará un recargo de $3500 (no aplicable a descuento)")
# elif(opc==2):
#     print ("compra tus cartas pokemon")
