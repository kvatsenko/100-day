numbers = list(map(int, input('give me some numbers of integers separated by a space: ').split()))

for i in range(len(numbers)):
    for a in range(len(numbers) - i - 1):
        if numbers[a] > numbers[a + 1]:
            numbers[a], numbers[a + 1] = numbers[a + 1], numbers[a]
print(numbers)


# arr = list(map(int, input('Введите некоторое количество целых чисел через пробел: ').split()))
# # Например: Введите некоторое количество целых чисел через пробел: 1 2 3 4 5 6 7
# print(arr)  # [1, 2, 3, 4, 5, 6, 7]

# k = -1 # индекс последнего элемента списка при первой итерации

# for i in range(len(arr)//2):
#     print("\nбыло - ", i, arr)
#     arr[k], arr[i] = arr[i], arr[k]
#     print("стало    ", arr)
#     k -= 1

# """
# было -  0 [1, 2, 3, 4, 5, 6, 7]
# стало     [7, 2, 3, 4, 5, 6, 1]

# было -  1 [7, 2, 3, 4, 5, 6, 1]
# стало     [7, 6, 3, 4, 5, 2, 1]

# было -  2 [7, 6, 3, 4, 5, 2, 1]
# стало     [7, 6, 5, 4, 3, 2, 1]
# """
