def fib_numbers(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c)


fib_numbers(10)
