# 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла,
# а затем «выделение» из этого пути имени файла (без расширения).


def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


print(get_file_name('/var/logs/nginx/error.log'))
