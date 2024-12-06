class Calculadora:
    def __init__(self):
        pass

    def soma(self,operando_a,operando_b):
        return operando_a + operando_b
    
    def sub(self,operando_a,operando_b):
        return operando_a - operando_b
    
    def mult(self,operando_a,operando_b):
        return operando_a*operando_b
    
    def div(self,operando_a,operando_b):
        try:
            return operando_a/operando_b
        except ZeroDivisionError:
            return "Erro de Divisão por Zero!"