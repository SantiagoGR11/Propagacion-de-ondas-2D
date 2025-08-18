'''
Quiero representar una membrana vibrante tras darle un golpe en un t0 descrito por la función f
Para ello usamos la función de ondas:
u(x,y,t)=sum_n(sum_m((Anm*cos(wnm*t)+Bnm*sin(wnm*t))*sin(n*pi*x/a)*sin(m*pi*y/b)))
Tomamos una solución donde Bnm=0 por c.i.
Anm=4/(ab)*int_0^a(int_0^b(f(x,y)*sin(n*pi*x/a)*sin(m*pi*y/b)dy)dx)
'''


'''IMPORTACIÓN DE MÓDULOS'''
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import dblquad

'''DEFINICIÓN DE PARÁMETROS Y CONDICIONES'''
def f(x,y,a,b): #esta función describe la forma de la membrana en el instante inicial, en este caso suponiendo un golpe de forma gaussiano
    return 10*np.exp(-((x-a/4)**2+(y-b/2)**2)) 
a, b, k=10, 10, 1 #a y b delimitan el dominio a estudiar y k es la cte en la ec. de calor
tf=2 #los tiempos van de 0 hasta 2s
c=20 #velocidad de propagación de las ondas (pongo 5 por poner algo escalado)
N, M=10, 10
Narr, Marr=np.linspace(1,N,N), np.linspace(1,M,M)

''' DEFINICIÓN DE LOS SUMANDOS'''

def usum(x, y, t, n, m, c):
    omega = c * np.pi * np.sqrt((n/a)**2 + (m/b)**2)
    return np.cos(omega * t) * np.sin(n * np.pi * x / a) * np.sin(m * np.pi * y / b)



def g(x,y,n,m):#Definimos la función g como el integrando de Anm
    g=f(x, y, a, b) * np.sin(n*np.pi*x/a) * np.sin(m*np.pi*y/b)
    return g

def Anm(x, y, n, m):
    I = dblquad(g, 0, a, 0, b, args=(n, m))[0]
    A = 4 / (a * b) * I
    return A

'''DEFINICIÓN DE LA SOLUCIÓN'''

def u(x,y,t):
    U=0
    for n in Narr:
        for m in Marr:
            u=Anm(x,y,n,m)*usum(x,y,t,n,m,c)
            U+=u
    return U

'''OBTENEMOS TODOS LOS PUNTOS DE LA SOLUCIÓN'''
x=np.linspace(0,a,100)
y=np.linspace(0,b,100)
t=np.linspace(0,tf,500)
X,Y,T=np.meshgrid(x,y,t)
U=u(X,Y,T)

'''ANIMACIÓN DEL RESULTADO'''

plt.figure()
plt.xlabel('x(m)')
plt.ylabel('y(m)')

#Creamos el primer frame para el primer tiempo
p=plt.imshow(U[:,:,0], cmap='jet', extent=[0,a,0,b])
plt.title("Perturbación gaussiana en t= %.2fs" %(t[0]))
plt.colorbar(p, location='right')

#Creamos el bucle que genera cada frame en un tiempo t
for i in range(len(t)):
    p.remove()
    p=plt.imshow(U[:,:,i], cmap='jet', extent=[0,a,0,b])
    plt.title("Placa en t= %.2fs" %(t[i]))
    plt.pause(0.005)

plt.show()

#Representamos el resultado de la placa tras el tiempo dado, es decir en t=2s
plt.figure() 
plt.xlabel('x(m)')
plt.ylabel('y(m)')
p=plt.imshow(U[:,:,len(t)-1], cmap='hot', extent=[0,a,0,b])
plt.title("Placa en t= %.2fs" %(t[len(t)-1]))
plt.colorbar(p, location='right')
plt.show()

'''
Ahora quiero representar una membrana vibrante en la que se propaga una onda normalita
Para ello usamos la función de ondas:
Tomamos una solución donde B=0 por c.i. y A es una amplitud cte
'''
def u_onda_plana(x, t, A=1, k=2*np.pi/5, c=5):
    omega = c * k
    return A * np.sin(k * x - omega * t)
U_plana = u_onda_plana(X, T)
plt.figure()
plt.xlabel('x(m)')
plt.ylabel('y(m)')
p = plt.imshow(U_plana[:,:,0], cmap='cool', extent=[0,a,0,b])
plt.title("Onda plana en t = %.2fs" % t[0])
plt.colorbar(p, location='right')

for i in range(len(t)):
    p.remove()
    p = plt.imshow(U_plana[:,:,i], cmap='cool', extent=[0,a,0,b])
    plt.title("Onda plana en t = %.2fs" % t[i])
    plt.pause(0.005)

plt.show()


y_index = np.argmin(np.abs(y - b/2))  # índice más cercano a y = b/2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plt.suptitle("Propagación de onda plana en dirección x")

# Subplot 1: Mapa de colores
p1 = ax1.imshow(U_plana[:, :, 0], cmap='cool', extent=[0, a, 0, b])
ax1.set_title("Mapa 2D de amplitud")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
cb1 = fig.colorbar(p1, ax=ax1)

# Subplot 2: Corte en y = b/2
linea, = ax2.plot(x, U_plana[y_index,:, 0])  
ax2.set_ylim(-1.2, 1.2)
ax2.set_title("Corte: u(x, y = b/2, t)")
ax2.set_xlabel("x")
ax2.set_ylabel("u")

# Animación
for i in range(len(t)):
    p1.set_data(U_plana[:, :, i])
    linea.set_ydata(U_plana[y_index,:, i])
    plt.pause(0.01)

plt.show()