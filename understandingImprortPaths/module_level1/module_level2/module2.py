#!/usr/bin/env python3
"""
This module is a second level down.
I'm using this to test out doing module imports from a folder structure
"""


def main():
    """
    This is the top level script
    """
    print("This is the main function of module1")
    module2_hello()
    say_hello_again()


def module2_hello():
    """
    This is just to say hello
    """
    print("Hello from module2")


if __name__ == "__main__":
    main()
else:
    from ..module1 import say_hello_again
