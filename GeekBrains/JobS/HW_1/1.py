# Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.
# Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
# После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
# Полученная строка выводится в главной функции.
# Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.

def table(length, height):
    main = []
    f = lambda x: '\t'.join(str(item) for item in x)
    for item in range(1, height + 1):
        row = []
        row.append([item2 * item for item2 in range(1, length + 1)])
        main.append(f(row))
    return main

print(table(14, 5))