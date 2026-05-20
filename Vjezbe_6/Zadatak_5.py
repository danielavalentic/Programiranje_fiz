import numpy as np


def izracunaj_sigma_n(podaci):
   
    srednja = np.mean(podaci)
    n = len(podaci)
    suma_kvadrata = sum((x - srednja)**2 for x in podaci)
    return np.sqrt(suma_kvadrata / n)

def izracunaj_s(podaci):
    
    srednja = np.mean(podaci)
    n = len(podaci)
    suma_kvadrata = sum((x - srednja)**2 for x in podaci)
    return np.sqrt(suma_kvadrata / (n - 1))

def izracunaj_sigma_x_crta(s_vrijednost, podaci):
    
    n = len(podaci)
    return s_vrijednost / np.sqrt(n)




#5 mjerenja temperatura vrenja vode
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

#10000 mjerenja istog eksperimenta
np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()


# za mali skup podataka
sigma_n_mali = izracunaj_sigma_n(malo_n)
s_mali = izracunaj_s(malo_n)
sigma_x_mali = izracunaj_sigma_x_crta(s_mali, malo_n)
# Relativna razlika izmedju sigma_n i s 
rel_razlika_mali = (abs(sigma_n_mali - s_mali) / s_mali) * 100

#za veliki skup podataka
sigma_n_veliki = izracunaj_sigma_n(veliko_n)
s_veliki = izracunaj_s(veliko_n)
sigma_x_veliki = izracunaj_sigma_x_crta(s_veliki, veliko_n)
# Relativna razlika izmedju sigma_n i s 
rel_razlika_veliki = (abs(sigma_n_veliki - s_veliki) / s_veliki) * 100




print("MALI SKUP (n = 5):")
print(f"sigma_n = {sigma_n_mali:.4f}")
print(f"s = {s_mali:.4f}")
print(f"sigma_x_crta = {sigma_x_mali:.4f}")
print(f"Relativna razlika (sigma_n i s) = {rel_razlika_mali:.2f}%")

print("\nVELIKI SKUP (n = 10000):")
print(f"sigma_n = {sigma_n_veliki:.4f}")
print(f"s = {s_veliki:.4f}")
print(f"sigma_x_crta = {sigma_x_veliki:.4f}")
print(f"Relativna razlika (sigma_n i s) = {rel_razlika_veliki:.4f}%")