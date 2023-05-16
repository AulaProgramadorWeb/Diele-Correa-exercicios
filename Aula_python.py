#tipos de vártiaveis
#int/float/str/ 
#comando: print()

#Comandos escreva e leia:
'''idade = int (input("Diga qual sua idade: "))
idade = idade + 5
print("sua idade será em cinco anos: ", idade)'''


'''
Ex1: Calcular a área de terreno (largura x altura)
Ex2: perguntar quantos pães franceses e quantos sonhos o cliente deseja comprar. PÃO = 0,50 R$ e SONHO = 2,00 R$. (lembre-se de exibir o valor final.)
Ex3: Calcular o valor da viagem de um cliente, de acordo com a distância que ele vai andar, o preço da gasolina (o cliente informa o valor) e quanto o carro dele faz por litro
Ex4: Pedir ao usuário sua altura em centimetros e exibir em metros (conversão simples)
Ex5: Pedir ao usuário o valor de sua compra, e aplicar um desconto de 15%
'''
#Ex2: perguntar quantos pães franceses e quantos sonhos o cliente deseja comprar. PÃO = 0,50 R$ e SONHO = 2,00 R$. (lembre-se de exibir o valor final.)
pao = float
sonho = float
valorTotal = float
valorpao= float
valorsonho = float

pao = 0.50
sonho = 2.0


qntpao = float(input("quantos pães você quer? "))
valorpao = qntpao * pao
qntsonho = float(input("quantos sonhos você quer? "))
valorsonho = qntsonho * sonho

valorTotal = valorpao + valorsonho

print("valor total da sua compra é: ", valorTotal)




