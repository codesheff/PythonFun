#!/usr/bin/env python3


def main():
    """
    This is the top level script
    """
    print("This is the main function of module1")
    module1_hello()


def module1_hello():
    """
    This is just to say hello
    """
    print("Hello from module1")

    module2_hello()


def say_hello_again():
    """
    This is going to be called from module2
    """
    print("Hello again,from module 1")


if __name__ == "__main__":
    from module_level2.module2 import module2_hello

    main()
else:
    from .module_level2.module2 import module2_hello
