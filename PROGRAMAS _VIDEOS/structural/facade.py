#!/usr/bin/env python
# -*- coding: utf-8 -*-
#importas las print_function
from __future__ import print_function
import time

SLEEP = 0.1

#declara las claes y los parametros
# Complex Parts
class TC1:

    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC2:

    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC3:

    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


# Facade
class TestRunner:

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

#Jorge miguel Garcia Martinez