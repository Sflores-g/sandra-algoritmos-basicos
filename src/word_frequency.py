lista = {}
frase = input("Frase:")
lista_palabras=frase.split(" ")
caracteres = [":",",","@", "!", "."]

for palabra in lista_palabras:
	if palabra in caracteres:
		continue
	
	if palabra in lista:
		lista[palabra]+=1
	else:
		lista[palabra]=1	

sorted(lista)

for campo,valor in lista.items():
	
	print (campo,"->",valor)

