numbers = []
isHaveOrder = True
sum = 0

for i in range(10):
    numbers.append(int(input("Input number: ")))
    sum += numbers[i]
    if i != 0 and numbers[i - 1] > numbers[i]:
        isHaveOrder = False

print("Your sum is: ", sum)
print(isHaveOrder)
