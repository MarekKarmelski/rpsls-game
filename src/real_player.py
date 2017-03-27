#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
from src.player import Player

"""RealPlayer class."""


class RealPlayer(Player):

    def choose_element(self):
        """Get element from stream."""
        element = self.get_element_from_strem()
        element_class = getattr(importlib.import_module('src.' + element), element.title())
        element_instance = element_class()
        return element_instance

    def get_element_from_strem(self):
        """Get element from stream."""
        is_incorrect = True
        while is_incorrect:
            element = input('Select your element {}: '.format(self.elements))
            if isinstance(element, str):
                if element in self.elements:
                    is_incorrect = False
                else:
                    print('-'*50)
                    print('Element must be from list.')
                    print('-' * 50)
            else:
                print('-' * 50)
                print('Element must be string.')
                print('-' * 50)
        return element
