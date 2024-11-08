def add_everything_up(a, b):
    # Проверяем, являются ли a и b разными типами (число и строка)
    if isinstance(a, str) and isinstance(b, (int, float)):
        return f"{a}{b}"
    elif isinstance(b, str) and isinstance(a, (int, float)):
        return f"{a}{b}"

    # Если оба аргумента числа, возвращаем их сумму
    return a + b

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))      # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456

