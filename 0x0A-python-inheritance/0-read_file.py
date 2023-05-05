#!/usr/bin/python3
""This function return a list within the methods of available obj""


def lookup(obj):
    ""Returns list of available obj""
    return dir(obj)
