#Ex 1: Fazer uma calculadora de divisão com apenas 2 números, e
#testar se o número é válido (não é zero)

num = float(input("Diga um número: " ))
divisao = float(input("Dividido por: " ))


resultado = float 
resultado = num / divisao

if (resultado != 0):
    print("O resultado da divisãoi é: {}".format(resultado))
else:
     print("O resultado é inválido : ")

#Ex 2: Calcular o desconto do salário de um funcionário (11%),
#exibindo o valor ou o desconto máximo permitido (318,20R$) 

salario = float(input("Qual o salario do funcionario: "))
desconto = float(input("Qual a porcentagem de desconto:"))
desconto = desconto / 100
resultado = salario * desconto

if (resultado >= 318.20):
    print("O valor máximo do desconto permitido é R$ 318,20")
else:
   print("O valor do desconto é: R$ {} ".format(resultado))