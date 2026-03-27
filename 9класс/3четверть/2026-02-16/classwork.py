import numpy as np
import math

#Задание №1
vec1 = np.array([1, 0])
vec2 = np.array([0, 1])

print("angle:" + str(np.degrees(math.acos(vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))))))

#Задание №2

list = [np.array([1, 0]), np.array([0, 1])]

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i].dot(list[j]) == 0:
            print(list[i], list[j])

#Задания №3

