#!/usr/bin/python3
""" rectangle module contains class Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square clase inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ init with arguments and __init__ from Rectangle """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ printing of instance square """
        id_str = str(self.id)
        w_str = str(self.width)
        x_str = str(self.x)
        y_str = str(self.y)
        div_str = x_str + '/' + y_str + ' - ' + w_str
        return ("[Square] " + '(' + id_str + ') ' + div_str)
