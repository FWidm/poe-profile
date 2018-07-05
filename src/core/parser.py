from datetime import datetime

from src.core.poe_requests import PoeRequests
from src.models.item import Item
from src.util import tree_codec
from src.models.PoeEnums import CharacterFieldKeys, CharacterKeys


class CharacterParser():
    def __init__(self, account_name: str, character_name: str, session_id: str = None):
        self.poe_requests = PoeRequests(session_id)
        self.account_name = account_name
        self.character_name =character_name
        self.timestamp = datetime.now()
        self.update()

    def update(self):
        raw_character = self.poe_requests.get_char_info(self.account_name, self.character_name)
        self.tree_payload = self.__parse_payload(raw_character)
        self.items, self.jewels = self.__parse_items(raw_character)
        self.character = raw_character[CharacterKeys.CHARACTER.value]
        self.timestamp = datetime.now()


    def __repr__(self):
        return "{}".format(self.__dict__)

    @staticmethod
    def __parse_items(raw_character):
        jewels = raw_character[CharacterKeys.JEWELS.value]
        raw_items = raw_character[CharacterKeys.ITEMS.value]
        item_list = []
        jewel_list = []
        for item in raw_items:
            item_list.append(Item.from_dict(item))
            # find socketed jewels
        for jewel in jewels:
            jewel_list.append(Item.from_dict(jewel))
        return item_list, jewel_list

    @staticmethod
    def __parse_payload(raw_character):
        char = raw_character[CharacterKeys.CHARACTER.value]
        hashes = raw_character[CharacterKeys.HASHES.value]
        return tree_codec.encode_hashes(4, char[CharacterFieldKeys.CLASS_ID.value],
                                        char[CharacterFieldKeys.ASCENDENCY_CLASS_ID.value], 0, hashes)

    def get_items_dict(self)->dict:
        item_dict = {}
        for item in self.items:
            if not item_dict.get(item.slot):
                item_dict[item.slot]=[]
            item_dict[item.slot].append(item)
        return item_dict

    def get_hash(self)->str:
        pass