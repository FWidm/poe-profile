class Character:
    def __init__(self, name, league, classId, ascendency_class, className, level, exp, last_active):
        self.name = name
        self.league = league
        self.classId = classId
        self.ascendency_class = ascendency_class
        self.className = className
        self.level = level
        self.experience = exp
        self.last_active = last_active

    def __repr__(self):
        return "{}".format(self.__dict__)
    @staticmethod
    def from_dict(dict):
        return Character(dict.get('name'), dict.get('league'), dict.get('classId'), dict.get('ascendencyClass'),
                         dict.get('class'), dict.get('level'), dict.get('experience'), dict.get('lastActive', False))

