while True:
    try:
        x1=float(input('Unesi koordinatu: '))
        y1=float(input('Unesi koordinatu: '))
        x2=float(input('Unesi koordinatu: '))
        y2=float(input('Unesi koordinatu: '))
        if x1==x2 and y1==y2:
            print('Pazi! Za pravac trebaju dvije točke!')
            continue #vraćamo se na vrh
        break #sve dobro; ide dalje
    except:
        print('Upiši broj!')


#horizontalni pravac: 
if y1 == y2:
    print(f'y = {y1}')

#vertikalni pravac: 
elif x1 == x2:
    print(f'x = {x1}')



else:
    k =(y2 - y1) / (x2 - x1)
    l = y1 - k*x1
    print(f'y = {k}x + {l}' )