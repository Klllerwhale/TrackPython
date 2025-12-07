numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
num = sum(numbers[:4]+numbers[5:])
b = len(numbers)
c = round(num/b, 2)
numbers [4]=c
print("Измененный список:", numbers)


