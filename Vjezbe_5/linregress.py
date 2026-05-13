import numpy as np
import matplotlib.pyplot as plt


M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
n = len(M)


brojnik = np.mean(phi * M)
nazivnik = np.mean(phi**2)
Dt = brojnik / nazivnik


srednja_vrijednost_y2 = np.mean(M**2)
izraz_u_zagradi = (srednja_vrijednost_y2 / nazivnik) - Dt**2
sigma_a = np.sqrt((1/n) * izraz_u_zagradi)


print(f"Modul torzije Dt = {Dt:.4f} Nm/rad")
print(f"Statisticka pogreska sigma_a = {sigma_a:.4f} Nm/rad")

print(f"Konacni rezultat: Dt = ({Dt:.3f} +/- {sigma_a:.3f}) Nm/rad")

# 5. Graf regresije
plt.figure(figsize=(8, 5))
plt.scatter(phi, M, color='red', label='Izmjerene tocke (M, phi)')
plt.plot(phi, Dt * phi, 'b-', label=f'Linearna regresija: M = {Dt:.3f} * phi')

plt.xlabel('$\phi$ [rad]')
plt.ylabel('$M$ [Nm]')
plt.title('Odredjivanje modula torzije aluminijske sipke')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()