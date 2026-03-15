import matplotlib.pyplot as plt
def jednadzba(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = y1 - k*x1
    return k,l

def crtanje_pravca(x1, y1,x2,y2):
    k,l = jednadzba(x1,y1,x2,y2)
    x = int(input('Unesi vrijednost x: '))
    y = k*x + l
    plt.scatter([x1,x2],[y1,y2], color='blue')
    raspon_x = [x1 - 2, x2 + 2]
    raspon_y = [k * x + l for x in raspon_x]
    plt.plot(raspon_x, raspon_y, color='yellow')
   
    plt.xlabel('x')
    plt.ylabel('y')
    ime=str(input('Unesi naziv: '))
    plt.title(ime)
    plt.grid(True)
    plt.show()
crtanje_pravca(1,2,8,4)
