# Задача 5: Инвентаризация товаров

items = [
    [('Рубашка', 'Одежда'), ('Кружка', 'Посуда')],
    [('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')],
    [('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]
]

for item in items:
    result = dict(map(lambda x: (x[1], 1), item))
    print(result)
    