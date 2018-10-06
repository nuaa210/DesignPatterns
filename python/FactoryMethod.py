#!/usr/bin/env python
# coding=utf-8

"""
Factory Method
"""

 
class ChinaGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")
 
    def get(self, msg_id):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msg_id]
        except KeyError:
            return str(msg_id)
 
 
class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self, msg_id):
        return str(msg_id)
 
 
def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()
 
# Create our localizers
e, g = get_localizer("English"), get_localizer("China")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
