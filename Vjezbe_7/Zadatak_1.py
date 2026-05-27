import matplotlib.pyplot as plt
import numpy as np


np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()



def histogram(podaci, k):
    x_min = min(podaci)
    x_max = max(podaci)

    
    h = (x_max - x_min) / k

   
    rubovi = [x_min + i * h for i in range(k + 1)]

    
    brojaci = [0] * k

   
    for x in podaci:
        for i in range(k):
            donji_rub = rubovi[i]
            gornji_rub = rubovi[i + 1]

            if i < k - 1:
                if donji_rub <= x < gornji_rub:
                    brojaci[i] += 1
                    break
            else:
                
                if donji_rub <= x <= gornji_rub:
                    brojaci[i] += 1
                    break

   
    print("Histogram (tekst prikaz):")
    for i in range(k):
        lijeva = rubovi[i]
        desna = rubovi[i + 1]
        zatvaranje = "]" if i == k - 1 else ")"
        print(f"[{lijeva:.2f}, {desna:.2f}{zatvaranje} - {brojaci[i]}")

    return brojaci, rubovi



brojaci, rubovi = histogram(mase_ciste, k=10)

h = rubovi[1] - rubovi[0]
sredine_razreda = [(rubovi[i] + rubovi[i + 1]) / 2 for i in range(len(brojaci))]

plt.figure(figsize=(8, 5))
plt.bar(sredine_razreda, brojaci, width=h, edgecolor="black", color="skyblue")

plt.xlabel("Masa zvijezde Sirius A ($M_{\\odot}$)")
plt.ylabel("Frekvencija")
plt.title("Histogram mjerenja mase zvijezde Sirius A")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()