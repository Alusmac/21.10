"""Вычисление НДС Напишите программу,
которая вычисляет сумму НДС (20%) от введенной пользователем суммы."""

sum = float(input("Vvedite summu dla rozrahunky: "))
result = sum * 20 / 100
ost = sum - result
print(f"{sum:.2f} Vasha summa = {result:.2f} Podatok 20% = {ost:.2f} Vash Ostatok")
