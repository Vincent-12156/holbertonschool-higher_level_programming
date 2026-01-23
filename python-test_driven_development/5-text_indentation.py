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
    if text == "":
        raise TypeError("text must be a string")
    new_text = ""
    for c in text:
        if c == " " and new_text == "":
            continue
        new_text += c

        if c in ".?:":
            print(new_text)
            print()
            new_text = ""
    if new_text:
        print(new_text, end="")
