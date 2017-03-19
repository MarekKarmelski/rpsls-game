#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.element import Element

"""Scissors class."""


class Scissors(Element):

    name = 'SCISSORS'
    traversed_by = ['ROCK', 'SPOCK']
    beats = ['LIZARD', 'PAPER']
