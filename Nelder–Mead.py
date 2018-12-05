# -*- coding: utf-8 -*-
from math import cos,pi,exp,log;
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "({0}, {1}, {2})".format(self.x, self.y,self.z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vector(x, y, z)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vector(x, y, z)

    def c(self):
        return (self.x, self.y, self.z)
        
def f(point):
	x,y,z = point;
	res = exp((x**2)+(y**2))+log(4+(y**2)+2*(z**2));
	return res

def Andrii():
	x,y,z = point;
	res = exp(x^2+y^2)+log(4+y^2+2*z^2);
	return res

def func_Rastrigin(point):
	# Это функция Растрыгина для n = 2 func: R^n -> R;
	# Нужно подстроить под функцию n = 3;
	x,y = point
    a = 10
    rez = 2*a + x**2 - a*cos(2*(pi)*x) + y**2 - a*cos(2*(pi)*y);
    return rez

def nelder_mead(alpha=1, beta=0.5, gamma=2, maxiter=10):
    
    # Выбираю рандомные точки для симплекса ( звучит, как болезнь или секс-игрушка )

    v1 = Vector(0, 0, 0)
    v2 = Vector(1.0, 0, 1.0)
    v3 = Vector(0, 1.0, 1.0)

    for i in range(maxiter):
        adict = {v1:f(v1.c()), v2:f(v2.c()), v3:f(v3.c())}
        points = sorted(adict.items(), key=lambda x: x[1])
        
        b = points[0][0]
        g = points[1][0]
        w = points[2][0]
        
        
        mid = (g + b)/2

        # Отражение
        xr = mid + alpha * (mid - w)
        if f(xr.c()) < f(g.c()):
            w = xr
        else:
            if f(xr.c()) < f(w.c()):
                w = xr
            c = (w + mid)/2
            if f(c.c()) < f(w.c()):
                w = c
        if f(xr.c()) < f(b.c()):

            # Растяжка
            xe = mid + gamma * (xr - mid)
            if f(xe.c()) < f(xr.c()):
                w = xe
            else:
                w = xr
        if f(xr.c()) > f(g.c()):
            
            # Сжашка ( сжатие )
            xc = mid + beta * (w - mid)
            if f(xc.c()) < f(w.c()):
                w = xc

        # Обновляем точки
        v1 = w
        v2 = g
        v3 = b
    return b

print("Result of Nelder-Mead algorithm: ")
xk = nelder_mead()
print("Best poits is: %s"%(xk))
print(f(xk.c()))