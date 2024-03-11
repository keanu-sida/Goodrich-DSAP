import random
def my_choice(data):
    return data[random.randrange(len(data))]

data = [1, 4, 712, 122, 12, 45, 32]

print(my_choice(data))