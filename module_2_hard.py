import random


def one_window():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = int(random.choice(numbers))
    return num


num = one_window()
print('Первое поле: ', num)  # выпадает случайное число от 3 до 20


def get_password():
    password = ""
    for i in range(1, 21):
        for j in range(1, 21):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = get_password()
print('Пароль для выхода из ловушки: ', ' '.join(result))
