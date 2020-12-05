n = int(input('Ingrese el limite de la serie Fibonacci: '))
primero = 0
segundo = 1
fibo = 0
i = 0
print(i, ' ', primero)
i = i + 1
print(i, ' ', segundo)
i = i + 1
for i in range(n-1):               
    fibo = primero + segundo
    primero = segundo
    segundo = fibo       
    print(i+2, ' ', fibo)