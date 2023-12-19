#!/usr/bin/env python3

from module_level1.module1 import module1_hello
import module_level1.module_3


def main():
    """
    This is the top level script
    """

    module1_hello()
    module_level1.module_3.test1.module3_hello()


if __name__ == "__main__":
    main()
