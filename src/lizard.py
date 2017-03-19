#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.element import Element

"""Lizard class."""


class Lizard(Element):

    name = 'LIZARD'
    traversed_by = ['ROCK', 'SCISSORS']
    beats = ['SPOCK', 'PAPER']
