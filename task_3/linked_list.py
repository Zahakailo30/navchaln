import random
from validation import *
import numpy as np

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

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


    def add_to_the_end(self, new_el):
        new_node = Node(new_el)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node

    def add_el(self, new_el, position):
        new_node = Node(new_el)
        if position < 0 or position > self.__len__():
            print('Позиція має бути >= 1 і меншою за розмір.')
        elif (position == 1):
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                new_node.next = temp.next
                temp.next = new_node

    def delete_el(self, position):
        if self.head == None:
            return
        temp = self.head
        if position == 1:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 2):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            print('Нема такої позиції.')
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def generate(self,number_of_elements):
        print("Введіть діапазон значень для генерації.")
        a = validation_for_number("A: ")
        b = validation_for_number("B: ")
        if a > b:
            a, b = b, a
        for i in range(number_of_elements):
            self.add_to_the_end(random.randint(a, b))



