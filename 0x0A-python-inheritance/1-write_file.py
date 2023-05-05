#!/usr/bin/python3
"""
This function creates a class called MyList that inherits a class List
"""


class MyList(list):
    """
    This class inherits from class list and can print it's sorted elements
    """

    def print_sorted(self):
        print(sorted(self))
