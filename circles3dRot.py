"""
Rotación 3D
"""

import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians #o usar la que ya trae numpy
# Importar las funciones que se definieron en el archivo tools3d
import tools3d as tools 

plt. axis([0,150,100,0])
plt.axis('on')
plt.grid(True)

x = []
y = []
z = []

xg = []
yg = []
zg = []

phi1 = radians(0)
phi2 = radians(360)
dphi = radians(5) # Representa la distancia entre punto y punto

r=10 # radio del circulo


for phi in np.arange(phi1, phi2+dphi, dphi): # Establecemos las coordenadas de los puntos de circulo
    xp = r*cos(phi)
    yp = r*sin(phi)
    zp = 0

    x.append(xp)
    y.append(yp)
    z.append(zp)

    xg.append(xp)
    yg.append(yp)
    zg.append(zp) 

#___________________ Definir la funcion para plotear el circulo
def plotCircle(xg,yg,zg):
    lastxg = xg[0]
    lastyg = yg[0]

    for i in range(len(x)):
        if i < len(x)/2:
            plt.plot([lastxg, xg[i]],[lastyg, yg[i]], linewidth=1, color='g')
        else:
            plt.plot([lastxg, xg[i]],[lastyg, yg[i]], linewidth=1, color='r')
        lastxg = xg[i]
        lastyg = yg[i]

        plt.scatter(xc, yc, s=5) # Plotear el centro dle circulo

# Aplicar las transformacion a las coordenadas y plotear
def plotCirclex(xc, yc, zc, Rx): # Calcular los puntos de rotacion y plotear el circulo
    for i in range(len(y)):
        [xg[i], yg[i], zg[i]] = tools.rotRx(xc, yc, zc, x[i], y[i], z[i], Rx)
        [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
    plotCircle(xg, yg, zg)

def plotCircley(xc, yc, zc, Ry): # Calcular los puntos de rotacion y plotear el circulo
    for i in range(len(y)):
        [xg[i], yg[i], zg[i]] = tools.rotRy(xc, yc, zc, x[i], y[i], z[i], Ry)
        [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
    plotCircle(xg, yg, zg)

def plotCirclez(xc, yc, zc, Rz): # Calcular los puntos de rotacion y plotear el circulo
    for i in range(len(y)):
        [xg[i], yg[i], zg[i]] = tools.rotRz(xc, yc, zc, x[i], y[i], z[i], Rz)
        [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
    plotCircle(xg, yg, zg)

#___________________ Plotear circulo a 
Rx = radians(0)
xc = 25
yc = 40
zc = 20
plotCirclex(xc, yc, zc, Rx)
plt.text(18, 60, "Gira 0°")

#___________________ Plotear circulo b 
Rx = radians(45)
xc = 55
yc = 40
zc = 20
plotCirclex(xc, yc, zc, Rx)
plt.text(48, 60, "Gira 45°")

#___________________ Plotear circulo c 
Rx = radians(30)
xc = 85
yc = 40
zc = 20
plotCirclex(xc, yc, zc, Rx)
plt.text(78, 60, "Gira 30°")

#___________________ Plotear circulo d
Rx = radians(30)
xc = 115
yc = 40
zc = 20
plotCirclex(xc, yc, zc, Rx)
plt.text(108, 60, "Gira 30°")

plt.show()
