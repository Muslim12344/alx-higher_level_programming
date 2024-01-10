#!/usr/bin/python3
"""
Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
root@DESKTOP-C5794NR:~/pythone/alx-higher_level_programming/0x0B-python-input_output# cat 2-append_write.py
#!/usr/bin/python3
"""
function that appends a string
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
