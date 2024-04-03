"""Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é “123mudar”. Devem ser impressas as seguintes mensagens: 

a. ACESSO PERMITIDO. Caso a senha seja válida 

b. ACESSO NEGADO. Caso a senha seja inválida. """

senhaUsuario = "123mudar"

senhaDigitada = input("Digite a senha para entrar: ")
if senhaDigitada == senhaUsuario:
  print("ACESSO PERMITIDO.")
else:
  print("ACESSO NEGADO.")