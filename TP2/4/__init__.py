import math
def escalar_calcula(vetores):
    #aqui calculo o escalar vetorial e retorno
    soma=0
    for x in range(len(vetores[0])):
        soma += vetores[0][x]*vetores[1][x]
    return soma
def calcula_versor(versores):
    x = 1/(((versores[0]**2)+(versores[1]**2)+(versores[2]**2))**(1/2))
    return ((versores[0]*x), (versores[1]*x), (versores[2]*x)),x

def angulo_bgl():
    print("Ângulo entre os vetores u e v:")
    msg = ["u", "v"]
    vetores = [[], []]

    dimensao = 3
    # Adiciono os dados dos vetores, no "vetores" 2 em 1

    for x in range(2):
        print("Coordenadas do vetor %s:" % msg[x])
        for y in range(dimensao):
            vetores[x].append(float(input("Digite a %da. coordenada: " % (y + 1))))

    versor, comprimento = (calcula_versor(versores=vetores[0]))
    versor, comprimento2 = (calcula_versor(versores=vetores[1]))

    Ev = escalar_calcula(vetores)
    Pv = (comprimento**-1*(comprimento2**-1))

    print("Ângulo: %.2f graus"%math.degrees( math.acos(Ev/Pv)))

def tenta():
    try:
        angulo_bgl()
    except:
        tenta()

tenta()
