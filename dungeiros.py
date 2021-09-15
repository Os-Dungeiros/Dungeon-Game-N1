
numeroSala = 1
escolhaCaminho = 0
cont = 0
print("\nOlá aventureiro!! :D\n")
print("--------------------------\nSala atual (inicial) : {}\n--------------------------".format(numeroSala))
while numeroSala != 9 and cont < 7:
    escolhaCaminho = int(input("Qual caminho você seguirá (se escolher algum diferente de 1 ou 2 será adicionado 1)?\n[1] Vermelho\n[2] Preto\nEscolha : "))
    
    print("----------------------\nSua sala atual é : {}\n----------------------\n".format(numeroSala))
    cont = cont + 1
