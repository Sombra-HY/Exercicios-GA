# Equacao do plano é determinado, assim:
# dado os pontos A =(1,1,1) e vetores v =(2,2,2) u =(3,3,3),basta fazer a determinante:
#  |   AP   |   | x-1 y-1 z-1 |
#  |vetor u | = |  2   2   2  | = - 29x - 31y -5z -44 =0  = ax + by + cz +d = 0
#  |vetor v |   |  3   3   3  |

# se ele nao der os vetores, pode se criado com a utilizacao dos pontos
# por exemplo, é informado os pontos A B C, pode ser criado os vetores
# AB --> B-A e AC --> C-A
# apos isso fazendo o produto vetorial entre o AB e AC, encontramos um vetor ortogonal ao
# AB e ao AC = i + j + k com isso faltara apenas o elemento d que é feito substituindo
# um ponto no vetor encontrado


cordenada = []
# pegando os dados dos pontos
for x in range(3):

    cordenada.append([])                                  # adiciono para cada linha da matriz
    print("Coordenadas do ponto %s" % ["A", "B", "C"][x])     # Como a unica diferenca no print das cordenadas é "A B C", simplifico com uma lista em conjunto do for

    for y in range(3):
        cordenada[x].append(float(input("Digite a  %da.coordenada: " % (y+1))))   # aqui eu adiciono cada elemento da linha na matriz
determinante = [(cordenada[0][-3+y] * cordenada[1][-2+y] * cordenada[2][-1+y])-(cordenada[0][0+y] * cordenada[1][-1+y] * cordenada[2][-2+y]) for y in range(3)]

if(sum(determinante)==0): # verificacao se é LD, no caso se a determinante for 0 é LD, se nao é LI
    print("Dados incorretos!")
else:
    # criando os vetores
    u = [(y-x) for x, y in zip(cordenada[0], cordenada[1])] # criacao do vetor AB --> B-A
    v = [(y-x) for x, y in zip(cordenada[0], cordenada[2])] # criacao do vetor AC --> C-A
    matriz =[[1, 1, 1], u, v]

    produto_vetorial = [(matriz[0][-3+y] * matriz[1][-2+y] * matriz[2][-1+y])-
                        (matriz[0][0+y] * matriz[1][-1+y] * matriz[2][-2+y]) for y in range(3)] #produto vetorial de u e v
    print(""
          "ax + by + cz + d = 0",
          "onde:",
          "a = %.2f, b = %.2f, c = %.2f e d = %.2f"%
          (produto_vetorial[0], produto_vetorial[1], produto_vetorial[2], sum(determinante)),
          sep="\n")