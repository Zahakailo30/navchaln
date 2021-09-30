import random
def input_array(n):
    while True:
        try:
            array = []
            for i in range(n):
                a = int(input("Введіть елемент масиву: "))
                array.append(a)
            print(array)
            break
        except ValueError:
            print("Неправильний тип!")
    return array

def input_number():
    while True:
        try:
            n = int(input("Введіть розмір масиву: "))
            if n <= 0:
                print("Введіть правильний розмір!")
                continue
            break
        except ValueError:
            print("Неправильний тип")
    return n

def input_diap():
    while True:
        try:
            print("Введіть діпазон значень для генерації.")
            a = int(input("A: "))
            b = int(input("B: "))
            if a > b:
                a, b = b, a

            break
        except ValueError:
            print("Неправильний тип")
    return a, b

def generate_array(n, a, b):
    while True:
        try:
            array = []
            for i in range(n):
                array.append(random.randint(a, b))
            print(array)
            break
        except ValueError:
            print("Неправильний тип!")
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
        n = input_number()
        array = input_array(n)
        oper1 = mergeSort(array)
        print(array)
        print("Кількість операцій: ", oper1)
        print("Оберіть опцію:\n 1 - ввести масив \n 2 - згенерувати масив \n 3 - завершити роботу \n", end=" ")
        P = int(input(""))
    elif P == 2:
        n = input_number()
        a, b = input_diap()
        array2 = generate_array(n, a, b)
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


