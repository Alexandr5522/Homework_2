first = int(input('Введите число:'))                 # вводим 123 или 42 или 33
second = int(input('Введите число:'))                # вводим 456 или 69 или 33
third =  int(input('Введите число:'))                # вводим 789 или 42 или 33
if first == second and first == third and second == third :
    print('Все значения равны = 3')
elif first == second or first == third or second == third or second == first :
    print('Только два из трех значений равны = 2/3')
else:
    print('Значения не равны = 0')
print('Проверка окончена')