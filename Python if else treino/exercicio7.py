"""Escreva um programa que leia os 3 ângulos de um triângulo e escreva se ele é um ACUTÂNGILO, RETÂNGULO ou OBTUSÂNGULO. Sendo que: 

a. Triângulo retângulo: possui um ângulo reto. (igual a 90 graus); 

b. Triângulo obtusângulo possui um ângulo obtuso (maior que 90 graus); 

c. Triângulo escaleno possui ângulos agudo. (menor que 90 graus); """

angulo1 = float(input("Digite o primeiro ângulo do triângulo: "))
angulo2 = float(input("Digite o segundo ângulo do triângulo: "))
angulo3 = float(input("Digite o terceiro ângulo do triângulo: "))


if angulo1 + angulo2 + angulo3 != 180:
        print("Os ângulos fornecidos não formam um triângulo válido.")

elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("O triângulo é RETÂNGULO.")

elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("O triângulo é ACUTÂNGULO.")