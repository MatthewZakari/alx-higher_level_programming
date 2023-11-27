# Shell and Python Scripting Tasks

This directory contains a collection of Shell and Python scripts addressing various programming and scripting challenges. The tasks cover a range of topics, from running Python files to working with strings and more.

## Table of Contents

0. [Run Python File](#1-run-python-file)
1. [Run Inline](#2-run-inline)
2. [Hello, Print](#3-hello-print)
3. [Print Integer](#4-print-integer)
4. [Print Float](#5-print-float)
5. [Print String](#6-print-string)
6. [Play with Strings](#7-play-with-strings)
7. [Copy - Cut - Paste](#8-copy---cut---paste)
8. [Create a New Sentence](#9-create-a-new-sentence)
9. [Easter Egg](#10-easter-egg)
10. [Linked List Cycle](#11-linked-list-cycle)
11. [Hello, Write](#12-hello-write)
12. [Compile](#13-compile)
13. [ByteCode -> Python #1](#14-bytecode---python-1)

## 0. Run Python File

The script `run_python_file.sh` executes a Python script specified by the environment variable `$PYFILE`.

#!/bin/bash
python "$PYFILE"

## 1. Run Inline

The script `run_inline.sh` runs Python code specified in the environment variable `$PYCODE`.

#!/bin/bash
python -c "$PYCODE"

## 2. Hello, Print (Python Script)

The Python script `hello_print.py` prints the message "Programming is like building a multilingual puzzle."

# hello_print.py
print("Programming is like building a multilingual puzzle")

## 3. Print Integer (Python Script)

The script `print_integer.py` prints an integer followed by "Battery street."

# print_integer.py
number = 42
print(f"{number} Battery street")

## 4. Print Float (Python Script)

The script `print_float.py` prints a float with a precision of 2 digits.

# print_float.py
number = 3.14159
print(f"Float: {number:.2f}")

## 5. Print String (Python Script)

The script `print_string.py` prints a string three times and its first 9 characters.

# print_string.py
str = "Hello, World!"
print(f"{3 * str}\n{str[:9]}")

## 6. Play with Strings (Python Script)

The script `play_with_strings.py` prints the welcome message by combining two strings.

# play_with_strings.py
str1 = "Welcome "
str2 = "to Holberton School!"
print(str1 + str2)

## 7. Copy - Cut - Paste (Python Script)

The script `copy_cut_paste.py` extracts substrings from a given word and prints them.

# copy_cut_paste.py
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

## 8. Create a New Sentence (Python Script)

The script `create_new_sentence.py` prints a new sentence by combining two strings.

# create_new_sentence.py
str1 = "object-oriented programming"
str2 = " with Python"
print(str1 + str2)

## 9. Easter Egg (Python Script)

The script `easter_egg.py` prints "The Zen of Python" by Tim Peters.

## 10. Linked List Cycle (C Function)

The C function `check_cycle` checks if a singly linked list has a cycle.

## 11. Hello, Write (Python Script)

The script `hello_write.py` writes a message to stderr and exits with a status code of 1.

# hello_write.py
import sys

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)

## 12. Compile (Bash Script)

The script `compile_python_file.sh` compiles a Python script file into bytecode.

#!/bin/bash
python -m py_compile "$PYFILE"

## 13. ByteCode -> Python #1 (Python Function)

The Python function `magic_calculation` in `magic_calculation.py` performs the same logic as a given Python bytecode.

# magic_calculation.py
def magic_calculation(a, b):
    if a > b:
        return a + b
    else:
        return a * b - 13


**Note:** Please ensure that the necessary permissions are set to execute the scripts. Use the provided scripts responsibly and in accordance with the task requirements.

