# 1

import random

name = input('Введите имя: ')
question = input('Задайте вопрос: ')
answer = ''

random_number = random.randint(1, 9)
print(f'{name} спрашивает {question}')

a1 = 'Да, безусловно.'
a2 = 'Это решительно так.'
a3 = 'Без сомнения.'
a4 = 'Ответ туманный, попробуйте еще раз.'
a5 = 'Спросите еще раз позже.'
a6 = 'Лучше не говорить вам сейчас.'
a7 = 'Мои источники говорят "Нет".'
a8 = 'Прогноз не очень хороший.'
a9 = 'Очень сомнительно.'

if random_number == 1:
   answer = a1
elif random_number == 2:
    answer = a2
elif random_number == 3:
    answer = a3
elif random_number == 4:
    answer = a4
elif random_number == 5:
    answer = a5
elif random_number == 6:
    answer = a6
elif random_number == 7:
    answer = a7
elif random_number == 8:
    answer = a8
elif random_number == 9:
    answer = a9
else:
    print('Ошибка')

print(f'Магический шар отвечает: {answer}')

#2

maxi = float(input('Введите максимум:'))
mini = float(input('Введите минимум:'))
sred = float(input('Введите среднее:'))
otkl = float(input('Введите стандартное отклонение:'))
if (maxi <= sred + 3 * otkl) or (mini >= sred - 3 * otkl):
    print('Ваши данные пригодны для анализа.')
elif (maxi > sred + 5 * otkl) or (mini < sred - 5 * otkl):
    print('В ваших данных имеются экстремальные значения и требуют предобработки.')
elif (5 * otkl + sred >= maxi > sred + 3 * otkl) or (sred - 5 * otkl <= mini < sred - 3 * otkl):
    print('В ваших данных имеются выбросы и требуют доработки.')

# 3
age_of_user = int(input('Введите возраст; '))
age_limit = int(input('Введите ограничение: '))
if age_of_user >= age_limit:
    print('Приятного просмотра!')
else:
    print('Извините, ваш возраст не соответсвует введенным возрастным ограничениям')


# 4

car_brand = input('Введите марку машины, на которой хотите поехать(Volkswagen Polo / BMW X1)\n')
age_of_driver = int(input('Введите возраст водителя, с которым хотели бы поехать(20 - 34)\n'))
experience_of_driver = int(input('Введите стаж водителя, с которым хотели бы поехать(2 - 15)\n'))
reputation_of_driver = int(input('Введите репутацию водителя, с которым хотели бы поехать(1 - 5)\n'))
traffic_jams = int(input('Введите загруженность дорог в данный момент(1 - 7)\n'))
trip_duration = int(input('Введите длительность поездки(в минутах)\n'))

rate_per_minute = 0
if car_brand == 'Volkswagen Polo':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 8.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.5
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.4
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7.2
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 7.2
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 6.9
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.7
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 6.6

elif car_brand == 'BMW X1':
    if 20 <= age_of_driver <= 27:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 12
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 12.5
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.6
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.3
    elif 27 <= age_of_driver <= 34:
        if 2 <= experience_of_driver <= 9:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.4
            elif 3 <= reputation_of_driver <= 5:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 11.7
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11.9
        elif 10 <= experience_of_driver <= 15:
            if 1 <= reputation_of_driver <= 2:
                if 1 <= traffic_jams <= 3:
                    rate_per_minute = 10.8
                elif 4 <= traffic_jams <= 7:
                    rate_per_minute = 11
            elif 3 <= reputation_of_driver <= 5:
                if 4 <= traffic_jams <= 7:
                    rate_per_minute = 10.9

price = rate_per_minute * trip_duration
if price == 0:
    print('Проверьте введённые вами данные, где-то допущена ошибка')
else:
    print(f'Стоимость вашей поездки составит {price}')




# 5

cof = input('Введите название кофе: ')
cap = '1.Сварите кофе. Можно сварить в турке (доведите до кипения 2-3 раза, чтобы напиток получился насыщеннее). Или заварить во френч-прессе. Обязательно процедите, налейте в подогретую кружку. 2.Подогрейте молоко. Старайтесьне перегревать его больше, чем 65 градусов. Оно не должно быть сильно горячим. 3. Взбейте с помощью блендера или миксера. Добивайтесь однородной пены, без крупных пузырьков.Влейте взбитую массу в кофе.'
lat = 'Кофе следует заварить, причем любым способом, который вам кажется удобнее. Главное, чтобы кофе был довольно крепким. Молоко нужно разогреть, но не кипятить: оптимальной будет температура в 50-60 градусов. Читайте ещё: вкусный рецепт приготовления кофе по турецки. 4. После этого его нужно тщательно взбить с помощью блендера (либо миксера).'

if cof == 'Капучино':
    print(cap)
elif cof == 'Латте':
    print(lat)
