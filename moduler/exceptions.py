# -*- coding: utf-8 -*-
#
class AddLineFileNotFound(FileNotFoundError):
    """Function add line can't open non existing file"""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f"Function AddLine filen {self.message} er ikke fundet"
        else:
            return "AddLineFileNotFound error has been raised"

