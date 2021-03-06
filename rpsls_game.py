#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from src.real_player import RealPlayer
from src.ai_player import AiPlayer
from src.score_table import ScoreTable

"""RPSLS game."""


class RPSLSGame:

    APPLICATION_NAME = 'Game: RPSLS'
    LINE_LENGTH = 50

    def run(self):
        """Run game."""
        run_app = True
        self.display_app_name()
        self.display_app_menu()
        while run_app:
            option = self.get_menu_option_from_strem()
            if option == 1:
                run_game = True
                self.clear()
                self.display_game_menu()
                while run_game:
                    game_option = self.get_game_menu_option_from_strem()
                    if game_option == 1:
                        run_game = True
                        self.clear()
                        self.round_game()
                        self.display_game_menu()
                    elif game_option == 2:
                        run_game = True
                        self.clear()
                        self.points_game()
                        self.display_game_menu()
                    elif game_option == 3:
                        self.clear()
                        run_game = False
                self.display_app_menu()
            elif option == 2:
                self.clear()
                self.exit_game()
                run_app = False

    def display_app_name(self):
        """Display application name."""
        self.print_line()
        print(self.APPLICATION_NAME)

    def display_app_menu(self):
        """Display application menu."""
        self.print_line()
        print('MENU:')
        self.print_line()
        print('1. Start new game')
        print('2. Exit game')
        self.print_line()

    def display_game_menu(self):
        """Display game menu."""
        self.print_line()
        print('GAME MENU:')
        self.print_line()
        print('1. Round game')
        print('2. Points game')
        print('3. Back')
        self.print_line()

    def get_menu_option_from_strem(self):
        """Get option from stream."""
        is_incorrect = True
        while is_incorrect:
            option_number = input('Select option [1-2]: ')
            if option_number.isdigit():
                option_number = int(option_number)
                if option_number in [1, 2]:
                    is_incorrect = False
                else:
                    print('Option number must by from 1 to 2.')
                    self.print_line()
            else:
                print('Option number must by an integer number.')
                self.print_line()
        self.print_line()
        return option_number

    def get_game_menu_option_from_strem(self):
        """Get game option from stream."""
        is_incorrect = True
        while is_incorrect:
            game_option_number = input('Select option [1-3]: ')
            if game_option_number.isdigit():
                game_option_number = int(game_option_number)
                if game_option_number in [1, 2, 3]:
                    is_incorrect = False
                else:
                    print('Option number must by from 1 to 3.')
                    self.print_line()
            else:
                print('Option number must by an integer number.')
                self.print_line()
        self.print_line()
        return game_option_number

    def round_game(self):
        """Round game."""
        self.print_line()
        print('ROUND GAME')
        self.print_line()
        rounds = self.get_rounds_number_from_stream()
        current_round = 1
        score_table = ScoreTable()
        score_table.set_headers(['ROUND', 'USER', 'AI'])
        real_palyer = RealPlayer()
        ai_player = AiPlayer()
        while current_round <= rounds:
            self.print_line()
            print('ROUND {0}'.format(current_round))
            self.print_line()
            print('SCORE: REAL USER({0}) - AI({1})'.format(real_palyer.get_score(), ai_player.get_score()))
            self.print_line()
            real_player_element = real_palyer.choose_element()
            ai_player_element = ai_player.choose_element()
            self.print_line()
            print('USER selection: [{}] - AI selection: [{}]'.format(real_player_element, ai_player_element))
            self.print_line()
            if real_player_element == ai_player_element:
                real_palyer.increase_score()
                ai_player.increase_score()
            elif real_player_element > ai_player_element:
                real_palyer.increase_score()
            elif real_player_element < ai_player_element:
                ai_player.increase_score()
            score_table.set_round_data(current_round, real_palyer.get_score(), ai_player.get_score())
            current_round += 1
        print('SCORE: REAL USER({0}) - AI({1})'.format(real_palyer.get_score(), ai_player.get_score()))
        self.print_line()
        if real_palyer.get_score() > ai_player.get_score():
            print('USER WIN!!!!')
        elif ai_player.get_score() > real_palyer.get_score():
            print('AI WIN!!!')
        else:
            print('REMIS!!!')
        self.print_line()
        print('SCORE TABLE')
        self.print_line()
        score_table.display()
        score_table.save_to_file()


    def points_game(self):
        """Points game."""
        self.print_line()
        print('POINTS GAME')
        self.print_line()
        points = self.get_points_number_from_stream()
        current_round = 1
        score_table = ScoreTable()
        score_table.set_headers(['ROUND', 'USER', 'AI'])
        real_palyer = RealPlayer()
        ai_player = AiPlayer()
        while real_palyer.get_score() < points and ai_player.get_score() < points:
            self.print_line()
            print('ROUND {0}'.format(current_round))
            self.print_line()
            print('SCORE: REAL USER({0}) - AI({1})'.format(real_palyer.get_score(), ai_player.get_score()))
            self.print_line()
            real_player_element = real_palyer.choose_element()
            ai_player_element = ai_player.choose_element()
            self.print_line()
            print('USER selection: [{}] - AI selection: [{}]'.format(real_player_element, ai_player_element))
            self.print_line()
            if real_player_element == ai_player_element:
                real_palyer.increase_score()
                ai_player.increase_score()
            elif real_player_element > ai_player_element:
                real_palyer.increase_score()
            elif real_player_element < ai_player_element:
                ai_player.increase_score()
            score_table.set_round_data(current_round, real_palyer.get_score(), ai_player.get_score())
            current_round += 1
        print('SCORE: REAL USER({0}) - AI({1})'.format(real_palyer.get_score(), ai_player.get_score()))
        self.print_line()
        if real_palyer.get_score() > ai_player.get_score():
            print('USER WIN!!!!')
        elif ai_player.get_score() > real_palyer.get_score():
            print('AI WIN!!!')
        else:
            print('REMIS!!!')
        self.print_line()
        print('SCORE TABLE')
        self.print_line()
        score_table.display()
        score_table.save_to_file()

    def get_rounds_number_from_stream(self):
        """Get rounds number from stream."""
        is_incorrect = True
        while is_incorrect:
            rounds_number = input('Type number of rounds: ')
            if rounds_number.isdigit():
                rounds_number = int(rounds_number)
                return rounds_number
            else:
                self.print_line()
                print('Rounds number must by an integer number.')
                self.print_line()
        self.print_line()

    def get_points_number_from_stream(self):
        """Get points number from stream."""
        is_incorrect = True
        while is_incorrect:
            points_number = input('Type number of points: ')
            if points_number.isdigit():
                points_number = int(points_number)
                return points_number
            else:
                print('Points number must by an integer number.')
                self.print_line()
        self.print_line()

    def exit_game(self):
        """Exit game."""
        self.print_line()
        print('EXIT GAME')
        self.print_line()

    def print_line(self):
        """Print line."""
        print('-' * self.LINE_LENGTH)

    def clear(self):
        if os.name == 'nt':
            c = os.system('cls')
        else:
            c = os.system('clear')
        del c

rpsls_game = RPSLSGame()
rpsls_game.run()
