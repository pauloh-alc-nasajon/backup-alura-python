def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber apenas valores inteiros")

    try:
        aux = dividendo / divisor
        return aux
    except:
        print(f"Nao foi possivel dividir {dividendo} por {divisor}")
        raise

def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisao de 10 por {divisor} eh {resultado}')


try:
    testa_divisao(0.0)
except ZeroDivisionError as E:
    print(E.__class__.__bases__)
    print("Erro de divisao por zero tratado")
except AttributeError as E:
    print(E.__class__.__bases__)
    print("Erro de atributo tratado")
except Exception as E:
    print("Tratamento generico")

print("Programa encerrado")