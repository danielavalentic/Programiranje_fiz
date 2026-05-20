import numpy as np

def volumen_valjka(R, L):
    return np.pi * R**2 * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * np.pi * R * L
    dV_dL = np.pi * R**2
    return np.sqrt((dV_dR * sigma_R)**2 + (dV_dL * sigma_L)**2)

def gustoca_valjka(m, V):
    return m / V

def sigma_gustoce(m, sigma_m, V, sigma_V):
    drho_dm = 1 / V
    drho_dV = -m / V**2
    return np.sqrt((drho_dm * sigma_m)**2 + (drho_dV * sigma_V)**2)

def relativna_pogreska(rho, rho_lit):
    return (np.abs(rho - rho_lit) / rho_lit) * 100

# gustoce nekih materijala
materijali = {
    "Aluminij":  2.70,
    "Titanij":   4.51,
    "Željezo":   7.87,
    "Nikal":     8.91,
    "Bakar":     8.96,
    "Cink":      7.13,
    "Olovo":    11.34,
}

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

mase_g = {
    "Valjak 1": [138.92, 138.98, 139.20, 138.90, 138.92],
    "Valjak 2": [128.65, 128.60, 128.65, 128.35, 128.50],
    "Valjak 3": [71.89, 71.90, 71.79, 71.85, 71.70],
}


for naziv in dijametri_mm:
    polumjeri_cm = [d / 2 / 10 for d in dijametri_mm[naziv]]
    duljine_cm = [l / 10 for l in duljine_mm[naziv]]
    masa_g_list = mase_g[naziv]

    n = len(polumjeri_cm)

    R_sr = np.mean(polumjeri_cm)
    L_sr = np.mean(duljine_cm)
    m_sr = np.mean(masa_g_list)

    sigma_R = np.std(polumjeri_cm, ddof=1) / np.sqrt(n)
    sigma_L = np.std(duljine_cm, ddof=1) / np.sqrt(n)
    sigma_m = np.std(masa_g_list, ddof=1) / np.sqrt(n)

    V = volumen_valjka(R_sr, L_sr)
    sV = sigma_volumena(R_sr, sigma_R, L_sr, sigma_L)

    rho = gustoca_valjka(m_sr, V)
    sRho = sigma_gustoce(m_sr, sigma_m, V, sV)

   
    najmanja_razlika = float('inf')
    materijal = ""
    rho_lit = 0

    for mat in materijali:
        razlika = abs(materijali[mat] - rho)
        if razlika < najmanja_razlika:
            najmanja_razlika = razlika
            materijal = mat
            rho_lit = materijali[mat]

    #rel pogreska
    delta_rho = relativna_pogreska(rho, rho_lit)

    
    print(f"{naziv} ({materijal}): gustoća = {rho:.2e} g/cm³, pogreška = {sRho:.2e} g/cm³; relativno odstupanje = {delta_rho:.2f}%")