# Uma equipe da Fórmula 1 deseja calcular o número mínimo de litros que deverá colocar no tanque de um de seus carros para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento. Escreva um programa (EM QUALQUER LINGUAGEM) que leia o comprimento da pista (em metros), o número total de voltas a serem percorridas no grande prêmio, o número de reabastecimentos desejados e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para percorrer até o primeiro reabastecimento. Considere que o número de voltas entre os reabastecimentos é o mesmo.

# 1 - Leia o comprimento da pista em metros
# 2 - Leia o numero total de voltas
# 3 - Leia quantas vezes o usuario quer parar para abastecer
# 4 - Leia o consumo de combustível do carro (em Km/L):

# 5 - Mostrar o numero minimo de litros necessarios para percorrer ate o primeiro reabastecimento

# Se a laneLenght tiver 4km 
# Se a totalLaps for 10
# Se stopCount 3
# Se o carSupplies for 2km

# laneLenght * totalLaps = 40km => Percurso total
# percurso total / stopCount = 13,3km => Quilometros por parada
# Quilometros por parada / carSupplies = 6,6l => Quantidade de combustivel minima a ser abastecida por parada

laneLenght = int(input("Qual o comprimento da pista(Em metros) ?: "))
totalLaps = int(input("Qual o numero total de voltas da corrida ?: "))
stopCount = int(input("Quantas vezes voce quer parar para abastecer ?: "))
carSupplies = float(input("Qual o consumo de combustível do carro(Km/L) ?: "))

def carSupplyCalc():
    totalLeght = laneLenght * totalLaps

    stopKilometers = totalLeght / stopCount

    minimumSupply = stopKilometers / carSupplies

    print("A quantidade minima de combustivel a ser abastecido em uma pista com {}m de comprimento em {} voltas é de {}l por parada({} paradas)."
        .format(laneLenght, totalLaps, round(minimumSupply / 1000, 1), round(totalLaps, 0)))

carSupplyCalc()