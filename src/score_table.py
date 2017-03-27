#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

"""ScoreTable class."""


class ScoreTable:

    headers = False;

    table_data = []

    def set_headers(self, headers):
        """Set score table headers."""
        self.headers = headers

    def set_round_data(self, round, first_player_score, second_player_score):
        data = [round, first_player_score, second_player_score]
        self.table_data.append(data)

    def display(self):
        """Display score table."""
        print(self.format_matrix(self.headers, self.table_data, '{:^{}}', '', '{:>{}.0f}', '\n', ' | '))

    def save_to_file(self):
        """Save score table to file"""
        file_name = 'game_' + time.strftime('%Y%m%d%H%M%S') + '.txt'
        with open(file_name, 'w') as game_score_file:
            game_score_file.write(self.table_data)

    def format_matrix(self, header, matrix,
                      top_format, left_format, cell_format, row_delim, col_delim):
        """Score table."""
        table = [[''] + header] + [[name] + row for name, row in zip(header, matrix)]
        table_format = [['{:^{}}'] + len(header) * [top_format]] \
                       + len(matrix) * [[left_format] + len(header) * [cell_format]]
        col_widths = [max(
            len(format.format(cell, 0))
            for format, cell in zip(col_format, col))
                      for col_format, col in zip(zip(*table_format), zip(*table))]
        return row_delim.join(
            col_delim.join(
                format.format(cell, width)
                for format, cell, width in zip(row_format, row, col_widths))
            for row_format, row in zip(table_format, table))
