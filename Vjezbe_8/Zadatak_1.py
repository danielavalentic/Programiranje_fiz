import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54
m = 0.5257
r = 4.025e-3
g = 9.81

h = np.array([0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40])
t = np.array([1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813])

s = h

def linearna_regresija(x, y):
    n = len(x)
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxx = np.sum(x**2)
    Sxy = np.sum(x * y)

    a = (n * Sxy - Sx * Sy) / (n * Sxx - Sx**2)
    b = (Sy - a * Sx) / n

    y_fit = a * x + b
    rez = y - y_fit
    sigma_y = np.sqrt(np.sum(rez**2) / (n - 2))

    Sxx_c = np.sum((x - np.mean(x))**2)
    sigma_a = sigma_y / np.sqrt(Sxx_c)
    sigma_b = sigma_y * np.sqrt(1/n + np.mean(x)**2 / Sxx_c)

    return a, b, sigma_a, sigma_b, y_fit

x1 = np.log10(t)
y1 = np.log10(s)
a1, b1, da1, db1, y1_fit = linearna_regresija(x1, y1)

x2 = t**2
y2 = s
a2, b2, da2, db2, y2_fit = linearna_regresija(x2, y2)

a_ef = 2 * a2
da_ef = 2 * da2

Iz = m * r**2 * (g / a_ef - 1)
dIz_daef = -m * r**2 * g / (a_ef**2)
dIz = abs(dIz_daef) * da_ef

print("=== (a) log10(s) - log10(t) ===")
print(f"a = {a1:.6f} ± {da1:.6f}")
print(f"b = {b1:.6f} ± {db1:.6f}")

print("\n=== (b) s - t^2 ===")
print(f"a = {a2:.6f} ± {da2:.6f}")
print(f"b = {b2:.6f} ± {db2:.6f}")

print("\n=== (c) Izračun momenta tromosti ===")
print(f"a_ef = {a_ef:.6f} ± {da_ef:.6f} m/s^2")
print(f"Iz = {Iz:.6e} ± {dIz:.6e} kg m^2")

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].scatter(x1, y1, color="blue", label="Mjerenja")
x1_lin = np.linspace(np.min(x1), np.max(x1), 200)
ax[0].plot(x1_lin, a1 * x1_lin + b1, color="red", label="Linearni fit")
ax[0].set_xlabel(r'$\log_{10}(t)$')
ax[0].set_ylabel(r'$\log_{10}(s)$')
ax[0].set_title(r'Prikaz $\log_{10}(s)$ - $\log_{10}(t)$')
ax[0].grid(True)
ax[0].legend()

ax[1].scatter(x2, y2, color="blue", label="Mjerenja")
x2_lin = np.linspace(np.min(x2), np.max(x2), 200)
ax[1].plot(x2_lin, a2 * x2_lin + b2, color="red", label="Linearni fit")
ax[1].set_xlabel(r'$t^2\,[s^2]$')
ax[1].set_ylabel(r'$s\,[m]$')
ax[1].set_title(r'Prikaz $s - t^2$')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()