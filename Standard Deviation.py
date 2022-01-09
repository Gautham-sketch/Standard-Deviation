import csv
import math

opener = open("data.csv")
reader = csv.reader(opener)
data = list(reader)

whole_data = []
for i in range(len(data)):
    full_list = data[i][0]
    data.append(float(full_list))

length = len(whole_data)
total = 0
for x in whole_data :
    total += x
mean = total/length

num1 = mean - 60
num2 = mean - 61
num3 = mean - 65
num4 = mean - 63
num5 = mean - 98
num6 = mean - 99
num7 = mean - 90
num8 = mean - 95
num9 = mean - 91
num10 = mean - 96

square1 = math.sqrt(num1)
square2 = math.sqrt(num2)
square3 = math.sqrt(num3)
square4 = math.sqrt(num4)
square5 = math.sqrt(num5)
square6 = math.sqrt(num6)
square7 = math.sqrt(num7)
square8 = math.sqrt(num8)
square9 = math.sqrt(num9)
square10 = math.sqrt(num10)

sum = square1 + square2 + square3 + square4 + square5 + square6 + square7 + square8 + square9 + square10

divide = sum/num1+num2+num3+num4+num5+num6+num7+num8+num9+num10

answer = math.sqrt(divide)
print(answer)