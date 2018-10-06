#!/usr/bin/env python
# coding=utf-8

"""
Decorator
"""


class Foo(object):
    def f1(self):
        print("original f1", self)

    def f2(self):
        print("original f2", self)


class FooDecorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


u = Foo()
v = FooDecorator(u)
v.f1()
v.f2()
