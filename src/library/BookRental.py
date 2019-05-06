class BookRental():
    def __init__(self, person, book):
        self.person = person
        self.book = book

    def getRentalInformation(self):
        return "Book: {}, rented by person: {}".format(self.book.getAuthorAndBookTitle(), self.person.getFullName())


