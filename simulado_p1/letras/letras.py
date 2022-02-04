n = int(input())
dobradas = []
naodobradas = []
dobra = False
for i in range(n):
    palavra = input()

    for c in range(len(palavra)-1):
        if palavra[c] == palavra[c+1]:
            dobradas.append(palavra)
            dobra = True
            break
        else:
            dobra = False
    if dobra == False:
        naodobradas.append(palavra)

print(f'{len(dobradas)} palavra(s) com letras dobradas:')
for i in range(len(dobradas)):
    print(dobradas[i])
print('---')
print(f'{len(naodobradas)} palavra(s) sem letras dobradas:')
for i in range(len(naodobradas)):
    print(naodobradas[i])
