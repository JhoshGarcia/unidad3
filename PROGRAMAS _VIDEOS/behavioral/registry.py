#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RegistryHolder(type):

    REGISTRY = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
       
"""
            Aquí el nombre de la clase se usa como clave pero podría ser cualquier clase
            parámetro.
        """
        cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(object):
    __metaclass__ = RegistryHolder
    
"""
        Se incluirá cualquier clase que herede de BaseRegisteredClass
        dentro del dict RegistryHolder.REGISTRY, la clave es el nombre del
        clase y el valor asociado, la clase misma.
    """
    pass

if __name__ == "__main__":
    print("Before subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)

    class ClassRegistree(BaseRegisteredClass):

        def __init__(self, *args, **kwargs):
            pass

    print("After subclassing: ")
    for k in RegistryHolder.REGISTRY:
        print(k)
"""jorge miguel garcia"""
