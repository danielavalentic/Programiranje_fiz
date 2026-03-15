import matplotlib.pyplot as plt

def jednoliko_gibanje(F,m):
    t = range(0, 11, 1)

    x = [(F/(2*m))*pow(time,2) for time in t]
    v =[(F/m)*time for time in t]
    a =[F/m for time in t]

# graf x - t:
    plt.subplot(3 ,1 ,1)
    plt.plot(t, x)
    plt.xlabel('t(s)')
    plt.ylabel('x(m)')

# graf v - t:
    plt.subplot(3, 1, 2)
    plt.plot(t, v)
    plt.xlabel('t(s)')
    plt.ylabel('v(m/s)')

# graf a - t:
    plt.subplot(3, 1, 3)
    plt.plot(t, a)
    plt.xlabel('t(s)')
    plt.ylabel('a(m/s^2)')

    plt.show()
