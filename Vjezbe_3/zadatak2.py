#Runge_Kutta metoda 4. reda:
import matplotlib.pyplot as plt
import math

class Projectile:
  def __init__(self, x0, y0, v0, kut, masa, Cd, rho, povrsina, dt):

    self.x = [x0]
    self.y = [y0]

    rad = math.radians(kut)
    self.vx = v0 * math.cos(rad)
    self.vy = v0 * math.sin(rad)

    self.m = masa
    self.cd = Cd
    self.rho = rho
    self.A = povrsina
    self.dt = dt
    self.g = 9.81

  def move_rk4(self):
    def acceleration(vx, vy): #pomocna funkcija unutar metode da ne moram pisati formulu 4 puta
        v = math.sqrt(vx**2 + vy**2)
        if v == 0:
            return 0, -self.g
        fo = 0.5 * self.rho * self.cd * self.A * v**2
        drag = fo / self.m / v #trik za izbjegnut kosinus i sinus (drag - akceleracija po jed. brzine)
        return -drag * vx, -self.g - drag * vy #komponente akceleracije -->mnozenje s vx i vy ce automatski rijesit trigonometriju

    while self.y[-1] >= 0:
        dt = self.dt

        ax1, ay1 = acceleration(self.vx, self.vy)  #Trenutna akceleracija na pocetku intervala
        ax2, ay2 = acceleration(self.vx + ax1*dt/2, self.vy + ay1*dt/2) #Procjena akceleracije na polovici intervala (dt/2), koristeci nagib iz prvog koraka
        ax3, ay3 = acceleration(self.vx + ax2*dt/2, self.vy + ay2*dt/2) #analogno gornjoj,ali koristeci iz 2. koraka
        ax4, ay4 = acceleration(self.vx + ax3*dt,   self.vy + ay3*dt)   #Procjena na kraju intervala (dt), koristeci nagib iz treceg koraka

        self.vx += (dt/6) * (ax1 + 2*ax2 + 2*ax3 + ax4)
        self.vy += (dt/6) * (ay1 + 2*ay2 + 2*ay3 + ay4)

        self.x.append(self.x[-1] + self.vx * dt)
        self.y.append(self.y[-1] + self.vy * dt)


import matplotlib.pyplot as plt

p = Projectile( x0=0, y0=0,  v0=50, kut=45,masa=1.0, Cd=0.47,rho=1.2, povrsina=0.01, dt=0.01)


p.move_rk4()

plt.plot(p.x, p.y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Putanja projektila (RK4)")
plt.grid(True)
plt.show()


# 2. dio zadatka (usporedba):
import matplotlib.pyplot as plt
import math

class Projectile:
    def __init__(self, x0, y0, v0, kut, masa, Cd, rho, povrsina, dt):
        self.x0, self.y0 = x0, y0
        self.v0, self.kut = v0, kut
        self.m = masa
        self.cd = Cd
        self.rho = rho
        self.A = povrsina
        self.dt = dt
        self.g = 9.81
        self._reset()

    def _reset(self):
        self.x = [self.x0] #vracanje na pocetnu poziciju svaki put kad se pokrene
        self.y = [self.y0]
        rad = math.radians(self.kut)
        self.vx = self.v0 * math.cos(rad)
        self.vy = self.v0 * math.sin(rad)

    def move_euler(self):
        self._reset()
        while self.y[-1] >= 0:
            v = math.sqrt(self.vx**2 + self.vy**2)
            Fo = 0.5 * self.rho * self.cd * self.A * v**2
            ax = -(Fo/self.m) * (self.vx/v)
            ay = -self.g - (Fo/self.m) * (self.vy/v)
            self.vx += ax * self.dt
            self.vy += ay * self.dt
            self.x.append(self.x[-1] + self.vx * self.dt)
            self.y.append(self.y[-1] + self.vy * self.dt)

    def move_rk4(self):
        self._reset()
        def acceleration(vx, vy):
            v = math.sqrt(vx**2 + vy**2)
            if v == 0:
                return 0, -self.g
            fo = 0.5 * self.rho * self.cd * self.A * v**2
            drag = fo / self.m / v
            return -drag * vx, -self.g - drag * vy

        while self.y[-1] >= 0:
            dt = self.dt
            ax1, ay1 = acceleration(self.vx, self.vy)
            ax2, ay2 = acceleration(self.vx + ax1*dt/2, self.vy + ay1*dt/2)
            ax3, ay3 = acceleration(self.vx + ax2*dt/2, self.vy + ay2*dt/2)
            ax4, ay4 = acceleration(self.vx + ax3*dt,   self.vy + ay3*dt)
            self.vx += (dt/6) * (ax1 + 2*ax2 + 2*ax3 + ax4)
            self.vy += (dt/6) * (ay1 + 2*ay2 + 2*ay3 + ay4)
            self.x.append(self.x[-1] + self.vx * dt)
            self.y.append(self.y[-1] + self.vy * dt)


# --- Usporedba ---
p = Projectile(x0=0, y0=0, v0=50, kut=45, masa=1.0, Cd=0.47, rho=1.2, povrsina=0.01, dt=0.01)

p.move_euler()
x_euler, y_euler = p.x[:], p.y[:] #p.x[:] --> stvara kopiju liste, inace bi promjena u objektu izbrisala podatke iz prve varijable

p.move_rk4()
x_rk4, y_rk4 = p.x[:], p.y[:]

plt.plot(x_euler, y_euler, label="Euler", linestyle="--")
plt.plot(x_rk4,   y_rk4,   label="RK4")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Usporedba Euler vs RK4 (dt=0.01)")
plt.legend()
plt.grid(True)
plt.show()