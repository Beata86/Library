class PersonInRentalException(Exception):
    def __init__(self):
        super().__init__("Person in rental")