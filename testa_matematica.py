import matematica as math
from matematica.estatistica import media

def teste():
    print("Soma:",math.soma(15,15))
    print("Subtração:",math.sub(20,10))
    print(f"Area do círculo: {math.area_circulo(10)}")
    print(f"Area do Retangulo: {math.area_retangulo(10,15)}")
    a = [10,15,19,45]
    print(f"Média da lista {a} é {media.media_simples(a)}")

teste()