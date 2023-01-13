#!/usr/bin/python3
"MyList"


class MyList(list):
    """class"""
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
