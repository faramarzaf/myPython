import math

def calcFun2 (a,b,c):

    #fun = a*math.pow(x,2)+b*x+c
    delta = math.pow(b,2) - 4*a*c

    if delta > 0 :
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        roots = [x1 ,x2]
        print ('roots are: ',roots)
    if delta < 0 :
        print("eq has no roots")

    if delta == 0 :
        x3 = (-b)/2*a
        print ('root is: ',x3)

moadele = calcFun2(1,-8,1)
#[7.872983346207417, 0.12701665379258298]