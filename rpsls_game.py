#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib

"""RPSLS game."""


class RPSLSGame:

    APPLICATION_NAME = 'Application: RPSLS'
    LINE_LENGTH = 50

    def run(self):
        run_app = True
        """Run application."""
        self.display_app_name()
        self.display_app_menu()
        while run_app:
            option = self.get_menu_option_from_strem()
            if option == 1:
                self.get_all_family_persons()
                self.display_app_menu()
            elif option == 2:
                self.get_family_person()
                self.display_app_menu()
            elif option == 3:
                self.add_new_person_to_family()
                self.display_app_menu()
            elif option == 4:
                self.remove_family_person()
                self.display_app_menu()
            elif option == 5:
                self.close_app()
                run_app = False

    def display_app_name(self):
        """Display application name."""
        self.print_line()
        print(self.APPLICATION_NAME)
        self.print_line()

    def display_app_menu(self):
        """Display application menu."""
        print('MENU:')
        print('1. Start new game')
        print('2. Show family person')
        print('3. Add person')
        print('4. Remove person')
        print('5. Close application')
        self.print_line()

    def get_menu_option_from_strem(self):
        """Get option from stream."""
        is_incorrect = True
        while is_incorrect:
            option_number = input('Select option [1-5]: ')
            if option_number.isdigit():
                option_number = int(option_number)
                if option_number in [1, 2, 3, 4, 5]:
                    is_incorrect = False
                else:
                    print('Option number must by from 1 to 5.')
                    self.print_line()
            else:
                print('Option number must by an integer number.')
                self.print_line()
        self.print_line()
        return option_number

    def close_app(self):
        """Close application."""
        print('CLOSE APPLICATION')
        self.print_line()

    def print_line(self):
        """Print line."""
        print('-' * self.LINE_LENGTH)

#rpsls_game = RPSLSGame()
#rpsls_game.run()

my_module = importlib.import_module("src.rock")
MyClass = getattr(my_module, "Rock")
instance = MyClass()
print(instance)
