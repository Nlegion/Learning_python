# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

#user_month = int(input('введите номер месяца'))
user_month = 2
# словарь
month_dic = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна',
             5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
             9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

print(f'Время года: {month_dic[user_month]}')

#длинный список
month_list_1 = ['', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'Время года: {month_list_1[user_month]}')

#короткий список
month_list_2 = ['зима', 'весна', 'лето', 'осень']

if 3 <= user_month <= 5:
    print(f'Время года: {month_list_2[1]}')
elif 6 <= user_month <= 8:
    print(f'Время года: {month_list_2[2]}')
elif 9 <= user_month <= 11:
    print(f'Время года: {month_list_2[3]}')
else:
    print(f'Время года: {month_list_2[0]}')