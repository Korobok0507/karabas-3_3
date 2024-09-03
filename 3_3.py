# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1,2)
print_params('Vasya', False,'Fantomas')

# 2.Распаковка параметров:
# Создание списка и словаря
values_list = [24, 'моя строка', False]
values_dict = {'a': 95, 'b': 'тоже моя строка', 'c': [4, 33, 76]}

# Распаковка параметров
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
# Создание списка с двумя элементами
values_list_2 = [54.32, 'Строка']

# Проверка распаковки
print_params(*values_list_2, 42)