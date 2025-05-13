print('................................\n')
print('Programa para Cálculos')
print('\n................................')

def soma(num1, num2):
  print('A soma é:',num1 + num2)

def subtracao(num1, num2):
  print('A subtração é:',num1 - num2)

def multiplicacao(num1, num2):
  print('A multiplicação é:',num1 * num2)

def divisao(num1, num2):
  print('A divisão é:',num1 / num2)

def potencia(num1, num2):
  print('A potência é:',num1 ** num2)

def raiz(num1, num2):
  print('A raíz é:',num1 ** (1 / num2))

def sair():
  print('\n................................\n')
  print('Calculadora Encerrada !!!')
  print('\n................................')

def main():
  escolha = int(input('\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potência \n6 - Raíz \n7 - Sair \nDigite um número: '))

  while escolha >= 1 and escolha <= 6:
    numero1 = float(input('\nInforme o 1° número: '))
    numero2 = float(input('Informe o 2° número: '))

    if escolha == 1:
      soma(numero1, numero2)

    elif escolha == 2:
      subtracao(numero1, numero2)

    elif escolha == 3:
      multiplicacao(numero1, numero2)

    elif escolha == 4:
      divisao(numero1, numero2)

    elif escolha == 5:
      potencia(numero1, numero2)

    elif escolha == 6:
      raiz(numero1, numero2)

    escolha = int(input('\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potência \n6 - Raíz \n7 - Sair \nDigite um número: '))

  if escolha < 1 or escolha >= 7:
    sair()

main()