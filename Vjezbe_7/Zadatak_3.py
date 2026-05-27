import numpy as np

def medijan(podaci):
    
    sortirani = sorted(podaci)
    n = len(sortirani)

   
    if n % 2 == 1:
        return sortirani[n // 2]
    else:
        
        lijevi_srednji = n // 2 - 1
        desni_srednji = n // 2
        return (sortirani[lijevi_srednji] + sortirani[desni_srednji]) / 2


a = [3, 1, 4, 1, 5, 9, 2, 6] #paran n
b = [3, 1, 4, 1, 5, 9, 2, 6, 5] #neparan n

print("Primjer a:", medijan(a))
print("Numpy:", np.median(a))

print("Primjer b:", medijan(b))
print("Numpy:", np.median(b))


np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

moj_med = medijan(mase)

numpy_med = np.median(mase)

print("Medijan masa (funkcija) =", moj_med)
print("Medijan masa (numpy) =", numpy_med)