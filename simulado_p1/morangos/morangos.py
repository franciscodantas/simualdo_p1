morangos = int(input())

caixas = int(morangos/400)
resto = morangos%400
porcentagem = (100*resto)/morangos

print(f'{caixas} caixa(s) completa(s) para embalar os morangos.')
print(f'{porcentagem:.1f}% dos morangos serão perdidos.')
