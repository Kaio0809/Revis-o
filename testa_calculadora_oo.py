from calculadora_oo import Calculadora

def teste():
    calc = Calculadora()
    print(calc.soma(10,15))
    print(calc.sub(15,10))
    print(calc.mult(10,15))
    print(calc.div(10,15))
    print(calc.div(0))
    print(calc.soma(10))
    print(calc.sub(9))
    print(calc.mult(10))
    print(calc.div(2))

teste()
