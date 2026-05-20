import numpy as np

def volumen_valjka(R, L):
    return np.pi * R**2 * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * np.pi * R * L
    dV_dL = np.pi * R**2
    return np.sqrt((dV_dR * sigma_R)**2 + (dV_dL * sigma_L)**2)

dijametri_mm = {
    "Valjak 1": [19.98, 20.18, 20.10, 20.08, 19.74],
    "Valjak 2": [19.92, 19.82, 19.96, 19.98, 19.88],
    "Valjak 3": [24.96, 24.98, 24.98, 24.92, 24.94],
}

duljine_mm = {
    "Valjak 1": [49.80, 49.00, 50.48, 49.80, 49.96],
    "Valjak 2": [52.56, 52.50, 52.62, 52.58, 52.54],
    "Valjak 3": [55.34, 55.40, 55.30, 55.44, 55.48],
}


for naziv in dijametri_mm:
    polumjeri_cm = [d / 2 / 10 for d in dijametri_mm[naziv]]
    duljine_cm = [l / 10 for l in duljine_mm[naziv]]

    R_srednji = np.mean(polumjeri_cm)
    L_srednja = np.mean(duljine_cm)

    n = len(polumjeri_cm)
    sigma_R = np.std(polumjeri_cm, ddof=1) / np.sqrt(n)

    sigma_L = np.std(duljine_cm, ddof=1) / np.sqrt(n)

    V = volumen_valjka(R_srednji, L_srednja)
    sigma_V = sigma_volumena(R_srednji, sigma_R, L_srednja, sigma_L)

    
    print(f"{naziv}: volumen = {V:.2e} cm³, pogreška = {sigma_V:.2e} cm³")