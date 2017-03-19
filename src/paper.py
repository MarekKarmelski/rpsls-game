#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.element import Element

"""Paper class."""


class Paper(Element):

    name = 'PAPER'
    traversed_by = ['LIZARD', 'SCISSORS']
    beats = ['ROCK', 'SPOCK']
