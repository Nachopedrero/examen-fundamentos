def conversion_hex_bin(num_hex):
  
    # Definimos un diccionario con el número binario asociado a cada dígito hexadecimal
    hexbin = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    # Inicializamos la cadena para guardar el número binario a la cadena vacía.
    num_bin = "" 
    # Bucle iterativo para recorrer los dígitos del número hexadecimal por valor. i toma como valores cada uno de los caracteres que forman la cadena con el número hexadecimal.
    for i in num_hex: 
        try:
            # Accedemos al diccionario mediante la clave correspondiente al dígito hexadecimal y añadimos a la cadena con el número binario los dígitos binarios correspondientes al dígito hexadecimal.
            num_bin += hexbin[i]
        # Controlamos la excepción en caso de que alguno de los dígitos del número hexadecimal no sea válido.
        except KeyError:
            return "El número introducido no es hexadecimal."
    # Devolvemos la cadena con el número binario.
    return num_bin

def conversion_bin_dec(num_bin):
    """
    """ 
    # Convertimos la cadena con el número binario en una lista de caracteres. Cada dígito del número binario es un elemento de la lista.
    num_bin = list(num_bin) 
    # Para recorrer la lista de derecha a izquierda la invertimos.
    num_bin.reverse()
    # Inicializamos a 0 una variable entera para ir guardando el número decimal. 
    num_dec = 0 
    # Bucle iterativo para recorrer la lista de dígitos binarios por posición. i toma como valores los enteros de la secuencia desde 0 al tamaño de la lista menos 1.
    for i in range(len(num_bin)): 
        # Multiplicamos el dígito binario por la potencia de 2 correspondiente a la posición del dígito en la lista y lo sumamos al número decimal.
        num_dec += int(num_bin[i]) * 2 ** i 
    # Devolvemos el número decimal
    return num_dec

def maximo_hex(lista_hex):
    """
    Función que devuelve el número mayor de una lista de números hexadecimales.
    """
    # Inicializamos una lista vacía para guardar los números decimales correspondientes a los números hexadecimales.
    lista_dec = []
    # Bulce iterativo para recorrer los valores de la lista de números hexadecimales. i toma como valores cada uno de los números hexadecimales de la lista.
    for i in lista_hex:
        # Aplicamos a cada número hexadecimal la función de conversión a binario y después la función de conversión a decimal y añadimos el número decimal obtenido a la lista de números decimales.
        lista_dec.append(conversion_bin_dec(conversion_hex_bin(i)))
    # Obtenemos el máximo valor de la lista de números decimales.
    max_dec = max(lista_dec)
    # Obtenemos el número hexadecimal máximo accediendo a la misma posición de la lista de números hexadecimales que ocupa el máximo de la lista de números decimales.
    max_hex = lista_hex[lista_dec.index(max_dec)]
    # Devolvemos una tupla con el número hexadecimal máximo y su valor decimal.
    return (max_hex, max_dec)

def minimo_hex(lista_hex):
    """
    Función que devuelve el número mayor de una lista de números hexadecimales.
    """
    # Inicializamos una lista vacía para guardar los números decimales correspondientes a los números hexadecimales.
    lista_dec = []
    # Bulce iterativo para recorrer los valores de la lista de números hexadecimales. i toma como valores cada uno de los números hexadecimales de la lista.
    for i in lista_hex:
        # Aplicamos a cada número hexadecimal la función de conversión a binario y después la función de conversión a decimal y añadimos el número decimal obtenido a la lista de números decimales.
        lista_dec.append(conversion_bin_dec(conversion_hex_bin(i)))
    # Obtenemos el máximo valor de la lista de números decimales.
    min_dec = min(lista_dec)
    # Obtenemos el número hexadecimal máximo accediendo a la misma posición de la lista de números hexadecimales que ocupa el máximo de la lista de números decimales.
    min_hex = lista_hex[lista_dec.index(min_dec)]
    # Devolvemos una tupla con el número hexadecimal máximo y su valor decimal.
    return (min_hex, min_dec)

# Ejemplo de prueba
print("El número hexadecimal AA55 es", conversion_bin_dec(conversion_hex_bin("AA55")), "en binario.")

hex = ["AA55", "1010", "BEBE", "0101", "0FEA"] 
print("el maximo valor es: " ,maximo_hex(hex))
print("el minimo valor es: " ,minimo_hex(hex))