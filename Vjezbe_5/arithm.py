# A
import math

tocke = [10.2, 10.5, 9.8, 10.1, 10.3, 9.9, 10.0, 10.4, 10.2, 9.7]
n = len(tocke)

# 1.Formula
sredina = sum(tocke) / n

# 2.Formula
suma_kvadrata_razlika = 0
for x in tocke:
    razlika = x - sredina
    suma_kvadrata_razlika += razlika**2


nazivnik = n * (n - 1)


sigma = math.sqrt(suma_kvadrata_razlika / nazivnik)

print(f"Tocke: {tocke}")
print(f"Aritmeticka sredina (x_crtica): {sredina:.4f}")
print(f"Standardna devijacija (sigma): {sigma:.4f}")

'''--------------------------------------------------------'''

# B: 
import numpy as np

tocke_np = np.array(tocke)

#aritmeticka sredina
sredina_np = np.mean(tocke_np)

# standardna devijacija 
s_uzorka = np.std(tocke_np, ddof=1)


sigma_np = s_uzorka / np.sqrt(len(tocke_np))

print(f"Aritmetička sredina (NumPy): {sredina_np:.4f}")
print(f"Standardna devijacija (NumPy): {sigma_np:.4f}")