#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import random
from src.player import Player

"""AiPlayer class."""


class AiPlayer(Player):

    def choose_element(self):
        """Random element."""
        element = random.choice(self.elements)
        element_class = getattr(importlib.import_module('src.' + element), element.title())
        element_instance = element_class()
        return element_instance
