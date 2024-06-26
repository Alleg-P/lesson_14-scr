# Задача 5: Инвентаризация товаров
  
def count_items(items):
    total = {}
    for item in items:
        total[item[1]] = total.get(item[1], 0) + 1
    return total

input_data = [
    [('Рубашка', 'Одежда'), ('Кружка', 'Посуда')],
    [('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')],
    [('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')]
]

output_data = list(map(lambda x: count_items(x), input_data))

for data in output_data:
    print(data)
    