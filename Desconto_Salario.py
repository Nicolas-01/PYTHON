def calcular_salario(salario1):
  if salario1 <= 2112:
    return salario1

  elif salario1 <= 2826.65:
    calc_desconto2 = salario1 * 7.5 / 100
    sub_irpf2 = calc_desconto2 - 158.40
    print(f'Valor do IRPF: R$ {sub_irpf2:.2f}')
    return sub_irpf2

  elif salario1 <= 3751.05:
    calc_desconto3 = salario1 * 15 / 100
    sub_irpf3 = calc_desconto3 - 370.40
    print(f'Valor do IRPF: R$ {sub_irpf3:.2f}')
    return sub_irpf3

  elif salario1 <= 4664.68:
    calc_desconto4 = salario1 * 25.5 / 100
    sub_irpf4 = calc_desconto4 - 651.73
    print(f'Valor do IRPF: R$ {sub_irpf4:.2f}')
    return sub_irpf4

  elif salario1 > 4664.68:
    calc_desconto5 = salario1 * 27.5 / 100
    sub_irpf5 = calc_desconto5 - 884.96
    print(f'Valor do IRPF: R$ {sub_irpf5:.2f}')
    return sub_irpf5

def main():
  for i in range(5):
    salario = float(input(f'\nInforme o {i+1}° salário: '))
    desconto = calcular_salario(salario)

    if salario > 0:
      if salario <= 2112:
        print(f'Salário após o desconto: R$ {desconto:.2f}')

      elif salario <= 2826.65:
        subtracao_salario2 = salario - desconto
        print(f'Salário após o desconto: R$ {subtracao_salario2:.2f}')

      elif salario <= 3751.05:
        subtracao_salario3 = salario - desconto
        print(f'Salário após o desconto: R$ {subtracao_salario3:.2f}')

      elif salario <= 4664.68:
        subtracao_salario4 = salario - desconto
        print(f'Salário após o desconto: R$ {subtracao_salario4:.2f}')

      elif salario > 4664.68:
        subtracao_salario5 = salario - desconto
        print(f'Salário após o desconto: R$ {subtracao_salario5:.2f}')

    else:
      print('\nSalário Inválido.')

main()