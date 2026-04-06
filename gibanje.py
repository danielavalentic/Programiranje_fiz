from particle import Particle as ptcl
import matplotlib.pyplot as plt
import numpy as np


# Zadatak 1
pat1 = ptcl(10, 30, 1, 2, 0.001)

pat1.plot_trajectory()
pat1.range()




# Zadatak 2

# Za drugi zadatak uzet ćemo najjednostavniji slučaj - kosi hitac iz (0, 0)
# Provrtiti ćemo petlju i zabilježiti odstupanje (jer to možemo pomoću funkcije range()!), uz dt naravno. 
v0 = 10
phi = 60
x0 = 0
y0 = 0


# Recimo da uzimamo ovaj set vrijednosti (np.arange stvara raspon [početak, kraj> sa korakom k)
mistake = []
dts = []
for dt in np.arange(0.001, 0.1, 0.001):
    pat2 = ptcl(v0, phi, x0, y0, dt) # Stvaramo novu česticu

    numAn = pat2.range()

    mistake.append( (numAn[0]-numAn[1]) / numAn[0] ) # Odstupanje stavljamo u listu
    dts.append(dt) # Korak dt stavljamo u listu


# Sada plotiramo
# Pritom je važno napomenuti da 'width' parametar funckije bar() mora biti jednak koraku for-petlje
# jer će tako svi stupci zauzeti jednako mjesta, bez preklapanja.
# Ovo ujedno radimo preko for-petlje, a ne jednom crtom, tako da svaki stupac ima svoju boju :)
for i in range(len(mistake)):
    plt.bar(dts[i], mistake[i], width=0.001)
plt.show()


