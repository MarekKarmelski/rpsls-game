#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Player class."""


class Player:

    elements = ['lizard', 'paper', 'rock', 'scissors', 'spock']

    score = 0

    def choose_element(self):
        """Abstract method"""
        raise NotImplemented

    def increase_score(self):
        """Increase player score."""
        self.score += 1

    def get_score(self):
        """Get player score."""
        return self.score
