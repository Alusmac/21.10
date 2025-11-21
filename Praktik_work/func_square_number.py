# Створіть функцію, яка приймає список чисел і повертає
# новий список, де кожне число замінено його квадратом.
def square_numbers(numbers):
    """
    Замінює кожне число у списку його квадратом.

    :param numbers: Список чисел.
    :return: Новий список з квадратами чисел.
    """
    result = []
    for n in numbers:
        result.append(n**2)
    return result


# Перевірка
assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
assert square_numbers([]) == []
