#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Element class."""


class Element:

    name = 'ELEMENT'
    traversed_by = []
    beats = []

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name
