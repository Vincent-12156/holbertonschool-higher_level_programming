#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        result.append(i % 2 == 0)
        print(result)
    return result
