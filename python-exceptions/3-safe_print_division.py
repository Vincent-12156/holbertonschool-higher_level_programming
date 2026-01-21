#!/usr/bin/python3
def safe_print_division(a, b):
    quotien = None
    try:
        quotien = a / b
    except (TypeError, ZeroDivisionError):
        quotien = None
    finally:
            print("Inside result: {}".format(quotien))
    return quotien
