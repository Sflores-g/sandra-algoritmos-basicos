lista = {}
frase = input("Frase:")
lista_palabras=frase.split(" ")
caracteres = [":",",","@", "!", ".", ";", "?", " "]

for palabra in lista_palabras:
	if palabra in caracteres:
		continue
	
	if palabra in lista:
		lista[palabra]+=1
	else:
		lista[palabra]=1	

lista_ordenado = sorted(lista.items(), key =lambda x: x[1], reverse=True)
#print(lista_ordenado)

for campo,valor in lista_ordenado:
	
	print (campo,"->",valor)

