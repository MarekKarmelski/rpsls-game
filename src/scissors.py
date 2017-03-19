#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpsls.src.element import Element

"""Scissors class."""


class Scissors(Element):

    name = 'SCISSORS'
    traversed_by = ['ROCK', 'SPOCK']
    beats = ['LIZARD', 'PAPER']
