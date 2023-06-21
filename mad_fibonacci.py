# napisz program wczytujący liczbe naturlną odpowiadający na pytanie czy liczba ta jest iloczynem dowolnych dwóch wyrazów fibonacciego
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibV2(n):
    if n == 1 or n == 2:
        return 1
    temp1 = 1
    temp2 = 1
    temp3 = 0
    for i in range(3, n + 1):
        temp3 = temp1 + temp2
        temp1 = temp2
        temp2 = temp3
    return temp3


def fibonacci(n):
    for i in range(n):
        for j in range(n):
            A = fib(i)
            B = fib(j)
            if A * B > n:
                pass
            if A * B == n:
                return i * j


# fibonacci(16)
print(fibV2(6))
