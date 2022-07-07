import random 
preciocaramelo = 350
preciovacio = 50
cantllenos = random.randint(10,20)
cantvacios = random.randint(1,100)
total = cantllenos + cantvacios
descuento = (cantllenos + cantvacios) // 20 
preciototal = (preciocaramelo * cantllenos) + (preciovacio * cantvacios) - (descuento * 70)
precioeuros = preciototal /100
print("compraste ", cantllenos, " caramelos llenos")
print("tambien compraste ", cantvacios, " caramelos vacios")
print ("el producto costo  ", precioeuros, " euros")