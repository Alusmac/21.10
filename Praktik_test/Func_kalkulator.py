# Створіть функцію калькулятора, яка приймає два числа і операцію
# (додавання, віднімання, множення, ділення) та повертає результат.


def calculator(num1, num2, operation):
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """
    result = 0
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            result = "Error"
        result = num1 / num2
    else:
        return "unknown operation"
    return result


# Перевірка
assert calculator(5, 3, "add") == 8
