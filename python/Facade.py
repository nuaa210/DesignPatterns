#!/usr/bin/env python
# coding=utf-8

"""
Facade
"""

import time

SLEEP = 0.5


# Complex Parts
class TC1:
    def run(self):
        print("###### In Test 1 ######", self)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC2:
    def run(self):
        print("###### In Test 2 ######", self)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC3:
    def run(self):
        print("###### In Test 3 ######", self)
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


# Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [i for i in (self.tc1, self.tc2, self.tc3)]

    def run_all(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.run_all()
