def add_everything_up(a, b):
    try:
        # Если оба значения числовые (int или float), складываем их
        return a + b
    except TypeError:
        # Если возникает ошибка, значит типы разные (число и строка)
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))      # Вывод: яблоко4215
print(add_everything_up(123.456, 7))           # Вывод: 130.456