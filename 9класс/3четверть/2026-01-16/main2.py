numbers = [1, 2, 5, 9, 0]

for i in range(len(numbers)):
    current = numbers[i]
    index = i-1
    while current < numbers[index] and index >= 0:
        numbers[index+1] = numbers[index]
        index -= 1
    numbers[index+1] = current

print(numbers)