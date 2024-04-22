# Задача 2: Фильтр товаров

prices = [99, 150, 200, 349, 501]

rounded_prices = sorted(list(dict.fromkeys(map(lambda x: round(x, -2), prices))))

print(rounded_prices)
