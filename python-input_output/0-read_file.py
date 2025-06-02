#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF8)
and prints its content to stdout.
"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
