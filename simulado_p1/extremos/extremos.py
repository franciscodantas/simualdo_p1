lista = []
maior = False
quantidade = int(input())
abaixo = 0
acima = 0

for x in range(quantidade):
    maior = False

    n = int(input())

    if x > 0 :
        for y in range( len(lista) ):
            if  n <= lista[y] :
                lista.insert( y, n )
                maior = True
                break
    if x == 0 or maior == False:
        lista.append( n )

for i in range(quantidade):
    if lista[i] > 1:
        minimo = lista[i]
        break

media = lista[-1]/minimo
for i in range(len(lista)):
    if lista[i] > media:
        acima += 1
    elif lista[i] < media:
        abaixo += 1

print(f'Menor número: {lista[0]}')
print(f'Maior número: {lista[-1]}')
print(f'Média dos extremos: {media:.2f}')
print(f'{abaixo} número(s) abaixo da média')
print(f'{acima} número(s) acima da média')

