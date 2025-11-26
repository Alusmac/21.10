"""Расчет индекса массы тела Напишите программу для расчета
индекса массы тела (ИМТ) по формуле: вес (кг) / (рост (м))²."""

vvod1 = float(input("Vvedite svou Vagy : "))
vvod2 = float(input("Vvedite svou Rost : "))
ind = vvod1 / (vvod2**2)

print(f"{vvod1} kg i {vvod2} cm = {ind:.2f} Vash index tila")
