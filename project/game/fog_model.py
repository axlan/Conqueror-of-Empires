# Ben-Ryder 2019

import random
import paths
import constants

import project.game.calculations as calculations


class Model:
    """ holds all the data and interface to manipulate the game """
    def __init__(self, player, map_name):  # only when creating new game
        self.map_name = map_name
        self.game_end = False
        self.world = World(self.map_name)  # assigns settlements to players
        self.current_player = player

    def get_current_player(self):
        return self.current_player

    def game_ended(self):
        return self.game_end



class Player:
    """ Each player of the game, which holds their units, key values and links to settlements etc"""
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.camera_focus = [None, None]  # TODO: system to auto-scroll to spawn
        self.show_minimap = False

        self.units = []
        self.settlements = []

        self.turn = 0
        self.ap = 3  # initial ap, not per turn. (first turn ap = self.ap + self.get_turn_ap()
        self.dead = False
        self.max_score = self.ap
        self.cash = 10
        self.purchases = []

        # self.wood = 0
        # self.stone = 0
        # self.metal = 0

    # def add_wood(self, amount):
    #     self.wood += amount
    #
    # def add_stone(self, amount):
    #     self.stone += amount
    #
    # def add_metal(self, amount):
    #     self.metal += amount

    def get_name(self):
        return self.name

    def is_dead(self):
        return self.dead

    def kill(self):
        self.dead = True

    def get_colour(self):
        return self.colour

    def get_turn(self):
        return self.turn

    def get_score(self):
        # score workout =  Each city's score +  turn*5 +  each unit's health.
        score = 0
        score += self.turn * 5
        for city in self.settlements:
            score += city.get_score()

        for unit in self.units:
            score += unit.health

        if score > self.max_score:
            self.max_score = score
        return score

    def get_max_score(self):
        return self.max_score

    def get_ap(self):
        return self.ap

    def get_turn_ap(self):
        ap = 0
        for city in self.settlements:
            ap += city.get_ap_value()  # changed from generate_ap
        return ap

    def take_ap(self, amount):
        self.ap -= amount

    def start_turn(self):
        self.ap += self.get_turn_ap()

        # Resetting all units for new turn
        for unit in self.units:
            unit.reset()

    def end_turn(self):
        self.turn += 1

    def add_settlement(self, reference):
        self.settlements.append(reference)

    def remove_settlement(self, reference):
        self.settlements.remove(reference)

    def add_unit(self, unit):
        self.units.append(unit)

    def delete_unit(self, unit):
        self.units.remove(unit)

    def get_camera_focus(self):
        return self.camera_focus

    def set_camera_focus(self, camera_focus):
        self.camera_focus = camera_focus

    def get_minimap_status(self):
        return self.show_minimap

    def set_minimap_status(self, show):
        self.show_minimap = show


class Tile:
    def __init__(self, tile_type, position):
        self.type = tile_type
        self.position = position
        # self.wood, self.stone, self.metal = constants.TILE_DATA[tile_type]

    def get_type(self):
        return self.type

    def get_position(self):
        return self.position

def get_world(map_name):
    # Reading in the map from a .csv file, convert to list of strings.
    with open(paths.mapPath + map_name + ".csv", "r") as file:
        grid = file.read().split("\n")
        grid = [i.replace(",", "") for i in grid]

    # Converting for referencing as [row][col] as split by "/n" gives [col][row]
    new_grid = []
    for row in range(constants.MAP_SIZE[0]):
        new_grid.append([])
        for col in grid:
            new_grid[len(new_grid) - 1].append(col[row])

    return new_grid



class World:
    """ holds all the map tiles, be that a Tile or City, in a 2d-array """
    def __init__(self, map_name):  # __init__ creates new world
        self.format = get_world(map_name)

        # Make Tiles
        self.tiles = []
        for row in range(len(self.format[0])):  # assumes col 0, is same len as all others.
            self.tiles.append([])

            for col in range(len(self.format)):
                self.tiles[-1].append(Tile(self.format[row][col], [row, col]))


    def get_tile(self, position):
        return self.tiles[position[0]][position[1]]

    def get_format(self):
        return self.format
