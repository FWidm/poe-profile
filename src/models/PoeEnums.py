from enum import Enum


class CharacterKeys(Enum):
    HASHES = 'hashes'
    ITEMS = 'items'
    JEWEL_SLOTS = 'jewel_slots'
    CHARACTER = 'character'
    JEWELS ='jewels'


class CharacterFieldKeys(Enum):
    """
    This class describes all keys that are returned from querying the char from a profile under the
    'character' key.
    """
    ASCENDENCY_CLASS_ID = 'ascendancyClass'
    CLASS_ID = 'classId'
    CLASS = 'class'
    LEAGUE = 'league'
    NAME = 'name'
    LAST_ACTIVE = 'lastActive'
    LEVEL = 'level'
    EXP = 'experience'
