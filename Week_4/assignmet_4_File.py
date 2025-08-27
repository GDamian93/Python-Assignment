"""
===========================================================================================================
* Programa : assignment_4_File.py
* Author   : G. Damian
* Date     : 2025-08-26
* Version  : 1.0
* Purpose  : To create a program that reads a text file, processes its content, and writes the results
*            to a new file.
* Origin   : Course Assignment 4.
* Notes    : To Practice File handling.
===========================================================================================================
"""
# Opening file for reading
file = open("input.txt", "r")
content = file.read()
file.close()

# Converting the content to uppercase
content= content.upper()

# Writing processed content to new file
file = open("output.txt", "w")
file.write(content)
file.close()