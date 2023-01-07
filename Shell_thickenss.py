import sympy as sp
import numpy as np
import math

#Variable assign && Formula ===================
R_out, R_in, rho_silver, rho_polymer, WP\
    = sp.symbols('R_out Rin rho_silver rho_polymer WP')

A = rho_silver*math.pi*((R_out**2)-(R_in**2))
B = rho_polymer*math.pi*R_in**2
Equation = sp.Eq((A/(A+B)),WP)
print(Equation)
#===================================

#Variable value ===================
R_out_value = 0.5 #Unit: cm
rho_silver_value = 10.49 #Unit: 10.49g/cm^3
rho_polymer_value = 0.92 #Unit: 0.92g/cm^3
WP_value = 0.25
#===================================
C_math = sp.solve(Equation,R_in)
#print(C_math)

C = Equation.subs([(R_out,R_out_value),(rho_silver,rho_silver_value),
                   (rho_polymer,rho_polymer_value),(WP,WP_value)])
Value = sp.solve(C,R_in)

Real_Value = []

for i in range(0,len(Value)):
    if Value[i] > 0:
        Real_Value.append(Value[i])

for i in range(0,len(Real_Value)):
    print(Real_Value[i])
    print('Thickness[mm]: ', (R_out_value - Real_Value[i])*10)
    print('Ratio:', ((R_out_value - Real_Value[i])/Real_Value[i]))

