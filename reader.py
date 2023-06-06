class Reader:
    def __init__(self, name):
        self.identifier = None  # The identifier will be generated automatically
        self.name = name

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier

    def __str__(self):
        return f"Читач: {self.name}"