# Створіть функцію, яка приймає список чисел і повертає новий список,
# де всі числа помножені на 2, але тільки для парних чисел.
def multiply_even_numbers(numbers):
    """
    Помножує всі парні числа у списку на 2.

    :param numbers: Список чисел.
    :return: Новий список з парними числами, помноженими на 2.
    """
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i * 2)
    return result


# Перевірка
assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]
