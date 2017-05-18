class Event:
    def __init__(self, id, description=None):
        self._id = id
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
