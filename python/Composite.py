#!/usr/bin/env python
# coding=utf-8

"""
Composite
"""


class Component:
    def __init__(self, str_name):
        self.m_strName = str_name

    def add(self, com):
        pass

    def display(self, depth):
        pass


class Leaf(Component):
    def add(self, com):
        print("leaf can't add")

    def display(self, depth):
        strtemp = "-" * depth
        strtemp = strtemp + self.m_strName
        print(strtemp)


class Composite(Component):
    def __init__(self, str_name):
        super(Composite, self).__init__(str_name)
        self.c = []

    def add(self, com):
        self.c.append(com)

    def display(self, depth):
        str_temp = "-" * depth
        str_temp = str_temp + self.m_strName
        print(str_temp)
        for com in self.c:
            com.display(depth + 2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.add(Leaf("Lee"))
    p.add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.add(Leaf("San"))
    p.add(p1)
    p.display(1)
