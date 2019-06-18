import unittest
from src.library.InvalidBookNumberException import InvalidBookNumberException
from src.library.InvalidPersonNumberException \
    import InvalidPersonNumberException
from src.library.BookInRentalException import BookInRentalException
from src.library.PersonInRentalException import PersonInRentalException
from src.library.Library import Library


class Test_Library(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_libraryAddPerson(self):
        self.assertEqual(0, len(self.library.persons))
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        numberOfPersons = len(self.library.persons)
        self.assertEqual(1, numberOfPersons)
        person = self.library.persons[0]
        self.assertEqual("Joanna", person.name)
        self.assertEqual("Kowalska", person.surname)
        self.assertEqual("woman", person.sex)
        self.assertEqual(33, person.age)
        self.assertEqual(168, person.height)

    def test_libraryAddBook(self):
        self.assertEqual(0, len(self.library.books))
        self.library.addBook("Nazwa ksiazki", "autor", 200)
        numberOfBooks = len(self.library.books)
        self.assertEqual(1, numberOfBooks)
        book = self.library.books[0]
        self.assertEqual("Nazwa ksiazki", book.title)
        self.assertEqual("autor", book.author)
        self.assertEqual(200, book.numberOfPages)

    def test_libraryRemovePerson(self):
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        self.library.addPerson("Ewa", "Kowalska", "woman", 33, 172)
        self.library.removePerson(1)
        self.assertEqual(1, len(self.library.persons))
        person = self.library.persons[0]
        self.assertEqual("Ewa", person.name)

    def test_addBookRental(self):
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        self.library.addBook("Nazwa ksiazki", "autor", 0)
        self.library.addBookRental(1, 1)
        numberOfRentals = len(self.library.bookRentals)
        self.assertEqual(1, numberOfRentals)
        bookRental = self.library.bookRentals[0]
        surname = bookRental.person.surname
        self.assertEqual("Kowalska", surname)
        author = bookRental.book.author
        self.assertEqual("autor", author)

    def test_findPersons(self):
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        self.library.addPerson("Wiesław", "Paleta", "man", 35, 174)
        self.library.addPerson("Ela", "Pajor", "woman", 62, 170)
        foundPersons = self.library.findPersons(30, 40, 170, 175)
        self.assertEqual(1, len(foundPersons))
        self.assertEqual("Wiesław", foundPersons[0].name)

    def test_removePersonShouldRaiseExceptionWhenNumberTooLow(self):
        try:
            self.library.removePerson(0)
            self.fail("Exception Expected")
        except InvalidPersonNumberException:
            pass

    def test_removePersonShouldRaiseExceptionWhenNumberTooHigh(self):
        try:
            self.library.removePerson(100)
            self.fail("Exception Expected")
        except InvalidPersonNumberException:
            pass

    def test_removeBookShouldRaiseExceptionWhenNumberTooLow(self):
        try:
            self.library.removeBook(0)
            self.fail("Exception Expected")
        except InvalidBookNumberException:
            pass

    def test_removeBookShouldRaiseExceptionWhenNumberTooHigh(self):
        try:
            self.library.removeBook(100)
            self.fail("Exception Expected")
        except InvalidBookNumberException:
            pass

    def test_addBookRentalShouldRaiseExceptionWhenPersonNumberTooLow(self):
        try:
            self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
            self.library.addBook("Nazwa ksiazki", "autor", 0)
            self.library.addBookRental(1, 0)
            self.fail("Exception Expected")
        except InvalidPersonNumberException:
            pass

    def test_addBookRentalShouldRaiseExceptionWhenPersonNumberTooHigh(self):
        try:
            self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
            self.library.addBook("Nazwa ksiazki", "autor", 0)
            self.library.addBookRental(1, 100)
            self.fail("Exception Expected")
        except InvalidPersonNumberException:
            pass

    def test_addBookRentalShouldRaiseExceptionWhenBookNumberTooLow(self):
        try:
            self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
            self.library.addBook("Nazwa ksiazki", "autor", 0)
            self.library.addBookRental(0, 1)
            self.fail("Exception Expected")
        except InvalidBookNumberException:
            pass

    def test_addBookRentalShouldRaiseExceptionWhenBookNumberTooHigh(self):
        try:
            self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
            self.library.addBook("Nazwa ksiazki", "autor", 0)
            self.library.addBookRental(100, 1)
            self.fail("Exception Expected")
        except InvalidBookNumberException:
            pass

    def test_shouldThrowExceptionWhenBookInRental(self):
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        self.library.addBook("Nazwa ksiazki", "autor", 0)
        self.library.addBookRental(1, 1)
        try:
            self.library.removeBook(1)
            self.fail("Exception Expected")
        except BookInRentalException:
            pass

    def test_shouldThrowExceptionWhenPersonInRental(self):
        self.library.addPerson("Joanna", "Kowalska", "woman", 33, 168)
        self.library.addBook("Nazwa ksiazki", "autor", 0)
        self.library.addBookRental(1, 1)
        try:
            self.library.removePerson(1)
            self.fail("Exception Expected")
        except PersonInRentalException:
            pass
