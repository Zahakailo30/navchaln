from iterator import *
from validation import *

class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

class Linked_list:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def __getitem__(self, index):
        pos = 0
        current = self.head
        if self.__len__() <= index:
            print('Немає такого індекса')
            return None
        while pos is not index:
            current = current.next
            pos += 1
        return current.data

    def print(self):
        value = self.head
        while value is not None:
            print(value.data, end = ' ')
            value = value.next

    def fill(self, length):
        self.head = None
        for i in range(length):
            el = validation_for_number("Ввести елемент: ")
            self.add_to_the_end(el)

    def add_to_the_beginning(self, other):
        if self.head is None:
            self.head = Node(other)
        else:
            rest = self.head
            self.head = Node(other)
            self.head.next = rest

    def add_el(self, new_el, position):
        position = position-1
        if position < 0 or position > self.__len__():
            print('Позиція має бути >= 1 і меншою за розмір.')
            return None
        if position == 0:
            self.head = Node(new_el, self.head)
        elif position == self.__len__():
            self.add_to_the_end(new_el)
        else:
            i = 0
            current = self.head
            while current.next:
                if i == position - 1:
                    current.next = Node(new_el, current.next)
                current = current.next
                i += 1

    def add(self, new_node):
        if self.head:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    def is_empty(self):
        return self.head is None

    def add_to_the_end(self, item):
        if self.is_empty():
            self.add(item)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(item,None)

    def clear(self):
        temp = self.head
        if temp is None:
            print('Пусто')
        while temp:
            self.head = temp.next
            temp = self.head
    def delete(self, position):
        current = self.head
        previous = None
        while current and current.item != position:
            previous = current
            current = current.next
        if current:
            if previous is None:
                self.head = self.head.next
            else:
                previous.next = current.next
        else:
            print('Нема такої позиції.')


    def generate(self, number_of_elements):
        print("Введіть діапазон значень для генерації.")
        a = validation_for_number("A: ")
        b = validation_for_number("B: ")
        if a > b:
            a, b = b, a
        for i in range(number_of_elements):
            self.add_to_the_end(random.randint(a, b))


    def by_gener(self, number):
        print("Введіть діапазон значень для генерації.")
        a = validation_for_number("A: ")
        b = validation_for_number("B: ")
        if a > b:
            a, b = b, a
        temp = generator(a,b)
        for i in range(number):
            result = next(temp)
            self.add_to_the_beginning(result)

    def by_iter(list):
        for i in list:
            print(i)


    def index(self, item):
        position = 0
        current = self.head
        found = False
        while current and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
                position += 1
        if not found:
            print('Індекс не знайдено')
        return position

    def delete_index(self,index):
        index = index - 1
        i = 0
        current = self.head
        previous = None
        while current and i != index:
            previous = current
            current = current.next
            i += 1
        if current:
            if previous is None:
                self.head = self.head.next
            else:
                previous.next = current.next
        else:
            print('Такого індексу у списку немає')

    def delete_the_gap(self, one, two):
        if two > self.__len__() or one > two:
            print('Спробуйте ще раз.')
        for i in range(two - one + 1):
            self.delete_index(one)
