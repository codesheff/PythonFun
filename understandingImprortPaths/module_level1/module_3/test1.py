#!/usr/bin/env python3
"""
This module is a second level down.
I'm using this to test out doing module imports from a folder structure
"""


def main():
    """
    This is the top level script
    """
    print("This is the main function of module3")
    module3_hello()


def module3_hello():
    """
    This is just to say hello
    """
    print("Hello from module3")


if __name__ == "__main__":
    main()
