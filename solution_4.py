# Задача 4: Фибоначчи для ценообразования

def fibonacci_prices():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

gen = fibonacci_prices()
for _ in range(10):
    print(next(gen))
    