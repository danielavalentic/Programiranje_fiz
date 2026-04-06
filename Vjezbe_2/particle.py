import numpy as np
import matplotlib.pyplot as plt





# Zadatak 1
class Particle:
    def __init__(self, v0, phi, x0, y0, dt=0.01):
        # Postavljamo početne vrijednosti. Važno je imati x0 i y0 zasebno zbog kasnijeg izračuna x(t) i y(t)
        self.v0 = v0

        # NumPy trigi-funkcije računaju pomoću radijana
        self.phi = np.radians(phi)

        self.x0 = x0
        self.x = x0

        self.y0 = y0
        self.y = y0

        self.t = 0
        self.dt = dt



    def reset(self):
        # Resetiramo apsolutno sve vrijednosti koje smo postavili
        self.v0 = None

        self.phi = None

        self.x0 = None
        self.x = None

        self.y0 = None
        self.y = None

        self.t = 0
        self.dt = None



    def __move(self):
        #Pomičemo vrijeme za dt, a zatim računamo idući x i y
        self.t += self.dt

        self.x = self.v0*np.cos(self.phi) *(self.t) + self.x0

        self.y = self.v0*np.sin(self.phi)*(self.t) - 0.5*9.81*self.t**2 + self.y0

    

    # 'range' je inače keyword Pythona, loša ideja!
    def range(self):
        # Prvo izračunamo analitički domet
        tRise = ( self.v0*np.sin(self.phi) ) / 9.81
        tFall = np.sqrt( (self.v0**2 * np.sin(self.phi)**2) / 9.81**2  +  (2*self.y0)/9.81 )
        tTotal = tRise + tFall
        
        D = self.v0*np.cos(self.phi)*tTotal + self.x0


        # Sada generiramo sve vrijednosti x-a za zadani dt pomak
        
        # Sačuvamo trenutno stanje 
        xCurr = self.x
        yCurr = self.y
        tCurr = self.t

        # Iskoristimo funkciju __move() da generiramo sve x-eve na putanji čestice
        xList = []
        for tim in np.arange(self.t, tTotal+self.dt, self.dt):
            xList.append(self.x)
            self.__move()

        # Vratimo vrijednosti x, y, t
        self.x = xCurr
        self.y = yCurr
        self.t = tCurr


        # Ispišemo rezultat
        print(f"Analitičkog rješenje je: {D}, dok je numeričko {xList[-1]} od numeričkog je: {(xList[-1]-D)}")

        # Ovako napisana klasa omogućava izračun razlike analitičkog i numeričkog rješenja za bilo koji set vrijednosti! :)
        return [xList[-1], D]



    def plot_trajectory(self):
        # Računamo vrijeme uspinjanja i padanja kako bismo izračunali ukupno vrijeme
        tRise = ( self.v0*np.sin(self.phi) ) / 9.81

        tFall = np.sqrt( (self.v0**2 * np.sin(self.phi)**2) / 9.81**2  +  (2*self.y0)/9.81 )

        tTotal = tRise + tFall


        # Sačuvamo trenutno stanje 
        xCurr = self.x
        yCurr = self.y
        tCurr = self.t


        # Izračunamo x(t) i y(t) za interval [tTrenutno, tTotal] pomoću privatne funckije __move()
        xList = []
        yList = []
        for tim in np.arange(self.t, tTotal, self.dt):
            xList.append(self.x)
            yList.append(self.y)
            self.__move()

        
        # Vratimo vrijednosti x, y, t
        self.x = xCurr
        self.y = yCurr
        self.t = tCurr


        # Plotiramo
        plt.plot(xList, yList)
        plt.show()




