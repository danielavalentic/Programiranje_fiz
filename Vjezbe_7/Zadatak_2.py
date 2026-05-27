import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

x_min = min(mase_ciste)
x_max = max(mase_ciste)
k = 10
h = (x_max - x_min) / k
rubovi = [x_min + i * h for i in range(k + 1)]

sredina = np.mean(mase_ciste)
medijan = np.median(mase_ciste)

plt.figure(figsize=(8, 5))
plt.hist(mase_ciste, bins=rubovi, edgecolor="black", color="skyblue")

plt.axvline(sredina, linestyle="--", color="red",
            label=f"Aritmetička sredina = {sredina:.3f}")
plt.axvline(medijan, linestyle=":", color="magenta",
            label=f"Medijan = {medijan:.3f}")

plt.xlabel("Masa zvijezde Sirius A ($M_{\\odot}$)")
plt.ylabel("Frekvencija")
plt.title("Histogram mase Sirius A")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show() 

#za dodatne k isprobati
'''
for k in [8, 12]:
    plt.figure(figsize=(8, 5))
    plt.hist(mase_ciste, bins=k, edgecolor="black")
    plt.axvline(sredina, linestyle="--", color="red")
    plt.axvline(medijan, linestyle=":", color="magenta")
    plt.title(f"Histogram mase Sirius A, k = {k}")
    plt.show()'''