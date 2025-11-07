n = int(input("Введіть число: "))

while n > 9:  # Поки число більше 9
    product = 1
    for digit in str(n):
        product *= int(digit)
    n = product  # нове число — результат множення

print(n)
