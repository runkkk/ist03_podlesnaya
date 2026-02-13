
#1

n1 = bool((6 * 6) - 1 == 8 + 1)
n2 = bool(13 - 7 != (3 * 2) + 1)
n3 = bool(3 * (2 - 1) == 4 - 1)
print(n1, n2, n3)

a1 = bool((6 * 6) - 1 >= 8 + 1)
a2 = bool(13 - 7 <= (3 * 2) + 1)
a3 = bool(3 * (2 - 1) > 4 - 1)
print(a1, a2, a3)

bool_variable = 'true'  # если вывезти без кавычек - ошибка, так как не определен тип данных
print(type(bool_variable))

bool_variable_2 = True
print(type(bool_variable_2))

user_name = input()
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и щаймись работой!'
ans = 'Добро пожаловать'
enter_number = 3
if user_name == 'Дмитрий':
    enter_number -= 1
    print(Dmitriy_check)
else:
    print(ans)

if enter_number < 3:
    print(f'Попробуйте еще раз, у вас осталось {3 - enter_number} попыток')
else:
    print('Вы привычили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокиовки обратитесь в службу поддержки')




