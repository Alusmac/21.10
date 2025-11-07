# Користувач вводить кількість секунд
seconds = int(input("Введіть кількість секунд (0 ≤ n < 8640000): "))

# Константи
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

# Обчислення днів, годин, хвилин і секунд
days, remainder = divmod(seconds, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

# Вибір правильної форми слова "день"
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"
# Форматування виводу
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
