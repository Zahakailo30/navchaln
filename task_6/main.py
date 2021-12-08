from linked_list import Linked_list
import validation
import copy
from context import Context, generate_list
from strategy import *
from validation import *
from observer import *

def menu_opt():
    print('\n Оберіть опцію: \n'
          '1. Перша стратегія \n'
          '2. Друга стратегія \n'
          '3. Генерація списку \n'
          '4. Видалити елемент з позиції \n'
          '5. Видалити кілька позицій \n'
          '6. Вихід \n')

def menu():
    mylist = Linked_list()
    context = None
    obs = Observer()
    obs.observe('add')
    obs.observe('remove')
    while True:
        menu_opt()
        option = int(input())
        if option == 1:
            context = Context(first_strategy())
        elif option == 2:
            context = Context(second_strategy())
        elif option == 3:
            generate_list(mylist, context)
            print(*mylist)
        elif option == 4:
            index = general_validation('Введіть позицію для видалення: ')
            obs_list = copy.deepcopy(list(mylist))
            mylist.delete_index(index)
            Event("remove", list(mylist), obs_list, index)
            print(*mylist)
        elif option == 5:
            one = general_validation('Введіть початкову позицію: ')
            two = general_validation('Введіть кінцеву позицію:')
            obs_list = copy.deepcopy(list(mylist))
            mylist.delete_the_gap(one,two)
            Event("remove", list(mylist), obs_list, (one,two))
            print(*mylist)
        elif option == 6:
            exit()
        else:
            print("Спробуйте ще раз!")
            continue
        print()


menu()
