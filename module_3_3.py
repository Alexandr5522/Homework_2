def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)  # функция работает c измененным типом данных
print_params(c=[1, 2, 3])  # функция работает с измененным типом данных

values_list = [555, 'Denis', False]
dict_ = {'a': 89367798800, 'b': 89273546789, 'c': 89324568756}  # работает при полном совпадении названия параметра

print_params(*values_list)
print_params(**dict_)

values_list_2 = ['Alex', 88]
print_params(*values_list_2, 42)  # 42 это параметр 'с'
