from src.util.regex import strip_translation_prefix


class Item:
    def __init__(self, **kwargs):
        self.verified = kwargs.get('verified')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.ilvl = kwargs.get('ilvl')
        self.icon = kwargs.get('icon')
        self.league = kwargs.get('league')
        self.id = kwargs.get('id')
        # todo parse into own objects[group, attrib{s,d,i},sColour{R,G,B}
        self.sockets = kwargs.get('sockets')
        self.name = strip_translation_prefix(kwargs.get('name'))
        self.type = strip_translation_prefix(kwargs.get('type_line'))
        self.identified = kwargs.get('identified')
        # various properties such as quality names, values[], displayMode,type
        self.properties = kwargs.get('properties')
        self.requirements = kwargs.get('requirements')
        # string array
        self.explicit_mods = kwargs.get('explicit_mods')
        self.flavour_text = kwargs.get('flavour_text')
        self.frame_type = kwargs.get('frame_type')
        self.category = kwargs.get('category')
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.slot = kwargs.get('slot')
        # list of items
        self.socketed_items = kwargs.get('socketed_items')

    @staticmethod
    def from_dict(item_dict):
        item = Item(
            verified=item_dict.get('verified'),
            width=item_dict.get('w'),
            height=item_dict.get('h'),
            ilvl=item_dict.get('ilvl'),
            icon=item_dict.get('icon'),
            league=item_dict.get('league'),
            id=item_dict.get('id'),
            sockets=item_dict.get('sockets'),
            name=item_dict.get('name'),
            type_line=item_dict.get('typeLine'),
            identified=item_dict.get('identified'),
            properties=item_dict.get('properties'),
            requirements=item_dict.get('requirements'),
            explicit_mods=item_dict.get('explicitMods'),
            flavour_text=item_dict.get('flavourText'),
            frame_type=item_dict.get('frameType'),
            category=item_dict.get('category'),
            x=item_dict.get('x'),
            y=item_dict.get('y'),
            slot=item_dict.get('inventoryId'),
            socketed_items=item_dict.get('socketedItems'),
        )
        return item

    def __repr__(self):
        return self.name if self.slot != 'Flask' and self.slot != 'MainInventory' and self.frame_type != 0 else self.type
