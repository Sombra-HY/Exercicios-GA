# Equacao do plano é determinado, assim:
# dado os pontos A =(1,1,1) e vetores B =(2,2,2) C =(3,3,3), sendo P =(0,0,0) <-- vc msm considera isso,
# no caso e mais facil com 0
#  |   AP   |   | x-1 y-1 z-1 |
#  |vetor B | = |  2   2   2  | = - 29x - 31y -5z -44 =0
#  |vetor C |   |  3   3   3  |

pontos = ["A", "B", "C"]; cordenada=[]
for x in range(3):
    cordenada.append([])
    print("As cordenadas de %s" % pontos[x])
    for y in range(3):
        cordenada[x].append(float(input("Digite a cordenada %d.a: " % (y+1))))


for x in range(3):
    for y in range(-len(cordenada[0]), len(cordenada[0])):
        print(cordenada[x][y],end=" ")
    print("\n")
a = [(cordenada[0][-3+y] * cordenada[1][-2+y] * cordenada[2][-1+y])-() for y in range(3)]
print(a)