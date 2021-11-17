def fib(n):
    prev = 0
    next = 1
    def calculate():
        nonlocal prev, next
        for i in range(n):
            prev, next = next, prev+next
        return next
    return calculate()

print(fib(6))