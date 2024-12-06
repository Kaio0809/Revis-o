acumulador = 0.0

def soma(operando_b, operando_a = None):
    global acumulador
    if operando_a is None:
        acumulador = acumulador + operando_b
    else:
        acumulador = operando_a + operando_b
    return acumulador

def subtracao(operando_b, operando_a = None):
    global acumulador
    if operando_a is None:
        acumulador = acumulador - operando_b
    else:
        acumulador = operando_a - operando_b
    return acumulador

def multiplicacao(operando_b, operando_a = None):
    global acumulador
    if operando_a is None:
        acumulador = acumulador * operando_b
    else:
        acumulador = operando_a * operando_b
    return acumulador

def divisao(operando_b, operando_a = None):
    global acumulador
    try:
        if operando_a is None:
            acumulador = acumulador / operando_b
        else:
            acumulador = operando_a/operando_b
        return acumulador
    
    except ZeroDivisionError:
        return "Erro de Divisão por Zero"
