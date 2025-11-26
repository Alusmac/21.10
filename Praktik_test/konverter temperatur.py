"""Конвертер температур Напишите программу
для преобразования температуры из градусов Цельсия в градусы Фаренгейта."""

# (0 °C × 9/5) + 32 = 32 °F
a = float(input("Vvedite temperaturu po Celsiu: "))
foreng = (a * 1.8) + 32
print(f"{a} Celsiu = {foreng} Fahrenheit")
