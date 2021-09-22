import random
def input_array():
    n = int(input("Введіть розмір масиву: "))
    array = []
    for i in range(n):
        a = int(input("Введіть елемент масиву: "))
        array.append(a)
    print(array)
    return array
def generate_array():
    n = int(input("Введіть розмір масиву: "))
    print("Введіть діпазон значень для генерації.")
    a = int(input("A: "))
    b = int(input("B: "))
    array = []
    for i in range(n):
        array.append(random.randint(a, b))
    print(array)
    return array
def mergeSort(array):
    if len(array) > 1:
        exchanges = comparisons = 0

        middle = len(array)//2
        left_array = array[:middle]
        right_array = array[middle:]
        exchanges += 1

        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                exchanges += 1
            else:
                array[k] = right_array[j]
                j += 1
                exchanges += 1
            k += 1
            comparisons += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
            exchanges += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
            exchanges += 1

        operation = exchanges + comparisons
        return operation

try:
    print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
    P = int(input(""))
    while (P == 1 or P == 2) :
        while (P == 1):
            array1 = input_array()
            oper1 = mergeSort(array1)
            print(array1)
            print("Кількість операцій: ", oper1)
            print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
            P = int(input(""))
        while (P == 2):
            array2 = generate_array()
            oper2 = mergeSort(array2)
            print(array2)
            print("Кількість операцій: ", oper2)
            print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
            P = int(input(""))
        if (P == 3):
            print("Роботу завершено")
except ValueError:
    print("Введено неправильний тип даних!")
except Exception:
    print("Помилка!")

