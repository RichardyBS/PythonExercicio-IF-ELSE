"""As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos 12. Escreve um programa que leia o número de maçãs compradas e calcule o valor total da compra. """

maca = 0.25

qtdCompra = int(input("Digite quantas macas deseja comprar: "))
totalPagar = maca * qtdCompra

if qtdCompra >= 12: 
  maca = 0.25
  print(f"O valor a ser pago e de:   {totalPagar}R$")

else:
  print(f"O valor a ser pago e de:   {totalPagar}R$")