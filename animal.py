def calcula_animas():
  n = int(input('Informe o numero de animais: '))
  velho = 0
  nome_velho = ' '
  
  while n != 0:
    nome = input('Informe o nome ')
    idade = int(input('Informe a idade '))
    if idade > velho:
      velho = idade
      nome_velho = nome
    n -= 1
  print(nome_velho)
      