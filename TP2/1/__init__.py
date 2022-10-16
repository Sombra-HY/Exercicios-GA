def escalar_calcula(vetores):
    #aqui calculo o escalar vetorial e retorno
    soma=0
    for x in range(len(vetores[0])):
        soma += vetores[0][x]*vetores[1][x]
    return soma
def pede_produto_escalar():
    msg = ["u", "v"]
    vetores = [[], []]

    print("Produto Escalar: ")
    dimensao = int(input("Digite a dimensão dos vetores: "))
    #Adiciono os dados dos vetores, no "vetores" 2 em 1

    for x in range(2):
        print("Coordenadas do vetor %s:"%msg[x])
        for y in range(dimensao):
            vetores[x].append(float(input("Digite a %da. coordenada: " % (y+1))))
    print("Produto Escalar: %.2f"%escalar_calcula(vetores))

pede_produto_escalar()
