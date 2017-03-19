#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.element import Element

"""Spock class."""


class Spock(Element):

    name = 'SPOCK'
    traversed_by = ['LIZARD', 'PAPER']
    beats = ['SCISSORS', 'ROCK']
