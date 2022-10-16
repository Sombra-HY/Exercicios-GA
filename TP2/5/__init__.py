def proj_orto(vetores):

    vetesc = sum([z*y for z, y in zip(vetores[0], vetores[1])])
    Vsqr = sum([x*x for x in vetores[1]])
    res = [x*(vetesc/Vsqr)  for x in vetores[1]]

    print("Projeção Ortogonal: {:.2f}/{:.2f}({:.2f}, {:.2f}, {:.2f})".format(
        vetesc, Vsqr, vetores[1][0], vetores[1][1], vetores[1][2]),
        "\nProjeção Ortogonal: (%.2f, %.2f, %.2f)"%(res[0], res[1], res[2]))
def Get_vet():
    print("Projeção Ortogonal do vetor u sobre o vetor v:")
    msg = ["u", "v"]
    vetores = [[], []]

    dimensao = 3
    # Adiciono os dados dos vetores, no "vetores" 2 em 1

    for x in range(2):
        print("Coordenadas do vetor %s:" % msg[x])
        for y in range(dimensao):
            vetores[x].append(float(input("Digite a %da. coordenada: " % (y + 1))))
    proj_orto(vetores)

Get_vet()