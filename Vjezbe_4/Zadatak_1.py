import numpy as np
import matplotlib.pyplot as plt

def simuliraj_putanju(q, m, v0, r0, dt, koraci, E, B):
    v = np.array(v0, dtype=float).copy()
    r = np.array(r0, dtype=float).copy()
    E = np.array(E, dtype=float)
    B = np.array(B, dtype=float)

    putanja = [r.copy()]
    
    for _ in range(koraci):
        F = q * (E + np.cross(v, B))
        a = F / m
        v = v + a * dt
        r = r + v * dt
        putanja.append(r.copy())
    
    return np.array(putanja)

m = 1.0
dt = 0.01
t_max = 50
koraci = int(t_max / dt)

E = np.array([0.0, 0.0, 0.0])
B = np.array([0.0, 0.0, 1.0])

v_pocetna = np.array([2.0, 1.0, 0.2])
r_pocetni = np.array([0.0, 0.0, 0.0])

putanja_pozitron = simuliraj_putanju(1.0, m, v_pocetna, r_pocetni, dt, koraci, E, B)
putanja_elektron = simuliraj_putanju(-1.0, m, v_pocetna, r_pocetni, dt, koraci, E, B)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(putanja_pozitron[:, 0], putanja_pozitron[:, 1], putanja_pozitron[:, 2],
        label='Pozitron (+q)', color='red')

ax.plot(putanja_elektron[:, 0], putanja_elektron[:, 1], putanja_elektron[:, 2],
        label='Elektron (-q)', color='blue')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Elektron vs Pozitron u B polju')
ax.legend()
plt.show()