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

    def testemptymin(self):
        list = []
        value = ListManipulator(list).min()
        self.assertEqual(value, None)


class TestMax(unittest.TestCase):

    def testmax(self):
        list = [1, 2, 3]
        value = ListManipulator(list).max()
        self.assertEqual(value, 3)

    def testemptymax(self):
        list = []
        value = ListManipulator(list).max()
        self.assertEqual(value, None)


class TestRemove(unittest.TestCase):

    def testremove(self):
        list = [1, 2, 3, 1, 4, 78, 1, 6, 7, 8]
        values = ListManipulator(list)
        values.remove(5)
        for item in values.list:
            self.assertEqual(item, 1)


unittest.main()
