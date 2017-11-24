#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from dft.constructor_injection import TimeDisplay, MidnightTimeProvider, ProductionCodeTimeProvider, datetime



class ConstructorInjectionTest(unittest.TestCase):

    def test_display_current_time_at_midnight(self):
        """
        Will almost always fail (despite of right at/after midnight).
        """
        time_provider_stub = MidnightTimeProvider()
        class_under_test = TimeDisplay(time_provider_stub)
        expected_time = "<span class=\"tinyBoldText\">24:01</span>"
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(), expected_time)

    def test_display_current_time_at_current_time(self):
        """
        Just as justification for working example. (Will always pass.)
        """
        production_code_time_provider = ProductionCodeTimeProvider()
        class_under_test = TimeDisplay(production_code_time_provider)
        current_time = datetime.datetime.now()
        expected_time = "<span class=\"tinyBoldText\">{}:{}</span>".format(current_time.hour, current_time.minute)
        self.assertEqual(class_under_test.get_current_time_as_html_fragment(), expected_time)


		
		#Jorge Miguel Garcia Martinez