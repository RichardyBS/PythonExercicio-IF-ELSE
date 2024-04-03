"""Faça um programa que solicite a data de nascimento de uma pessoa e informe se ela pode votar ou não. """

dataNascimento = int(input("Digite sua o ano de seu Nascimento e Direi se voce pode votar em 2024:    "))

dataRestante = 2006 - dataNascimento

if dataNascimento <= 2006:
  dataRestante = 2006 % dataNascimento
  print(f"você tem:      {dataNascimento} anos\nlogo você pode votar pois a idade minima é de 18 anos.\nJa faz {dataRestante} anos, Que voce tem 18 :)")
else:
  print(f"sua idade e de {dataNascimento}\n logo voce nao pode votar ainda falta:    {dataRestante}anos")