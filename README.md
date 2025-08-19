# Propagacion-de-ondas-2D
Una simulación numérica de una membrana vibrante con los extremos fijados. Una a partir de una perturbación inicial gaussiana y otra de una onda plana.

## Modelo matemático

En cuanto lo matemático, se parte de la EDP de ondas en dos dimensiones 
$\frac{\partial^2 u}{\partial t^2} = c^2 (\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2})$
Y se construye la simulación matemática a partir de los coef. de Fourier:
$$u(x,y,t) = \sum_n \sum_m 
\Big( A_{nm} \cos(\omega_{nm} t) \Big) 
\sin\!\left(\frac{n \pi x}{a}\right)
\sin\!\left(\frac{m \pi y}{b}\right)$$

## Resultados

###Membrana vibrante
