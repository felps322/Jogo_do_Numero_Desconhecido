import random

muito_baixo = "|xxxxx|-----|-----|-----|-----|"

baixo = "|-----|xxxxx|-----|-----|-----|"

medio = "|-----|-----|xxxxx|-----|-----|"

alto = "|-----|-----|-----|xxxxx|-----|"

muito_alto = "|-----|-----|-----|-----|xxxxx|"

def continuar():
    pergunta = input("Deseja continuar? ")

    afirmação = ["Sim", "sim", "SS", "Ss", "ss", "S", "s"]

    if pergunta in afirmação:
        inicio()
    
    else:
        return
    
def somar(valor):
    num = int(input("Quanto? "))
    valor += num
    return valor

def subtrair(valor):
    num = int(input("Quanto? "))
    valor -= num
    return valor

def valor_desconhecido():

    vidas = 10

    numeros = list(range(1, 300))

    valor_max = random.choice(numeros)

    valor_min = valor_max - random.choice(numeros)

    valores_possiveis = list(range(valor_min + 1, valor_max))

    valor = random.choice(valores_possiveis)

    intervalo = int((valor_max - valor_min) / 5)

    um_quinto = valor_min + intervalo

    dois_quintos = valor_min + (intervalo * 2)

    tres_quintos = valor_min + (intervalo * 3)

    quatro_quintos = valor_min + (intervalo * 4)


    while valor >= valor_min + 1 and valor <= valor_max - 1 and vidas >= 0:

        if valor <= um_quinto:
            print(f"{valor_min}{muito_baixo}{valor_max} Seu valor está muito baixo \n Você tem {vidas} vidas restantes")
        
        elif valor > um_quinto and valor <= dois_quintos:
            print(f"{valor_min}{baixo}{valor_max} Seu valor está baixo \n Você tem {vidas} vidas restantes")
        
        elif valor > dois_quintos and valor <= tres_quintos:
            print(f"{valor_min}{medio}{valor_max} Seu valor está na média \n Você tem {vidas} vidas restantes")
        
        elif valor > tres_quintos and valor <= quatro_quintos:
            print(f"{valor_min}{alto}{valor_max} Seu valor está alto \n Você tem {vidas} vidas restantes")
        
        elif valor > quatro_quintos:
            print(f"{valor_min}{muito_alto}{valor_max} Seu valor está muito alto \n Você tem {vidas} vidas restantes")

        pergunta = input("Somar ou Subtrair? ")

        if pergunta == "Somar":
            valor = somar(valor)
            vidas -= 1
        
        elif pergunta == "Subtrair":
            valor = subtrair(valor)
            vidas -= 1
        

    if valor < valor_min or valor > valor_max:
        print(f"Você Perdeu! \n  Seu valor: {valor} | Valor máximo: {valor_max}| Valor mínimo: {valor_min}")

    elif valor == valor_min:
        print(f"Você conseguiu o valor mínimo! Seu valor: {valor} | Valor mínimo: {valor_min}")

    elif valor == valor_max:
        print(f"Você conseguiu o valor máximo! Seu valor: {valor} | Valor máximo: {valor_max}")

    elif vidas < 0:
        print(f"As suas vidas acabaram! \n  Seu valor: {valor} | Valor máximo: {valor_max}| Valor mínimo: {valor_min}")
    
    continuar()



def limite_desconhecido():

    vidas = 10

    numeros = list(range(1, 300))

    valor_max = random.choice(numeros)
    
    valor_min = valor_max - random.choice(numeros)
    
    valores_possiveis = list(range(valor_min + 1, valor_max))

    valor = random.choice(valores_possiveis)

    intervalo = int((valor_max - valor_min) / 5)
    
    um_quinto = valor_min + intervalo
    
    dois_quintos = valor_min + (intervalo * 2)
    
    tres_quintos = valor_min + (intervalo * 3)
    
    quatro_quintos = valor_min + (intervalo * 4)


    while valor >= valor_min + 1 and valor <= valor_max - 1 and vidas >= 0:

        if valor <= um_quinto:
            print(f"{muito_baixo} {valor} está muito baixo \n Você tem {vidas} vidas restantes")
        
        elif valor > um_quinto and valor <= dois_quintos:
            print(f"{baixo} {valor} está baixo \n Você tem {vidas} vidas restantes")
        
        elif valor > dois_quintos and valor <= tres_quintos:
            print(f"{medio} {valor} está na média \n Você tem {vidas} vidas restantes")
        
        elif valor > tres_quintos and valor <= quatro_quintos:
            print(f"{alto} {valor} está alto \n Você tem {vidas} vidas restantes")
        
        elif valor > quatro_quintos:
            print(f"{muito_alto} {valor} está muito alto \n Você tem {vidas} vidas restantes")

        pergunta = input("Somar ou Subtrair? ")

        if pergunta == "Somar":
            valor = somar(valor)
            vidas -= 1
        
        elif pergunta == "Subtrair":
            valor = subtrair(valor)
            vidas -= 1

    if valor < valor_min or valor > valor_max:
        print(f"Você Perdeu! \n  Seu valor: {valor} | Valor máximo: {valor_max}| Valor mínimo: {valor_min}")

    elif valor == valor_min:
        print(f"Você conseguiu o valor mínimo! Seu valor: {valor} | Valor mínimo: {valor_min}")

    elif valor == valor_max:
        print(f"Você conseguiu o valor máximo! Seu valor: {valor} | Valor máximo: {valor_max}")
    
    elif vidas < 0:
        print(f"As suas vidas acabaram! \n  Seu valor: {valor} | Valor máximo: {valor_max}| Valor mínimo: {valor_min}")

    continuar()


def inicio():

    modo_de_jogo = int(input("Escolha um modo de jogo \n 1-Limite Desconhecido \n 2-Valor Desconhecido \n"))

    if modo_de_jogo == 1:
        limite_desconhecido()

    elif modo_de_jogo == 2:
        valor_desconhecido()


inicio()