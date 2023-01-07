import sympy as sp
import numpy as np
import math

#Variable assign && Formula ===================
R_out, R_in, rho_silver, rho_polymer, WP\
    = sp.symbols('R_out Rin rho_silver rho_polymer WP')

A = rho_silver*math.pi*(R_out**2-R_in**2)
B = rho_polymer*math.pi*R_in**2
Equation = sp.Eq(A/(A+B),WP)
#===================================

#Variable value ===================
R_out_value = 1
rho_silver_value = 1000
rho_polymer_value = 100
WP_value = 20
#===================================

C = Equation.subs([(R_out,R_out_value),(rho_silver,rho_silver_value),
                   (rho_polymer,rho_polymer_value),(WP,WP_value)])

Value = sp.solve(C,R_in)


Real_Value = []
for i in range(0,len(Value)):
    if Value[i] > 0:
        Real_Value.append(Value[i])
for i in range(0,len(Real_Value)):
    print('Thickness: ', R_out_value - Real_Value[i])

