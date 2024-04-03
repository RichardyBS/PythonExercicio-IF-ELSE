"""Acrescente às seguintes mensagens à solução do exercício anterior conforme o caso: 

a. Caso o número de lados seja inferior a 3, escrever NÃO É UM POLÍGONO; 

b. Caso o número de lados seja	 superior a 5 escrever POLÍGONO NÃO IDENTIFICADO; """

import math

lados = int(input("Digite os lados do Poligono Regular:  "))

medida_lado = float(input("Digite a medida do lado (em cm): "))

perimetro = lados * medida_lado

area = (lados * medida_lado**2) / (4 * math.tan(math.pi / lados))

poligono = ""

if lados == 3:
    poligono = "Triangulo"
    print(f"A área do {poligono} é {area:.2f} cm².")
    print(f"O perímetro do {poligono} é {perimetro:.2f} cm.")

elif lados == 4:
    poligono = "Quadrado"
    print(f"A área do {poligono} é {area:.2f} cm².")
    print(f"O perímetro do {poligono} é {perimetro:.2f} cm.")


elif lados == 5:
    poligono = "Pentagono"
    print(f"A área do {poligono} é {area:.2f} cm².")
    print(f"O perímetro do {poligono} é {perimetro:.2f} cm.")

else:
    print(f"O valor de lados digitados foi de: {lados} \n Desculpe o dev foi vagabundo e criou 3 a 5 lados")