#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
