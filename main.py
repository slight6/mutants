""" Main entrypoint into the game. """

import sys
import logging
import pathlib
import csv

start_position = (0, 0)

# Step 1: Read the CSV file
def read_coordinates_from_csv(file_path):
    coordinates = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            coordinates.append(row)
    return coordinates

# Step 2: Store coordinates in a list
file_path = 'new_map.csv'
coordinates = read_coordinates_from_csv(file_path)

# Step 3: Display one coordinate at a time
def display_coordinate(coordinate):
    print(f'Current Position: ({coordinates[0]}, {coordinates[1]})')

# Step 4: Allow user to move around the map
current_position = 0
total_positions = len(coordinates)

while True:
    display_coordinate(coordinates[int(current_position)])

    move = input("Enter 'n' for next, 'p' for previous, 'q' to quit, 'north', 'south', 'east', or 'west': ")

    if move == 'n' and current_position < total_positions - 1:
        current_position += 1
    elif move == 'p' and current_position > 0:
        current_position -= 1
    elif move == 'north':
        if current_position < total_positions - 1:
            current_position += 1
    elif move == 'south':
        if current_position > 0:
            current_position -= 1
    elif move == 'east':
        if current_position < total_positions - 1:
            current_position += 1
    elif move == 'west':
        if current_position > 0:
            current_position -= 1
    elif move == 'q':
        break

    print("\n" + "="*30 + "\n")
