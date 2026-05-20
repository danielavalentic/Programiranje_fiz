import math

# Formula 1:
def izracun_srednja(podaci):
    return sum(podaci) / len(podaci)

# Formula 2:
def izracun_sigma(podaci, srednja):
    n = len(podaci)
    suma_kvadrata = sum((x - srednja)**2 for x in podaci)
    return math.sqrt(suma_kvadrata / (n * (n - 1)))

# Tablica 1: R = d/2 
valjak1_R = [19.98/2, 20.18/2, 20.10/2, 20.08/2, 19.74/2]
valjak2_R = [19.92/2, 19.82/2, 19.96/2, 19.98/2, 19.88/2]
valjak3_R = [24.96/2, 24.98/2, 24.98/2, 24.92/2, 24.94/2]

# Tablica 2: Duljine L 
valjak1_L = [49.80, 49.00, 50.48, 49.80, 49.96]
valjak2_L = [52.56, 52.50, 52.62, 52.58, 52.54]
valjak3_L = [55.34, 55.40, 55.30, 55.44, 55.48]

# Tablica 3: Mase m 
valjak1_m = [138.92, 138.98, 139.20, 138.90, 138.92]
valjak2_m = [128.65, 128.60, 128.65, 128.35, 128.50]
valjak3_m = [71.89, 71.90, 71.79, 71.85, 71.70]

# Grupiranje podataka 
Podaci = [
    ("1", valjak1_R),
    ("2", valjak2_R),
    ("3", valjak3_R)
]


for broj, R_lista in Podaci:
    srednji_radijus = izracun_srednja(R_lista)
    standardna_devijacija = izracun_sigma(R_lista, srednji_radijus)
    
    print(f"Srednji radijus{broj} = {srednji_radijus:.2f}, standardna devijacija = {standardna_devijacija:.2f}")