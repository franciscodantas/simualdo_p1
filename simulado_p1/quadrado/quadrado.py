import math

lado = float(input())

raio = (2*(lado/2)**2)**0.5
perimetro = 2*math.pi*raio
area = math.pi*raio**2

print(f'Perimetro: {perimetro:.5f}\nÁrea: {area:.5f}')
