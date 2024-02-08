def verifica_pertence_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

while True:
    try:
        numero_informado = int(input("Informe um número: "))
        if verifica_pertence_fibonacci(numero_informado):
            print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
            break 
        else:
            print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
