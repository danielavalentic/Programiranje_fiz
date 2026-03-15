import matplotlib.pyplot as plt


#Unos korisnika:
F = float(input('Unesi vrijednost sile (N): '))
m = float(input('Unesi masu čestice (kg): '))

#raspon vremena od 0 do 10 sek: 
t = (0, 11, 1)

#vrijednosti položaja, brzine i akceleracije: 
x = [(F/(2*m))*pow(time,2) for time in t]
v =[(F/m)*time for time in t]
a =[F/m for time in t]

#stvaranje Plot s 3 retka i 1 stupcem: 1. redak (x - t graf):
plt.subplot(3,1,1)
plt.plot(t,x)
plt.xlabel('t(s)')
plt.ylabel('x(m)')

#2. redak (v - t graf):
plt.subplot(3, 1 , 2 )
plt.plot(t,v)
plt.ylabel('v(m/s)')
plt.xlabel('t(s)')

#3. redak (a - t graf):
plt.subplot(3, 1, 3)
plt.plot(t,a)
plt.xlabel('t(s)')
plt.ylabel('a(m/s^2)')

#prikaz grafova: 
plt.show()