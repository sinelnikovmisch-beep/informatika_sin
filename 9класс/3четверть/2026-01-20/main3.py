names = [
    "Ivan Ivanich Ivanov",
    "Abob Abobovich Abobov"
]

second_names = []

for name in names:
    second_names.append(name.split(" ")[2])

print(second_names)