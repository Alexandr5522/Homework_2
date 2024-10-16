my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    num = my_list[index]
    if num == 0:
        index += 1
        continue
    if num < 0:
        break
    print('Значение: ',my_list[index])
    index += 1
