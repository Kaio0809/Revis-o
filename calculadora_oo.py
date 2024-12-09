class Calculadora:
    def __init__(self):
        self.__acumulador = 0.0

    def soma(self,operando_b,operando_a = None):
        if operando_a is None:
            self.__acumulador += operando_b
        else:
            self.__acumulador = operando_a + operando_b
        return self.__acumulador
    
    def sub(self,operando_b, operando_a = None):
        if operando_a is None:
            self.__acumulador -= operando_b
        else:
            self.__acumulador = operando_a - operando_b
        return self.__acumulador
    
    def mult(self,operando_b,operando_a = None):
        if operando_a is None:
            self.__acumulador *= operando_b
        else:
            self.__acumulador = operando_a * operando_b
        return self.__acumulador
    
    def div(self,operando_b,operando_a = None):
        try:
            if operando_a is None:
                self.__acumulador /= operando_b
            else:
                self.__acumulador = operando_a / operando_b
            return self.__acumulador
        except ZeroDivisionError:
            return "Erro de Divisão por Zero!"