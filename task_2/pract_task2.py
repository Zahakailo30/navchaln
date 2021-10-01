import random
def input_array(n):
    array = []
    for i in range(n):
        a = input_number("Введіть елемент масиву: ")
        array.append(a)
    print(array)
    return array

def check_size(n):
    if n <= 0:
        k = input_number("Помилка! Невірний розмір! Введіть ще раз:")
        n = check_size(k)
        return n
    else:
        return n

def input_number(message):
    while True:
        try:
            print(message)
            n = int(input())
            break
        except ValueError:
            print("Неправильний тип")
    return n


def input_diap():
    print("Введіть діапазон значень для генерації.")
    a = input_number("A: ")
    b = input_number("B: ")
    if a > b:
        a, b = b, a

    return a, b

def generate_array(n, a, b):
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


print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
P = int(input(""))
while P:
    if P == 1:
        n = input_number("Введіть розмір: ")
        array = input_array(check_size(n))
        oper1 = mergeSort(array)
        print(array)
        print("Кількість операцій: ", oper1)
        print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
        P = int(input(""))
    elif P == 2:
        a, b = input_diap()
        n = input_number("Введіть розмір: ")
        array2 = generate_array(check_size(n), a, b)
        oper2 = mergeSort(array2)
        print(array2)
        print("Кількість операцій: ", oper2)
        print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
        P = int(input(""))
    elif P == 3:
        print("Роботу завершено")
        break
    elif P > 3 or P < 0:
        print("Такої опції не існує!")
        print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
        P = int(input(""))


