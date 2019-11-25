# Ritti Bhogal
# Software Development Fundamentals Programming Lab 10
# This program tests the functionality of the List Manipulator class
import unittest

class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1

class TestMin(unittest.TestCase):
    def testmin(self):
        list = [1, 2, 3]
        value = ListManipulator(list).min()
        self.assertEqual(value, 1)

class TestRemove(unittest.TestCase):
    def testremove(self):
        list = [1, 2, 3]
        values = ListManipulator(list)
        values.remove(1)
        for item in values.list:
            self.assertEqual(item, 1)
            print()


