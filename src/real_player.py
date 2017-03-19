#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
from src.player import Player

"""RealPlayer class."""


class RealPlayer(Player):

    def choose_element(self):
        element = self.get_element_from_strem()
        element_class = getattr(importlib.import_module('src.' + element), element.title())
        element_instance = element_class()
        return element_instance

    def get_element_from_strem(self):
        """Get element from stream."""
        is_incorrect = True
        while is_incorrect:
            print(self.elements)
            element = input('Select your element: ')
            if isinstance(element, str):
                if element in self.elements:
                    is_incorrect = False
                else:
                    print('Element must be from list.')
            else:
                print('Element must be string.')
        return element
