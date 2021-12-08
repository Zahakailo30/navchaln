from strategy import *
from observer import *
import copy


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def generate_list(self, list, position, n) -> None:
        self._strategy.generate_data(list, position, n)




def generate_list(mylist, context):
    context = validation.generation_validation(context)
    if isinstance(context.strategy, first_strategy):
        dani = validation.general_validation("Введіть кількість елементів: ")
    else:
        dani = validation.validation_for_file('data.txt')
    position = validation.general_validation("Введіть позицію: ")
    obs_list = copy.deepcopy(list(mylist))


    context.generate_list(mylist, position, dani)
    Event("add", list(mylist), obs_list, position)