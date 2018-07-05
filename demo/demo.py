from pprint import pprint

from src.core.parser import CharacterParser

char = CharacterParser("FaustVIII", "FromDeadToWorse")
print(char.account_name,char.character)
print('----')
pprint(char.get_items_dict())
print('----')
for slot in char.get_items_dict():
    items=char.get_items_dict()[slot]
    print([item.explicit_mods for item in items if item.explicit_mods])
    # print(slot, items, ', '.join(]))
