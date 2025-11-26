"""Конвертер валют Создайте простой конвертер валют,
который переводит grn в euro по заданному курсу."""

# Решение:
rate = float(input("Введите текущий курс euro к grn: "))
grn = float(input("Введите сумму в grn: "))
euro = grn / rate
print(f"{grn} grn = {euro:.2f} euro")
