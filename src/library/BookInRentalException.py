class BookInRentalException(Exception):
    def __init__(self):
        super().__init__("Book in rental")
