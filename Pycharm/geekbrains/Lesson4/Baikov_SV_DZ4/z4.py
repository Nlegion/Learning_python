# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from random import randint

gen_list = [randint(1, 10) for i in range(20)]
print(gen_list)

# вариант 1
new_gen_list = []
for item in gen_list:
    if gen_list.count(item) < 2:
        new_gen_list.append(item)
print(new_gen_list)

# вариант 2
new_gen_list_2 = [item for item in gen_list if gen_list.count(item) < 2]
print(new_gen_list_2)
