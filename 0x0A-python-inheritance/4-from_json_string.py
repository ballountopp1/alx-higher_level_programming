#!/usr/bin/python3
"""
Validate if a class inherits from a_class
"""


def inherits_from(obj, a_class):
    """rue if the object is an instance
    of a class that inherited"""
    
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)
