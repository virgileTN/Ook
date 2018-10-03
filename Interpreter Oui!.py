"""
Interpreter Oui!.
===========

| Character         | Meaning                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------|
|     Oui. Oui.     | increment the data pointer (to point to the next cell to the right).                        |
|     Oui! Oui!     | decrement the data pointer (to point to the next cell to the left).                         |
|     Oui. Oui?     | increment (increase by one) the byte at the data pointer.                                   |
|     Oui? Oui.     | decrement (decrease by one) the byte at the data pointer.                                   |
|     Oui! Oui.     | output the byte at the data pointer.                                                        |
|     Oui. Oui!     | accept one byte of input, storing its value in the byte at the data pointer.                |
|     Oui! Oui?     | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward
                      to the next command, jump it forward to the command after the matching ] command.      |
|     Oui? Oui!     | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer
                      forward to the,next command, jump it back to the command after the matching [ command.      |
"""

from collections import defaultdict
import sys
import argparse
import re


__author__ = 'ipetrash'



def get_loops_block(source):
    begin_block = []
    blocks = {}
    i = 0
    words = re.findall("Oui[.?!] Oui[.?!]", source)
    l = len(words)  # Number of code symbols
    while i < l:
        s = words[i]
        if s == 'Oui! Oui?':
            begin_block.append(i)
        elif s == 'Oui? Oui!':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
        i += 1
    return blocks


def execute(source):
    """
    EN:
    The function parses source code Oui! and execute it.

    RU:
    Функция выполняет разбор исходного кода Oui! и выполняет его.

    :param source: Исходный код
    :return:
    """

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    Oui = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    words = re.findall("Oui[.?!] Oui[.?!]", source)
    l = len(words)  # Number of code symbols
    loops_block = get_loops_block(source)

    while i < l:
        s = words[i]
        if s == 'Oui. Oui?':  # Go to the next cell
            x += 1
        elif s == 'Oui? Oui.':  # Go to the previous cell
            x -= 1
        elif s == 'Oui. Oui.':  # Increasing the value of the current cell on 1
            Oui[x] += 1
        elif s == 'Oui! Oui!':  # Decrease the value of the current cell on 1
            Oui[x] -= 1
        elif s == 'Oui! Oui.':  # Printing the value of the current cell
            print(chr(Oui[x]), end='')
        elif s == 'Oui. Oui!':  # Enter a value in the current cell
            Oui[x] = int(input("Input = "))
        elif s == 'Oui! Oui?':  # Begin loop
            if not Oui[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s == 'Oui? Oui!':  # End loop
            if Oui[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1


def create_parser():
    parser = argparse.ArgumentParser(description='Interpreter language Oui!.')
    parser.add_argument("path", help="Path to file")
    return parser


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        file_name = args.path
        source = open(file_name).read()
        execute(source)
