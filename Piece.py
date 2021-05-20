class Piece:
    def __init__(self, type, ownership):
        self.type = type
        self.ownership = ownership

    def get_type(self):
        return self.type

    def get_ownership(self):
        return self.ownership
