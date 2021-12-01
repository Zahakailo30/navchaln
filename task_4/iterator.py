import random
import linked_list
from validation import *

class List_Iterator():

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


def generator(range):
    while True:
        yield random.choice(range)

