class Task:
    def __init__(self, title: str, desc: str, priority: int):
        self.title: str = title
        self.desc = desc
        self.priority = priority

    def to_dict(self):
        return self.__dict__
