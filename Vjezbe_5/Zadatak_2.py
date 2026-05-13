def izracunaj_pogresku(N):
    broj = 5.0
    trecina = 1/3

    for _ in range(N):
        broj += trecina
    for _ in range(N):
        broj -= trecina

    return broj

testne_vrijednosti = [200, 2000, 20000]

for n in testne_vrijednosti:
    print(f"{n}\t{izracunaj_pogresku(n)}")