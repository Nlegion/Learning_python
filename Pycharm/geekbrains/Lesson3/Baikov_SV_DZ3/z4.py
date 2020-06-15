# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    y *= -1
    z = x
    for item in range(1, y):
        z *= x
    return 1 / z


# x = float(input('введите действительное положительное число'))
# y = input('целое отрицательное число'))
x = 2.36
y = -3

while (x <= 0) or (type(x) != float):
    # x = float(input('введите действительное положительное число'))
    x = 2.00
while (y >= 0) or (type(y) != int):
    # x = input('ведите целое отрицательное число')
    y = -3
print(my_func_1(x, y))
print(my_func_2(x, y))
