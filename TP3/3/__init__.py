# para saber se uma base e positiva basta fazer a
# determinante dos vetores desta base se for maior que 0 é positiva


# Pegando os dados
cordenada = []
print("Bases Positivas e Bases Negativas")
for x in range(3):
    cordenada.append([])
    print("Coordenadas do vetor %s:" % ["u", "v", "w"][x])
    for y in range(3):
        cordenada[x].append(float(input("Digite a %da. coordenada: " % (y+1))))
# Fazendo a determinante
determinante = [(cordenada[0][-3 + y] * cordenada[1][-2 + y] * cordenada[2][-1 + y]) - (cordenada[0][0 + y] * cordenada[1][-1 + y] * cordenada[2][-2 + y]) for y in range(3)]
print("Base Positiva." if (sum(determinante)>=0) else "Base Negativa.")