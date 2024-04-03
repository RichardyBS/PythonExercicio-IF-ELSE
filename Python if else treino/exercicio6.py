"""Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é um EQUILÁTERO, ISÓSCELE ou ESCALENO. Sendo que: 

a. Triângulo equilátero: três lados iguais; 

b. Triângulo isóscele possui 2 lados iguais; 

c. Triângulo escaleno possui 3 lados diferentes; """
lado1 = int(input("Digite valor a medida do primeiro lado:   "))
print(f"o valor colocado para a primeira medida foi de: {lado1}")

lado2 = int(input("Digite valor a medida do segundo lado:   "))
print(f"o valor colocado para a segunda medida foi de: {lado2}")

lado3 = int(input("Digite valor a medida do terceiro lado:   "))
print(f"o valor colocado para a terceira medida foi de: {lado3}")

if lado1 == lado2 == lado3:
  print(f"Como o primeiro lado e de:  {lado1}\nComo o segundo lado e de:  {lado2}\nComo o terceiro lado e de:  {lado3} ele e um Triângulo equilátero pois os 3 lados sao iguais.")

elif lado1 == lado2:
  print(f"Como o primeiro lado e de:  {lado1}\n Como o segundo lado e de:  {lado2}\nComo o terceiro lado e de:  {lado3} ele e um Triângulo isóscele pois 2 lados sao iguais.")
  
elif lado2 == lado3:
  print(f"Como o primeiro lado e de:  {lado1}\nComo o segundo lado e de:  {lado2}\nComo o terceiro lado e de:  {lado3} ele e um Triângulo isóscele pois 2 lados sao iguais.")

elif lado1 == lado3:
  print(f"Como o primeiro lado e de:  {lado1}\nComo o segundo lado e de:  {lado2}\nComo o terceiro lado e de:  {lado3} ele e um Triângulo isóscele pois 2 lados sao iguais.")

else: 
  print(f"Como o primeiro lado e de:  {lado1}\nComo o segundo lado e de:  {lado2}\nComo o terceiro lado e de:  {lado3} ele e um Triângulo escaleno pois o 3 lados sao diferentes.")
