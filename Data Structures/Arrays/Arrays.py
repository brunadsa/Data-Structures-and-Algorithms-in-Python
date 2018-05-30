#Arrays

numbers = [1, 2, 3, 4, 5]

#random indexing --> O(1) if we know the index
#print(numbers[0])

numbers[3] = "Bruna"
for num in numbers:
    print(num)

print("----------------------")

for i in range(len(numbers)):
    print(numbers[i])

print("----------------------")

print(numbers[0:1])
print(numbers[0:2])
print(numbers[0:3])
print(numbers[0:4])
print(numbers[0:5])
print(numbers[:-1])
print(numbers[:-2])
print(numbers[:-3])
print(numbers[:-4])
print(numbers[:-5])

print("----------------------")

numbers = [18, 32, 43, 234, 195]
print("1) Find the max in", numbers)
max = numbers[0]
for num in numbers:
    if max < num:
        max = num
print("Max is", max)

print("----------------------")
numbers = [18, 32, 43, 234, 195]
print("2) Find the max in", numbers)
max = 0
for i in range(len(numbers)):
    if max < numbers[i]:
        max = numbers[i]

print("Max is", max)

