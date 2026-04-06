import numpy as np
import matplotlib.pyplot as plt




# Zadatak 3
# Ovdje je pretpostavljeno da će korisnik proslijediti referencu na trigi-funkciju, ne njeno ime
# Također je pretpostavljeno da korisnik unosi polinom u obliku liste koeficijenata uz potencije (standard)
def derivPoint(funcy, point, e=0.0001):

    # Provjeravamo vrstu funkcije (trigi ili poli), a zatim računamo derivaciju i vrijednost u točki
    if isinstance(funcy, list):
        poly = np.poly1d(funcy)
        polyd = poly.deriv()
        print(f"Vrijednost derivacije u točki je: {polyd(point)}")
    
    else:
        # Pretvaramo korak i točku u radijane za ispravan rad derivacije
        eRad = np.radians(e)
        pointRad = np.radians(point)

        # Računamo derivaciju ispitujući neposredno okružje oko točke
        env = np.arange(pointRad-eRad, pointRad+eRad, eRad)
        trigd = np.gradient(funcy(env), eRad)
        print(f"Vrijednost derivacije u točki je: {trigd[0]}")
        




def derivInterval(funcy, a, b, e, method='three-step'):

    # Prvo provjeravamo vrstu funckije (poli ili trigi)
    # Računamo i vrijednosti derivacije funkcije u zadanim točkama jer moramo kasnije usporediti točnost modela
    if isinstance(funcy, list):
        xs = np.arange(a, b+e, e) # Formiramo sve točke
        print(f"Točke nad kojima se vrši derivacija su: {xs}") # Ispisujemo točke za koje tražimo derivaciju

        funcy = np.poly1d(funcy)
        funcyD = funcy.deriv() # Deriviramo funkciju
        funcyDvals = [funcyD(val) for val in xs] # Formiramo vrijednosti derivacije za točke


    else:
        # Pretvaramo sve u radijane za ispravan rad derivacije i provodimo
        a = np.radians(a)
        b = np.radians(b) 
        e = np.radians(e)

        xs = np.arange(a, b+e, e)
        print(f"Točke nad kojima se vrši derivacija su: {xs}") # Ispisujemo točke za koje tražimo derivaciju

        funcyDvals = np.gradient(funcy(xs), e)  # Formiramo vrijednosti derivacije za točke


    # Sada provjeravamo metodu
    # Formula za y je prilagođena sa https://en.wikipedia.org/wiki/Linear_multistep_method 
    if method == 'three-step':
        vals = [funcy(a), funcy(a+e), funcy(a+2*e)] # Trebaju y0, yn+1 i yn+2 da bi se našao yn+3
        
        for i in np.arange(a+3*e, b+e, e):
            y = vals[-1] - (0.5+2)*e*vals[-1] + (0.5+1)*e*vals[-2] - (0.5+0)*e*vals[-3] # Računamo idući y
        
            vals.append(y) # Postavljamo ga u listu da ga se može koristiti u idućem prolazu

    
    else:
        vals = [funcy(a), funcy(a+e)] # Trebaju y0 i yn+1 za yn+2
        
        for i in np.arange(a+2*e, b+e, e):
            y = vals[-1] + (0.5+1)*e*funcy(i-e) - (0.5+0)*e*funcy(i-2*e) # Računamo idući y
        
            vals.append(y) # Postavljamo ga u listu da ga se može koristiti u idućem prolazu


    # Plottamo prave vrijednosti derivacije naspram onih izračunatih two-step/three-step metodom
    plt.plot(xs, vals, label = 'Numerički izračun')
    plt.plot(xs, funcyDvals, label = 'Analitički izračun')
    plt.legend()
    plt.show()


        


# Zadatak 4
# Vrijede iste pretpostavke kao i u 3. zadatku
def integRect(funcy, a, b, n):
    dx = (a+b)/n

    # Postavljamo varijablu primeF tako da se ne moramo brinuti je li trigi ili poli funkcija
    if isinstance(funcy, list):
        primeF = np.poly1d(funcy)
    else:
        primeF = funcy


    # Stvaramo varijablu za donju među te ju računamo
    upper = 0

    for x in np.arange(a, b, dx):
        upper+=primeF(x+dx)*dx


    # Stvaramo varijablu za gornju među te ju računamo
    lower = 0

    for x in np.arange(a, b, dx):
        lower+=primeF(x)*dx


    # Vraćamo gornju i donju među
    print(f"Gornja međa je: {upper}, a donja {lower}")




def integTrap(funcy, a, b, n):
    dx = (a+b)/n

    # Postavljamo varijablu primeF tako da se ne moramo brinuti je li trigi ili poli funkcija
    if isinstance(funcy, list):
        primeF = np.poly1d(funcy)
    else:
        primeF = funcy

    # Računamo vrijednost integrala pomoću trapezne formule
    env = np.arange(a, b, dx)
    print(f"Površina je: {np.trapezoid(primeF(env), env, dx)}")