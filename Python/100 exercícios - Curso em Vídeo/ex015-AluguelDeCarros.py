# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos Km você rodou: "))
dias = int(input("Qunatos dias você alugou: "))
contaTotal = (dias * 60) + (km * 0.15)

print(f"Sua conta total foi de R${contaTotal:.2f}")