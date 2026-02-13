# 1

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# 2

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations['friend'])

# 3

animals_in_zoo = {}

animals_in_zoo["зебры"] = 8
animals_in_zoo["обезьяны"] = 12
animals_in_zoo["динозавров"] = 0

print(animals_in_zoo)

# 4

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739

print(user_ids)

# 5

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# 6

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = dict(zipped_drinks)

print(drinks_to_caffeine)