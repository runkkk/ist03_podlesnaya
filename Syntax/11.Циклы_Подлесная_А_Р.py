# 1
board_games = ['Settlers of Catan', 'Carcassonne', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

# 2

promise = 'I will not chew gum in class'

for _ in range(5):
    print(promise)

# 3

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)

for student in students_period_B:
    print(student)

for student in students_period_A:
    students_period_A.append(student)
    break


# 4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihztu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break
