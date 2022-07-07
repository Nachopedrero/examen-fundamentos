print("OPERATIVA CUENTA BANCARIA")
# Inicializamos a 0 una variable real para guardar el saldo.
saldo = 0
operaciones = []
# Bucle infinito
while True:
    print("¿Qué deseas hacer?")
    print("1- Ingreso")
    print("2- Reintegro")
    # Preguntamos al usuario por la operación que quiere realizar.
    opcion = input("Elige una opción (cualquier otra para terminar): ")
    # Condicional para ver qué operacion ha seleccionado el usuario.
    if opcion == "1":  
        # Preguntamos al usuario por la cantidad a ingresar y la convertimos en un número real.
        cantidad = float(input("Introduce la cantidad: "))
        operaciones.append(cantidad)
        saldo += cantidad
        # Mostramos el saldo por pantalla.
        print("Saldo: ", saldo)
    elif opcion == "2":  
        # Preguntamos al usuario por la cantidad a reintegrar y la convertimos en un número real.
        cantidad = float(input("Introduce la cantidad: "))
        # Condicional para ver si el hay saldo suficiente para realizar el reintegro.
        if saldo < cantidad: 
            # Mostramos por pantalla un mensaje informando al usuario de que no hay saldo.
            print("Lo siento, no hay saldo suficiente.")
        else: 
            # Añadimos la cantidad en negativo a la lista de operaciones.
            operaciones.append(-cantidad)
            # Restamos del saldo la cantidad del ingreso.
            saldo -= cantidad
            # Mostramos el saldo por pantalla.
            print("Saldo: ", saldo)
    else:  # Si el usuario introduce cualquier otro número el bucle termina
        break
# Creamos dos listas vacías, una para los ingresos y otra para los reintegros.    
ingresos = []
reintegros = []
# Bucle iterativo para recorrer por valor los elementos de la lista de operaciones bancarias.
for i in operaciones:
    if i < 0:  # La operación es un reintegro.
        # Agregramos la operación a la lista de reintegros.
        reintegros.append(i)
    else:  # La operación es un ingreso.
        # Agregamos la operación a la lista de ingresos.
        ingresos.append(i)
# Mostramos la lista de ingresos y reintegros por pantalla.
print("Ingresos: ", ingresos)
print("Reintegros:", reintegros)