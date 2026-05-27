import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)


mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]


sredina_sve = np.mean(mase)
medijan_sve = np.median(mase)


print("Srednja vrijednost (sve) = ", sredina_sve)
print("Medijan (sve) = ", medijan_sve)
print("Razlika = ", abs(sredina_sve - medijan_sve))




mase_bez = []


for x in mase:
    if 1.8 <= x <= 2.3:
        mase_bez.append(x)


sredina_bez = np.mean(mase_bez)
medijan_bez = np.median(mase_bez)


print("Srednja vrijednost (bez pogrešaka) = ", sredina_bez)
print("Medijan (bez pogrešaka) = ", medijan_bez)





print("Promjena srednje vrijednosti = ", abs(sredina_sve - sredina_bez))
print("Promjena medijana = ", abs(medijan_sve - medijan_bez))






plt.hist(mase, bins=15, edgecolor='black', alpha=0.7, color='steelblue')


plt.axvline(sredina_sve, color="red", linestyle='--', lw=2.5, label="Sredina (sve)")
plt.axvline(medijan_sve, color="darkgreen", linestyle=':', lw=4, label="Medijan (sve)")


plt.axvline(sredina_bez, color="cyan", linestyle='-', lw=2, label="Sredina (bez pogrešaka)")
plt.axvline(medijan_bez, color="orange", linestyle='-.', lw=1.5, label="Medijan (bez pogrešaka)")

plt.xlabel("Masa zvijezde")
plt.ylabel("Frekvencija")
plt.title("Histogram mjerenja mase Sirius A")
plt.legend()

plt.show()