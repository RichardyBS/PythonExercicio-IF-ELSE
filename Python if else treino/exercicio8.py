"""Desenvolva um programa que receba o placar de um jogo de futebol, receba a quantidade de gols de cada time. Depois o programa deverá informar se foi empate, vitória do primeiro ou do segundo time. """
placar = int(input("Digite o Placar do jogo que voce viu: "))

qtdGolsT1 = int(input("Digite quanto o primeiro time marcou:  "))
qtdGolsT2 = int(input("Digite quanto o segunto time marcou: "))
difGols = placar - qtdGolsT1

confPlacar = qtdGolsT1 + qtdGolsT2
confPlacar == placar

if qtdGolsT2 > qtdGolsT1:
  difGols = placar - qtdGolsT1
  print(f"O time vencedor foi o Segundo time com um total de:   {qtdGolsT2}gols \nDando uma diferenca de {difGols}gols")

elif qtdGolsT2 < qtdGolsT1:
  difGols = placar - qtdGolsT2
  print(f"O time vencedor foi o Segundo time com um total de:   {qtdGolsT2}gols \nDando uma diferenca de {difGols}gols")

elif qtdGolsT2 == qtdGolsT1:
  print("deu empate")

else:
  print("Nao bate com a quantidade de Gols Digitada anteriormente")