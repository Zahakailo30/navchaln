from linked_list import Linked_list
import abc
import random
import validation
from iterator import generator


class Strategy(Linked_list):
    @abc.abstractmethod
    def generate_data(self, data: Linked_list, position, smth):
        pass


class first_strategy(Strategy):
    def generate_data(self, data: Linked_list, position, length) -> None:

        print("Введіть діапазон значень для генерації.")
        a = validation.validation_for_number("A: ")
        b = validation.validation_for_number("B: ")
        if a > b:
            a, b = b, a
        for i in range(length):
            data.add(data.add_el(*generator(a, b), position))



class second_strategy(Strategy):
    def generate_data(self, data: Linked_list, position, filename) -> None:
        with open(filename, "r") as infile:
            for line in infile:
                for x in line.split():
                    data.add_el(int(x), position)
                    position += 1
        infile.close()