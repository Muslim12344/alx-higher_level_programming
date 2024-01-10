root@DESKTOP-C5794NR:~/pythone/alx-higher_level_programming/0x0B-python-input_output# cat 3-to_json_string.py
#!/usr/bin/python3
"""
contain the JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
