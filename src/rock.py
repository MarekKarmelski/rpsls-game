#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.element import Element

"""Rock class."""


class Rock(Element):

    name = 'ROCK'
    traversed_by = ['PAPER', 'SPOCK']
    beats = ['LIZARD', 'SCISSORS']
