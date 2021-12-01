import sys
def general_validation(message):
    # розмір, ксть елементів, позиція
    try:
        print(message)
        n = int(input())
        if n < 0:
            print('Число має бути додатнім!')
            return general_validation(message)
        return n
    except ValueError:
        print("Неправильний тип")
        return general_validation(message)


def validation_for_number(mess):
    try:
        print(mess)
        n = int(input())
        return n
    except ValueError:
        print("Неправильний тип")
        return validation_for_number(mess)
