#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = 0
    best_value = 0

    if not a_dictionary:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > best_value:
                best_value = value
                best_key = key
        return best_key
