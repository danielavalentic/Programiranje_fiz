import matplotlib.pyplot as plt
from kinematika import jednoliko_gibanje as jg

#Korisnik unosi silu u N i masu u kg
F = float(input('Unesi iznos sile u N: '))
m = float(input('Unesi masu u kg: '))

#pozivamo funkciju
jg(F,m)