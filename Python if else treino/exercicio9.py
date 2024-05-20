"""Escreva um programa que verifique se uma letra inserida pelo usuário é vogal ou consoante. """

consoante = 'b' , 'c' , 'd' , 'f' , 'g' , 'j' , 'k' , 'l' , 'm' , 'n' , 'p' , 'q' , 'r' , 's' , 't' , 'v' , 'w' , 'x' , 'z'

vogal = 'a' , 'e' , 'i' , 'o' , 'u'

letra = chr(input("Digite uma Letra, e irei dizer se ela e VOGAL ou CONSOANTE"))

if letra == consoante:
  print("e uma consoate")

elif letra == vogal:
  print("e uma vogal")

else:
  print("Desculpe nao consegui entender")