#!/usr/bin/python3
"""
text must be a string,
otherwise raise a TypeError exception with
the message text must be a string
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in ['.', '?', ':']:
            print()
            print()
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
