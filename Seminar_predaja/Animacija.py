import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Programiranje_fiz.Seminar_predaja.Binarne import BinaryStar

# Stvarni astronomski podaci za Sirius A-B (izvor: https://enciklopedija.hr/clanak/sirius-astronomija)
m1 = 2.02     # Sirius A
m2 = 1.00     # Sirius B
a = 19.8      # velika poluos u AU
e = 0.59      # ekscentricitet

system = BinaryStar(m1, m2, a, e)
traj = system.simulate(T=80, dt=0.02)

r1 = traj[:, 0:2]
r2 = traj[:, 2:4]

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_aspect('equal')

ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_xlabel('x [AU]')
ax.set_ylabel('y [AU]')
ax.set_title('Simulacija gibanja: Sirius A-B')

ax.plot(0, 0, 'kx', label='Centar mase (barycenter)')

line1, = ax.plot([], [], 'gold', lw=1, alpha=0.6)
line2, = ax.plot([], [], 'lightblue', lw=1, alpha=0.6)
star1, = ax.plot([], [], 'o', color='gold', markersize=10, label='Sirius A')
star2, = ax.plot([], [], 'o', color='lightblue', markersize=8, label='Sirius B')
ax.legend(loc='upper right')

korak_prikaza = 5
indeksi_frameova = np.arange(0, len(r1), korak_prikaza)

def update(frame):
    line1.set_data(r1[:frame, 0], r1[:frame, 1])
    line2.set_data(r2[:frame, 0], r2[:frame, 1])

    star1.set_data([r1[frame, 0]], [r1[frame, 1]])
    star2.set_data([r2[frame, 0]], [r2[frame, 1]])

    return line1, line2, star1, star2

ani = FuncAnimation(fig, update, frames=indeksi_frameova, interval=10, blit=True)


plt.show()