#!/usr/bin/env python
# coding=utf-8

"""
Interpreter
"""


class Context:
    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression:
    def Interpret(self, ctx):
        pass


class Expression(AbstractExpression):
    def Interpret(self, ctx):
        print("terminal interpret")


class NonterminalExpression(AbstractExpression):
    def Interpret(self, ctx):
        print("Nonterminal interpret")


if __name__ == "__main__":
    context = ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
