def fibo(n):
    mylist  = [0, 1]


    z = 0
    y = 1

    d = 0


    while mylist[y]+mylist[z] <= n:
        

        a = mylist[z]
        b = mylist[y]

        d = a + b
        
        z= z+1
        y= y+1
        mylist.append(d)
    
    return mylist


def squaret(n):
    n = n ** 0.5
    #n = round(n, 2)
    return n

def quadr(a, b, c):
    
    n = ((b**2)-4*a*c)

    x1 = (-(b) + squaret(n) )/ (2*a)
    x2 = (-(b) - squaret(n) )/ (2*a)

    return x1,x2