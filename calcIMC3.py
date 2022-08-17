def atendes():
  numdpessoas = int(input('Informe o numero de pessoas a serem atendidas '))
  pacientes = []
  n=0
  
  while numdpessoas != 0:
    nome = input('Informe o nome do paciente: ')
    pacientes.append(nome)
    numdpessoas-=1
  for x in pacientes:
    peso = float(input(f'Ola {pacientes[n]}! Informe o seu peso em Kg: '))
    altura = float(input('Informe a sua altura em metros: '))
    imc= peso/(altura*altura)
    print(f'O IMC do paciente {pacientes[n]} é {imc}')
    n+=1
    if imc > 22:
      print('Imc alto')
    elif imc >= 20:
      print('Imc suave')
    else:
      print('Imc baixo')