# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр)
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def rd_file(f_name):
    with open(f_name, 'r', encoding='utf-8') as my_fyle_1:
        file_content = my_fyle_1.read()
        return file_content


f_name = 'docs/z6.txt'
voc = {}
z = rd_file(f_name).split()
y = 0
for idx in z:
    if idx == '—':
        z[y] = 0
    y += 1

for item in range(0, len(z), 4):
    name = z[item]
    lec = z[item + 1]
    prac = z[item + 2]
    lab = z[item + 3]
    voc[name] = int(lec) + int(prac) + int(lab)
print(voc)