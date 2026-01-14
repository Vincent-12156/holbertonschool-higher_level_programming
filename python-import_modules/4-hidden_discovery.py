#!/usr/bin/python3
import sys
import os

sys.path.insert(0, "/root")

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
