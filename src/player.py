#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Player class."""


class Player:

    def __new__(cls):
        if cls.__name__ is 'Player':
            raise Exception("Unable to create an instance of abstract class Player")