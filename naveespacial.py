from multiprocessing.sharedctypes import Value
#la idea es dividir la distancia recorrida entre el tiempo que tardo en recorrerla, y esto nos dara un valor similar al de la gravedad.
#ese valor va a ser restado a la gravedad de cada planeta y el numero mas bajo generado sera el de la gravedad mas probable
#luego buscamos de donde resulta el numero mas bajo(de restar la gravedad de que planeta), y el planeta en cuestion sera el que tiene mas probabilidades

diccplanetas = {"marte":3.23,"tierra":9.81, "jupiter":29.72,"saturno":9.53,"urano":8.71,"neptuno":11.3}
lista = [3.23,9.81,29.72,9.53,8.71,11.3]
listanums = []
for i in lista:
    valorg = 2 / 0.36
    numero =  i - valorg 
    numero.append(listanums)

#no se puede hacer append porque es un float
for i in lista:
    valorg = 1 /0.36 
    numero = i - valorg
    numero.append(listanums)  

listanums.sort
#buscamos ver cual es el planeta que coincide con la gravedad mas correcta segun los calculos
for i in lista:
   if listanums(0) + numero == i:
    correcto = i 
    print("a este planeta seguramente le corresponda una gravedad de " , i)
for j in diccplanetas:

    if diccplanetas.values == correcto:
        print (diccplanetas.key)






