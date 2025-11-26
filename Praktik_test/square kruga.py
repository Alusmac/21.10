"""Расчет площади круга Создайте программу, которая
вычисляет площадь круга по заданному радиусу."""

# S = π × r²
a = float(input("Vvedite Radius kruga: "))
sq = 3.14 * (a**2)
print(f"{a} Radius = {sq:.2f} Square")
