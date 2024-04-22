# Задача 3: Генератор отчетов

def report_generator(*args):
    for page in args:
        yield page

report = report_generator("Стр 1", "Стр 2", ...)

print(report)
