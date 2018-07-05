# POE Wrapper
A small library that handles Getting various data from the POE Profile page or API.

## Features 

- Get league info
- Get character's equipment & gear
- Get stash information
- Encode and decode tree data <> url payload

## Usage
```python
from pprint import pprint

from src.core.parser import CharacterParser

char = CharacterParser("FaustVIII", "FromDeadToWorse")
print(char.account_name,char.character)
print('----')
pprint(char.get_items_dict())
```

```
FaustVIII {'name': 'FromDeadToWorse', 'league': 'SSF Bestiary', 'classId': 3, 'ascendancyClass': 3, 'class': 'Necromancer', 'level': 92, 'experience': 2268730372, 'lastActive': True}
----
{'Amulet': [Wrath Locket],
 'Belt': [Bramble Harness],
 'BodyArmour': [Vis Mortis],
 'Boots': [Bones of Ullr],
 'Flask': [Chemist's Silver Flask of Adrenaline,
           Chemist's Stibnite Flask of Warding,
           Seething Divine Life Flask of Curing,
           Panicked Divine Mana Flask of Staunching,
           Seething Eternal Life Flask of Heat],
 'Gloves': [Southbound],
 'Helm': [Behemoth Glance],
 'Offhand': [Ahn's Heritage],
 'Offhand2': [Bitterdream],
 'Ring': [Pandemonium Knuckle],
 'Ring2': [Phoenix Loop],
 'Weapon': [Brightbeak],
 'Weapon2': [Tomahawk]}
```