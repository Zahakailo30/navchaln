from linked_list import *
from validation import *

def menu_opt():
    print('\n Оберіть опцію: \n'
          '1. Ввести список \n'
          '2. Генерація елементів рандомно з проміжку [a,b] \n'
          '3. Ітератор \n'
          '4. Генератор \n'
          '5. Додати елемент \n'
          '6. Додати елемент на позицію \n'
          '7. Видалити елемент з позиції \n')

def menu():
    n = general_validation('Введіть розмір списку: ')
    list = Linked_List()
    menu_opt()
    option = int(input())

    while option:
        if option == 1:
            list.fill(n)
            list.print()
            menu_opt()
            option = int(input())
        elif option == 2:
            num = general_validation('Введіть кількість елементів: ')
            if num > n:
                print('Введіть меншу кількість елементів!')
                continue
            list.generate(num)
            list.print()
            menu_opt()
            option = int(input())
        elif option == 3:
            list.by_iter()
            menu_opt()
            option = int(input())
        elif option == 4:
            num = general_validation('Введіть кількість елементів: ')
            if num > n:
                print('Введіть меншу кількість елементів!')
                continue
            list.by_gener(num)
            list.print()
            menu_opt()
            option = int(input())

        elif option == 5:
            new_el = validation_for_number('Введіть елемент: ')
            list.add_to_the_end(new_el)
            list.print()
            menu_opt()
            option = int(input())
        elif option == 6:
            new_el1 = validation_for_number('Введіть елемент: ')
            position = general_validation('Введіть позицію: ')
            list.add_el(new_el1, position)
            list.print()
            menu_opt()
            option = int(input())
        elif option == 7:
            position1 = general_validation('Введіть позицію: ')
            list.delete_el(position1)
            list.print()
            menu_opt()
            option = int(input())

        else:
            exit()



menu()
