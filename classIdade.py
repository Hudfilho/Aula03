def idades():
  idade = int(input('Qual sua idade? '))
  
  if idade <= 10 :
    print('Voce eh uma CRIANÇA')
  elif idade >= 18:
    print('Voce eh um ADULTO ')
  else:
    print('Voce eh um ADOLESCENTE')