import numpy as np

# Gravitacijska konstanta u jedinicama: AU, godina, masa Sunca
G = 4 * np.pi**2


class BinaryStar:
    def __init__(self, m1, m2, a, e):
        """
        
        m1, m2: mase zvijezda u masama Sunca (Msun)
        a: velika poluos u AU
        e: ekscentricitet 
        """
        self.m1 = m1
        self.m2 = m2
        self.a = a
        self.e = e

        r_peri = a * (1 - e)
        v_peri = np.sqrt(G * (m1 + m2) * (1 + e) / (a * (1 - e)))

        r1 = np.array([-m2 / (m1 + m2) * r_peri, 0.0])
        r2 = np.array([ m1 / (m1 + m2) * r_peri, 0.0])

        v1 = np.array([0.0, -m2 / (m1 + m2) * v_peri])
        v2 = np.array([0.0,  m1 / (m1 + m2) * v_peri])

        self.y0 = np.hstack([r1, r2, v1, v2])

    def deriv(self, y):
        
        r1 = y[0:2]
        r2 = y[2:4]
        v1 = y[4:6]
        v2 = y[6:8]

        dr = r2 - r1
        dist = np.linalg.norm(dr)

        a1 = G * self.m2 * dr / dist**3
        a2 = -G * self.m1 * dr / dist**3

        return np.hstack([v1, v2, a1, a2])

    def rk4_step(self, y, dt):
        
        k1 = self.deriv(y)
        k2 = self.deriv(y + 0.5 * dt * k1)
        k3 = self.deriv(y + 0.5 * dt * k2)
        k4 = self.deriv(y + dt * k3)
        return y + dt * (k1 + 2*k2 + 2*k3 + k4) / 6

    def simulate(self, T, dt):
        
        n = int(T / dt)
        y = self.y0.copy()
        traj = np.zeros((n, len(y)))

        for i in range(n):
            traj[i] = y
            y = self.rk4_step(y, dt)

        return traj