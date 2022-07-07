import random
preciobitcoin = 20.132,54
numerobitcoins = random.randint(2,15)
dolares = random.randint(1000,10000)
dinero = numerobitcoins * preciobitcoin
#la funcion no esta recibiendo los parametros numero de bitcoins y preciobitcoin, ya que me estaba dando error y en lugar obtiene dinero, que resulta de multiplicar las dos anteriores

def Dolaresaeuros (dinero):
    
    precioeuros =+ dinero
    return precioeuros
precioeuros = Dolaresaeuros(dinero) 

if precioeuros < 10000 :
    print("el valor de sus bitcoins esta cayendo por debajo de 10000 euros")  

print(precioeuros)
#he creado un random que nos da dolares para que el capital no fuera solo en valor de las bitcoins en euros
capital = dolares + precioeuros
tipointeres = input("introduzca en porcentaje el tipo de interes que tiene su banco (anualmente) ")
numeroaños = input("durante cuantos años va a invertir su dinero")
#creamos un bucle para cada año de interes, ya que esta operacion del interes en porcentaje se realizara tantas veces como numero de años este 
def Dinerofinal(capital,numeroaños,tipointeres):
    for i in  numeroaños:
        capital =+ tipointeres * capital/100
    print (capital)    
#la diferencia con el metodo anterior es que cada año nos va a decir el capital que tendia ese mismo año y lo va a meter en una lista
lista=[]
def  Dineroactual(capital,numeroaños,tipointeres):
    for i in  numeroaños:
        capital =+ tipointeres * capital/100
        capital.append(lista)
        


print(Dineroactual)
seleccion = input("en que año quiere conocer su capital?:")
#le imprimimos el año que nos pidio(la cantidad de capital de ese año)
print(lista[seleccion + 1])
        
