#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]

import random

num = [random.randint(1, 10) for _ in range(random.randint(3, 10))]
print("Cтворюємо випадковий список:", num)

my_lst = [num[0], num[2], num[-2]]
print("Створюємо інший список з 3 елементів зі списку:", my_lst)
