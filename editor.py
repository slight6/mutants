""" Module to edit all aspects of the game.
    It will be used to edit the map, players, monsters, etc. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2023'

import csv
import PySimpleGUI as sg
from game_util import log_output as log


def edit_map():
    """ Edit the map.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_area():
    """ Edit an area.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_player():
    """ Edit a player.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_monster():
    """ Edit a monster.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_item():
    """ Edit an item.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_spell():
    """ Edit a spell.
        Args:
            None
        Returns:
            None
    """
    pass


def edit_command():
    """ Edit a command.
        Args:
            None
        Returns:
            None
    """
    pass


def load_data(file_name):
    with open(file_name, mode='r') as map_file:
        reader = csv.DictReader(map_file)
        data = []
        for row in reader:
            data.append({
                'X': row['X Coordinates'],
                'Y': row['Y Coordinates'],
                'Description': row['Description'],
                'Monsters': row['Monsters'],
                'Items': row['Items'],
                'Exits': row['Exits']
            })
    return data

def save_data(file_name, data):
    with open(file_name, mode='w', newline='') as map_file:
        fieldnames = ['X', 'Y', 'Description', 'Monsters', 'Items', 'Exits']
        writer = csv.DictWriter(map_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    sg.theme('Default1')
    file_name = sg.popup_get_file('Select a CSV file to edit', file_types=(("CSV Files", "*.csv"),))

    if file_name:
        data = load_data(file_name)
    else:
        sg.popup('No file selected. Exiting.')
        return

    layout = [
        [sg.Table(values=data, headings=['X', 'Y', 'Description', 'Monsters', 'Items', 'Exits'], auto_size_columns=True, justification='right', key='-TABLE-')],
        [sg.Button('Save'), sg.Button('Exit')]
    ]

    window = sg.Window('CSV Editor', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Save':
            save_data(file_name, values['-TABLE-'])

    window.close()

if __name__ == "__main__":
    main()
