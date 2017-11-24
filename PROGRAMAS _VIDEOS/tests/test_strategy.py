#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import unittest


class StrategyTest(unittest.TestCase):

    def test_print_output(self):
      
        output = subprocess.check_output(["python", "behavioral/strategy.py"])
        expected_output = os.linesep.join([
            'Strategy Example 0',
            'Strategy Example 1 from execute 1',
            'Strategy Example 2 from execute 2',
            ''
        ])
        # byte representation required due to EOF returned subprocess
        expected_output_as_bytes = expected_output.encode(encoding='UTF-8')
        self.assertEqual(output, expected_output_as_bytes)

		
		#Jorge Miguel Garcia Martinez