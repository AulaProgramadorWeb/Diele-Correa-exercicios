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

#Ex 03: Fazer um programa onde o usuário vai digitar o valor atual do Dólar e
#Euro, Escolher qual opção de conversão ele deseja, e o valor para
#converter. Opções disponíveis: Euro para Dólar, Euro para Real, Dólar
#para Euro, Dólar para Real, Real para Euro e Real para Dólar. No final,
#perguntar para o usuário se ele deseja reiniciar o programa (se a
#resposta for sim, deve retornar ao início do programa)

euro = float(input("Qual o valor atual do EURO: "))
dolar = float(input("Qual o valor atual do DOLAR: "))
real = float(input("Qual o valor atual do REAL: "))
convert = float(input("Qual o valor para converter: "))

euro = convert * euro
dolar = convert * dolar
real = convert * real

print("valor em EURO: {}".format(euro), 
      "valor em DOLAR: {}".format(dolar), 
      "valor em REAL:{} ".format(real))
