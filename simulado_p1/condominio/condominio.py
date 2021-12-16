ruido = input()
horario = int()

if ruido != "":
    if horario > 22 or horario < 6:
        status = "Perturbação Detectada!"
else:
    status = "Condomínio em Paz."

print(status)
