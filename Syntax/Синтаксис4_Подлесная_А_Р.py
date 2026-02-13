# 1

favor_world = 'так'
print(favor_world)

# 2 - 3

first_name = 'Виталий'
last_name = 'Красилов'
new_account = last_name[0:5]
temp_password = last_name[3:7]
print(new_account, temp_password)


def account_generator(first_name, last_name):
    return first_name[0:3] + last_name[0:3]


new_account = account_generator(first_name, last_name)
print(new_account)


# 4

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')


def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]


temp_password = password_generator(first_name, last_name)
print(temp_password)

# 5

company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last, final_word)