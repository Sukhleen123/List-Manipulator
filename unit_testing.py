# Ritti Bhogal
# Software Development Fundamentals Programming Lab 10
# This program tests the functionality of the List Manipulator class

# Gain access to testing abilities
import unittest


# Given class that removes items from list and finds min and max
class ListManipulator:
    # Define objects that will be input by user
    def __init__(self, list):
        self.list = list

    # Min function returns smallest value in list
    def min(self):
        # If list is empty, return nothing
        if len(self.list) == 0:
            return None

        # Set min equal to first value in list
        min = self.list[0]
        # If there is an item in the list smaller than min, that item becomes new min
        for item in self.list:
            if item < min:
                min = item
        return min

    # Max function returns largest value in list
    def max(self):
        # If list is empty, return nothing
        if len(self.list) == 0:
            return None

        # Set max equal to first value in list
        max = self.list[0]
        # If there is an item in the list greater than max, that item becomes new max
        for item in self.list:
            if item > max:
                max = item
        return max

    # Remove function removes a vlue in the list
    def remove(self, value):
        # Create an empty list in which user can insert values
        to_remove = []
        # For loop checks if value input exists as an element in list
        for i, item in enumerate(self.list):
            # if statement removes value if it does exist
            if item == value:
                to_remove.append(i)

        # Counts the number of items that have been removed
        removed_count = 0
        # For loop returns value being removed
        for index in to_remove:
            self.list.pop(index - removed_count)
            # Increases the # of values removed by 1
            removed_count += 1


# Class that tests whether correct min is retrieved
class TestMin(unittest.TestCase):
    # Function tests whether value returned is the min
    def testmin(self):
        # Create list of values
        list = [0, 1, 2, 3]
        # Store list of values in ListManipulator class and find min
        value = ListManipulator(list).min()
        # Test whether list manipulator class retrieves correct value
        self.assertEqual(value, 0)

    # Function that tests whether anything is returned
    def testempty_min(self):
        # Create empty list for testing
        list = []
        # Store list of values in ListManipulator class and find min
        value = ListManipulator(list).min()
        # Test whether list manipulator class retrieves none
        self.assertEqual(value, None)


# Class that tests whether correct max is retrieved
class TestMax(unittest.TestCase):
    # Function tests whether value returned is the max
    def testmax(self):
        # Create list of values
        list = [0, 1, 2, 3]
        # Store list of values in ListManipulator class and find max
        value = ListManipulator(list).max()
        # Test whether list manipulator class retrieves correct value
        self.assertEqual(value, 3)

    # Function that tests whether anything is returned
    def testempty_max(self):
        # Create empty list for testing
        list = []
        # Store list of values in ListManipulator class and find max
        value = ListManipulator(list).max()
        # Test whether list manipulator class retrieves none
        self.assertEqual(value, None)


class TestRemove(unittest.TestCase):
    # Function that tests whether correct value was removed
    def testremove_quality(self):
        # Create list of values
        to_remove = [1, 2, 3, 4, 5, 6]
        # Store list of values in ListManipulator class
        values = ListManipulator(to_remove)
        # Remove value at index 0 in list stored in ListManipulator class
        values.remove(1)
        # For loop ensures that
        for item in values.list:
            self.assertNotEqual(item, 1)

    # Function that tests whether value was removed at all
    def testremove_quantity(self):
        # Create list of values
        to_remove = [1, 2, 3, 1, 4, 5, 6]
        # Store list of values in ListManipulator class
        values = ListManipulator(to_remove)
        # Remove the element 1 in list stored in ListManipulator class
        values.remove(1)
        # Ensures that a value has been removed/list length decreases by 2
        self.assertEqual(len(values.list), 5)


unittest.main()
