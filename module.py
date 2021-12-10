from sympy import symbols, Eq, solve
import json

def esolve(equation):
    x = symbols('x')
    feq = equation.replace("x", "{x}").split("=")
    eq1 = Eq((eval(feq[0].format(x=x))), eval(feq[1].format(x=x)))
    return solve((eq1), (x))[0]
