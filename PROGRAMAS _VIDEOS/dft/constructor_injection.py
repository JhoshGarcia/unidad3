#!/usr/bin/python
# -*- coding : utf-8 -*-
#se importa de datetime 
import datetime
#declaramos las clses con sus respectivas parametros
class TimeDisplay(object):

    def __init__(self, time_provider):
        self.time_provider = time_provider

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment


class ProductionCodeTimeProvider(object):
    
"""Versión del código de producción del proveedor de tiempo (solo un contenedor para el formato de fecha y hora para este ejemplo)."""

    def now(self):
        current_time = datetime.datetime.now()
        current_time_formatted = "{}:{}".format(current_time.hour,
                                                current_time.minute)
        return current_time_formatted


class MidnightTimeProvider(object):
    
"""Clase implementada como stub codificado (a diferencia del stub configurable).
    """

    def now(self):
        current_time_is_always_midnight = "24:01"
        return current_time_is_always_midnight
		
		
""" Jorge Miguel Garcia Martinez"""
