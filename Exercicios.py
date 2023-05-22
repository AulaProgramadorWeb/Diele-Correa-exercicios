#Ex1: Calcular a área de terreno (largura x altura)
largura = float(input("Diga qual é largura do terreno?: "))
altura = float(input("Diga qual é altura do terreno?: "))
resultado=float
resultado = largura * altura

print("A area do seu terreno é: ", resultado)

#Ex2: perguntar quantos pães franceses e quantos sonhos o cliente deseja comprar. 
# PÃO = 0,50 R$ e SONHO = 2,00 R$. (lembre-se de exibir o valor final.)
pao = float
sonho = float
valorTotal = float
valorpao= float
valorsonho = float

pao = 0.50
sonho = 2.0


qntpao = float(input("Quantos pães você quer? "))
valorpao = qntpao * pao
qntsonho = float(input("Quantos sonhos você quer? "))
valorsonho = qntsonho * sonho

valorTotal = valorpao + valorsonho

print("Valor total da sua compra é: ", valorTotal)

#Ex3: Calcular o valor da viagem de um cliente, de acordo com a 
# distância que ele vai andar, 
# o preço da gasolina (o cliente informa o valor) e 
# quanto o carro dele faz por litro

distancia = float(input("Qual a distancia que irá percorrer? "))
valorGasolina = float(input("Qual o valor da gasolina? "))
qntCarroFaz = float(input("Quanto seu carro faz por litro? "))

resultDivisao = float 
resultDivisao = distancia / qntCarroFaz

valorViagem = float 
valorViagem = resultDivisao * valorGasolina

print("Valor da sua viagem é: ", valorViagem )

#Ex4: Pedir ao usuário sua altura em centimetros e exibir em metros (conversão simples)

centimetro = float(input("Qual a sua altura em centrimetro? "))

metro =  float
metro = centimetro / 100

print("Convertido em metros você tem ", metro, " metros!")









