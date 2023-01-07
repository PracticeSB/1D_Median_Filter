import sympy as sp
import numpy as np
import math

R_out, R_in, rho_silver, rho_polymer, m1, m2, WP\
    = sp.symbols('R_out Rin rho_silver rho_polymer m1 m2 WP')

A = rho_silver*math.pi*(R_out**2-R_in**2)
B = rho_polymer*math.pi*R_in**2
Equation = sp.Eq(A/(A+B),WP)
print(sp.solve(Equation,R_in))
Thickness = R_out - R_in

