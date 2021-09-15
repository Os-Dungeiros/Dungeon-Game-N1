    print("----------------------\nSua sala atual é : {}\n----------------------\n".format(numeroSala))
    cont = cont + 1
if(numeroSala == 9):
    print("Você venceu! Parabens por chegar na sala 9 !!!\n")
elif(cont >= 7):
    print("Você perdeu por excesso de jogadas!\n")
print("Total de jogadas : {}\n".format(cont)) 