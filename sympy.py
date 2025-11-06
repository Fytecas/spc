# Il est préférable de coller ce script dans un cahier jupyter
# Pour afficher les valeurs rajoutez des `print` où vous le souhaitez

from sympy.core import Float, Mul, Pow
from sympy.physics.units import meter, nanometer, convert_to, joule, electronvolt 

lblue = Float(4.40 * 10**-7) # m
lyellow = Float(5.95 * 10**-7) # m

# E = h * v(Hz)
h = Float(6.63*10**-34) 
c = Mul(3, Pow(10,8, evaluate = False), evaluate = False) # m/s

# v = c/l
vblue = Float(c / lblue, 3) # Hz
vyellow = c / lyellow # Hz

# E = hv
e0 = Float(0)
e1 = vblue * h
e1p = vyellow * h

Δe11p = e1 - e1p

# E = hv
# v = E/h
vir = Δe11p/h

# v = c/l
# vl = c
# l = c/v
lir = c / vir # m

# convert_to(lir * meter, [nanometer])
# e1p
# convert_to(e1p*joule, [electronvolt])
lir