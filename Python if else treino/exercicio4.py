"""Escreva um programa que leia o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte: 

a. Se o número de lados for igual a 3, escrever TRIÂNGULO e exibir o valor de sua área; 

b. Se o número de lados for igual a 4, escrever QUADRADO e exibir o valor de sua área. 

c. Se o número de lados for igual a 5, escrever PENTÁGONO. """
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
    print(f"O valor de lados digitados foi de: {lados} \n Desculpe o dev foi vagabundo e nao criou poligonos com mais de 5 lados")