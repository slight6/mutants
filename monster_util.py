""" This module contains the Monster class and associated functions. """

__author__ = 'Jason Consiglio'
__date__ = '10/10/2018'

import sys
import logging
import pathlib
import csv
import random
from game_util import log_output as log


monster_names = monster_names = (
    "Goblin", "Orc", "Troll", "Dragon", "Giant", "Golem", "Ghoul", "Ghost", "Vampire", 
    "Werewolf", "Zombie", "Skeleton", "Wraith", "Wight", "Lich", "Mummy", "Specter", 
    "Banshee", "Harpy", "Chimera", "Minotaur", "Cyclops", "Medusa", "Griffin", 
    "Basilisk", "Hydra", "Siren", "Gorgon", "Kraken", "Succubus", "Incubus", 
    "Changeling", "Imp", "Satyr", "Centaur", "Nymph", "Ogre", "Slime", 
    "Spectral Hound", "Shadow Beast", "Lycanthrope", "Wendigo", "Demogorgon", 
    "Spectral Knight", "Manticore", "Spectral Mage", "Gargoyle", "Phantom", 
    "Reaper", "Cerberus", "Djinn", "Ghoulish Specter", "Warlock", "Nightstalker", 
    "Elder Vampire", "Elemental", "Living Armor", "Witch", "Warlord", "Behemoth", 
    "Infernal Fiend", "Chimera Lord", "Spectral Warrior", "Necromancer", 
    "Shadowmancer", "Dark Priest", "Nightshade", "Abyssal Horror", "Serpent King", 
    "Soul Devourer", "Ghostly King", "Sylph", "Archdemon", "Dark Lord", 
    "Plaguebringer", "Death Knight", "Lurking Terror", "Abomination", 
    "Corpse Eater", "Spectral Sorcerer", "Grave Warden", "Abyssal Behemoth", 
    "Eldritch Aberration", "Cursed Phantom", "Dread Banshee", "Malevolent Djinn", 
    "Fallen Angel", "Enraged Gorgon", "Corrupted Elemental", "Demonic Warlord", 
    "Ancient Dragon", "Twisted Chimera", "Soulless Reaper", "Harbinger of Doom", 
    "Undying Lich", "Nightmare Incarnate", "Voidspawn", "Eldritch Horror", 
    "Shadow God", "Primordial Chaos"
)

creature_adjectives = (
    "Abyssal", "Ancient", "Arcane", "Armored", "Blighted", "Celestial", "Chaos", "Cursed", 
    "Dark", "Demonic", "Dire", "Dread", "Eldritch", "Enchanted", "Ethereal", "Ferocious", 
    "Fiery", "Frost", "Ghostly", "Giant", "Grim", "Haunting", "Hellish", "Horrifying", 
    "Immortal", "Infernal", "Lethal", "Malevolent", "Mystic", "Necrotic", "Noxious", 
    "Ominous", "Petrified", "Plague", "Primeval", "Pristine", "Radiant", "Revenant", 
    "Savage", "Shadow", "Skeletal", "Sorcerer's", "Spectral", "Steel", "Twisted", 
    "Unholy", "Vengeful", "Venomous", "Vicious", "Vile", "Wicked", "Winged", "Wretched", 
    "Aberrant", "Abyssal", "Accursed", "Adamantine", "Blazing", "Blizzard", "Blighted", 
    "Crimson", "Cryptic", "Cursed", "Demonic", "Dreadful", "Ebon", "Eldritch", "Enchanted", 
    "Eternal", "Fearsome", "Flaming", "Forsaken", "Frigid", "Ghastly", "Gigantic", "Grim", 
    "Harbinger", "Haunted", "Infernal", "Maleficent", "Mystic", "Nether", "Nightmarish", 
    "Onyx", "Pernicious", "Plague-ridden", "Raging", "Relentless", "Searing", "Serpentine", 
    "Sinister", "Sorcerous", "Spectral", "Thundering", "Twisted", "Unearthly", "Vengeful", 
    "Venomous", "Vorpal", "Whispering", "Wretched"
)


class Monster:
    def __init__(self):
        self.name = monster_names[random.randint(0, len(monster_names) - 1)]
        self.health = random.randint(1, 100)
        self.attack = random.randint(1, 100)
        self.defense = random.randint(1, 100)
        self.speed = random.randint(1, 100)
        self.magic = random.randint(1, 100)
        self.gold = random.randint(1, 100)
        self.experience = random.randint(1, 100)
        self.level = random.randint(1, 100)
    

def create_monster():
    """ Creates a new monster.
        Args:
            None
        Returns:
            monster (Monster): A new monster.
    """
    
    return Monster()

    pass
