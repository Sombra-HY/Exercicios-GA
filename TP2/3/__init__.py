def calcula_versor(versores):
    x = 1/(((versores[0]**2)+(versores[1]**2)+(versores[2]**2))**(1/2))
    return ((versores[0]*x), (versores[1]*x), (versores[2]*x)),x


def pega_versor():
    versor = []
    print("Cosseno Diretor:\nCoordenadas do vetor u:")
    for x in range(3):
        versor.append(float(input("Digite a %da. coordenada: "%(x+1))))
    Nversor, x = calcula_versor(versores=versor)
    print("Cosseno Diretor: 1/{0:.2f} ({1:.2f}, {2:.2f}, {3:.2f})".format(x**-1,*versor))
    print("Cosseno Diretor: ({0:.2f}, {1:.2f}, {2:.2f})".format(*Nversor))
pega_versor()