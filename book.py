class Book:
    def __init__(self, title):
        self.identifier = None  # The identifier will be generated automatically
        self.title = title
        self.available = True

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier

    def __str__(self):
        return f"Книга: {self.title}"
