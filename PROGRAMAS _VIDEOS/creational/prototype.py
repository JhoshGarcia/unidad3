#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Prototype(object):

    value = 'default'

    def clone(self, **attrs):
       
"""Clonar un prototipo y actualizar el diccionario de atributos internos"""
        # Python in Practice, Mark Summerfield
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):

    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """obtenemos todos los objetos"""
        return self._objects

    def register_object(self, name, obj):
        """registramos los objetos"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """y se Anular el registro de un objeto"""
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)
    print([{n: p.value} for n, p in dispatcher.get_objects().items()])


if __name__ == '__main__':
    main()

"""jorge miguel garcia"""
