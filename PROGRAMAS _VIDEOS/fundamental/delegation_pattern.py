#!/usr/bin/env python
# -*- coding: utf-8 -*-
#clasificacion de clases sobre los objetos
class Delegator(object):
    
# se define los parametros
    def __init__(self, delegate):
        self.delegate = delegate

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if hasattr(self.delegate, name):
                attr = getattr(self.delegate, name)
                if callable(attr):
                    return attr(*args, **kwargs)
        return wrapper


class Delegate(object):

    def do_something(self, something):
        return "Doing %s" % something


if __name__ == '__main__':
    import doctest
    doctest.testmod()
#Jorge miguel gacia marinez