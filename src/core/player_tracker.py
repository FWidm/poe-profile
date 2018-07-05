
import copy


from src.core.parser import CharacterParser


class PlayerTracker():
    def __init__(self):
        self.char_parsers = []
        self.snapshots = {}

    def add_character(self, account: str, character: str):
        self.char_parsers.append(CharacterParser(account, character))
        print(self.char_parsers)

    def remove_character(self, account: str, character: str):
        parser = next(filter(lambda parser: parser.account_name == account and parser.character_name == character,
                             self.char_parsers))
        self.char_parsers.remove(parser)

    def fetch_chars(self):
        for parser in self.char_parsers:
            self.fetch_char(parser)

    def fetch_char(self, parser: CharacterParser):
        parser.update()
        snapshot_list = self.snapshots.get(parser.character_name)
        if not snapshot_list:
            self.snapshots[parser.character_name] = []
        self.snapshots[parser.character_name].append(copy.deepcopy(parser))