# LOGICA
#
# para determinar se um ponto esta presente em um vetor
# é preciso fazer equacao simetrica do vetor, apos isso
# substituir os valores do ponto que quer saber se esta presente,
# na equacao, se os valores forem verdadeiros entao esta presente...
#
# EQ.SIMETRICA = (x-x0)/a == (y-y0)/b == (z-z0)/c  se TRUE esta na reta
#
# sendo a b c componentes do vetor
# e x0,y0,z0 o ponto de inicio do vetor
# x,y,z o ponto que deseja saber se esta na reta


# guardando os valores dos pontos ABC na cordenada

cordenada = []
print("Plano:")
for x in range(3):
    cordenada.append([])
    print("Coordenadas do ponto %s:" % ["A", "B", "C"][x])
    for y in range(3):
        cordenada[x].append(float(input("Digite a %da. coordenada: " % (y+1))))
# montando o vetor AB
AB = [(y - x) for x, y in zip(cordenada[0], cordenada[1])]
# Eq.simetrica
Eqsim = [(x-xo)/a  for a, x, xo in zip(AB, cordenada[2], cordenada[0])]
resposta = "O ponto C pertence a reta." if (Eqsim[0] == Eqsim[1] == Eqsim[2]) else "O ponto C não pertence a reta."
print(resposta)