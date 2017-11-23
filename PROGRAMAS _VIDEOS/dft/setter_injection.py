#!/usr/bin/python
# -*- coding : utf-8 -*-
import datetime


class TimeDisplay(object):

    def __init__(self):
        pass

    def set_time_provider(self, time_provider):
        self.time_provider = time_provider

    def get_current_time_as_html_fragment(self):
        current_time = self.time_provider.now()
        current_time_as_html_fragment = "<span class=\"tinyBoldText\">{}</span>".format(current_time)
        return current_time_as_html_fragment


class ProductionCodeTimeProvider(object):
   

    def now(self):
        current_time = datetime.datetime.now()
        current_time_formatted = "{}:{}".format(current_time.hour,
                                                current_time.minute)
        return current_time_formatted


class MidnightTimeProvider(object):
  

    def now(self):
        current_time_is_always_midnight = "24:01"
        return current_time_is_always_midnight
