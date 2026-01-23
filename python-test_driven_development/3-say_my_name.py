#!/usr/bin/python3
"""
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name
must be a string or last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is first name and last name
    """
    if first_name == "":
        raise ValueError("first_name must be a string")
    if not isinstance(first_name, str) and not "":
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
