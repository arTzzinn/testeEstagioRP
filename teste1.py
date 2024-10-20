def fibonacci(n):
    fib_sequence = [0, 1] 
    
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def verifica_fibonacci(numero):
    
    sequencia = fibonacci(numero)
    
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."


numero_informado = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero_informado)
print(resultado)
