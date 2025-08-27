"""
========================================================================================================
* Programa : assignment_4_Exception.py
* Author   : G. Damian
* Date     : 2025-08-26
* Version  : 1.0
* Purpose  : Ask the user for a filename and handle errors if it doesn't exist or can't be read
* Origin   : Course Assignment 4.
* Notes    : To Practice Exception handling.
========================================================================================================
"""
namefile = input("Enter the file name: ")
try:
    file = open(namefile, 'r')
    content = file.read()
    file.close()
    print(f"File's content:\n{content}")
except FileNotFoundError:
    print("❌ File not found. Please check the file name and try again.")
except IsADirectoryError:
    print("❌ Invalid file path. Please check the file path.")
except PermissionError:
    print("❌ Permission denied. Unable to access the file.")
