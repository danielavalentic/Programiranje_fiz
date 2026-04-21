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

  def move(self):
    while self.y[-1] >= 0 :   #simuliramo let dok ne padne na tlo
    #trenutna brzina:
      v = math.sqrt(self.vx**2 + self.vy**2)

    #sila otpora zraka:
      Fo = 0.5 * self.rho * self.cd * self.A * v**2

    #akceleracija zbog Fo:
      ax = -(Fo/self.m) * (self.vx/v) #self.vx/v je kosinus kuta
      ay = -self.g - (Fo/ self.m) * (self.vy/v)

    #Eulerova metoda za promjenu brzine i trenutne pozicije za infinitezimalni pomak
      self.vx +=ax * self.dt   #Nova brzina = stara brzina + promjena brzine
      self.vy += ay * self.dt

      nov_x = self.x[-1] + self.vx * self.dt #Nova pozicija = stara pozicija + pomak
      nov_y = self.y[-1] + self.vy * self.dt

    #spremanje u listu nove koordinate
      self.x.append(nov_x)
      self.y.append(nov_y)



'''TEST ZA RAZLICITI dt'''

parametri = dict(x0 = 0, y0 = 0, v0 = 40, kut = 45, masa = 2, Cd = 0.5, rho = 1.2, povrsina = 0.01)

koraci = [0.5, 0.1, 0.05, 0.01, 0.001]

plt.figure(figsize = (12, 6))

for vremenski_korak in koraci:  #za svaki korak novi projektil
  p = Projectile(**parametri, dt=vremenski_korak) # ** je operator za "raspakirat" rijecnik --> uzima sve iz rijecnika i ubacuje u funkciju
  p.move()
  plt.plot(p.x, p.y)

plt.title("Usporedba putanja za razliciti dt")
plt.xlabel ("x [m]")
plt.ylabel ("y [m]")
plt.grid(True)
plt.show() #ne - fizikalno gibanje: plava boja na grafu! -->veliki dt
    
  
