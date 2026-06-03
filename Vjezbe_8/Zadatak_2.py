import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import g

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85], dtype=float)

T_120 = np.array([
    0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653,
    0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373,
    1.9100, 2.5460
])

T_240 = np.array([
    1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720,
    1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840,
    2.4473, 3.1573
])

theta = np.deg2rad(kut_deg)

def T_model(theta, l):
    return 2 * np.pi * np.sqrt(l / (g * np.cos(theta)))

par120, cov120 = curve_fit(T_model, theta, T_120, p0=[0.12], bounds=(0, np.inf))
par240, cov240 = curve_fit(T_model, theta, T_240, p0=[0.24], bounds=(0, np.inf))

l120 = par120[0]
l240 = par240[0]
dl120 = np.sqrt(cov120[0, 0])
dl240 = np.sqrt(cov240[0, 0])

L_nom_120 = 0.120
L_nom_240 = 0.240

rel120 = abs(l120 - L_nom_120) / L_nom_120 * 100
rel240 = abs(l240 - L_nom_240) / L_nom_240 * 100

print(f'Za slučaj od 120 mm dobiveno je l = {l120:.6f} ± {dl120:.6f} m.')
print(f'Relativna pogreška u odnosu na nominalnu duljinu iznosi {rel120:.2f} %.')

print(f'Za slučaj od 240 mm dobiveno je l = {l240:.6f} ± {dl240:.6f} m.')
print(f'Relativna pogreška u odnosu na nominalnu duljinu iznosi {rel240:.2f} %.')

theta_graf = np.linspace(0, np.deg2rad(85), 500)

T_teorija_120 = T_model(theta_graf, L_nom_120)
T_teorija_240 = T_model(theta_graf, L_nom_240)
T_fit_120 = T_model(theta_graf, l120)
T_fit_240 = T_model(theta_graf, l240)

plt.figure(figsize=(9, 6))

plt.scatter(kut_deg, T_120, color='tab:blue', label='Mjereno, 120 mm')
plt.scatter(kut_deg, T_240, color='tab:orange', label='Mjereno, 240 mm')

plt.plot(np.rad2deg(theta_graf), T_teorija_120, color='tab:blue', alpha=0.45, linewidth=2,
         label='Teorija, 120 mm')
plt.plot(np.rad2deg(theta_graf), T_teorija_240, color='tab:orange', alpha=0.45, linewidth=2,
         label='Teorija, 240 mm')

plt.plot(np.rad2deg(theta_graf), T_fit_120, '--', color='navy',
         label=f'Fit, l = {l120*1000:.2f} mm')
plt.plot(np.rad2deg(theta_graf), T_fit_240, '--', color='darkred',
         label=f'Fit, l = {l240*1000:.2f} mm')

plt.xlabel('Kut θ [°]')
plt.ylabel('Period T [s]')
plt.title('Ovisnost perioda fizikalnog njihala o kutu otklona')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()