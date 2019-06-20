from src.library.Book import Book
from src.library.Person import Person
from src.library.BookRental import BookRental
from src.library.InvalidPersonNumberException \
    import InvalidPersonNumberException
from src.library.InvalidBookNumberException \
    import InvalidBookNumberException
from src.library.BookInRentalException \
    import BookInRentalException
from src.library.PersonInRentalException \
    import PersonInRentalException


class Library():
    def __init__(self):
        self.books = []
        self.persons = []
        self.bookRentals = []

    def addPerson(self, name, surname, gender, age, height):
        person = Person(name, surname, gender, age, height)
        self.persons.append(person)

    def addBook(self, title, author, numberOfPages):
        book = Book(title, author, numberOfPages)
        self.books.append(book)

    def addBookRental(self, bookNumber, personNumber):
        if bookNumber > len(self.books) or bookNumber < 1:
            raise InvalidBookNumberException()
        if personNumber > len(self.persons) or personNumber < 1:
            raise InvalidPersonNumberException()
        person = self.persons[personNumber - 1]
        book = self.books[bookNumber - 1]
        rental = BookRental(person, book)
        self.bookRentals.append(rental)

    def removePerson(self, number):
        if number >= 1 and number <= len(self.persons):
            if self.isPersonInRental(self.persons[number - 1]):
                raise PersonInRentalException()
            del self.persons[number - 1]
            print("Person number {} removed".format(number))
        else:
            raise InvalidPersonNumberException()

    def findPersons(self, ageFrom, ageTo, heightFrom, heightTo):
        listOfFoundPersons = []
        for x in range(len(self.persons)):
            if self.persons[x].age >= ageFrom \
                    and self.persons[x].age <= ageTo \
                    and self.persons[x].height >= heightFrom \
                    and self.persons[x].height <= heightTo:
                listOfFoundPersons.append(self.persons[x])
        return listOfFoundPersons

    def findBooks(self, value):
        listOfFoundBooks = []
        for book in self.books:
            if value in book.title or value in book.author:
                listOfFoundBooks.append(book)
        return listOfFoundBooks

    def saveToFile(self, file):
        file.write(str(len(self.persons)))
        file.write("\n")
        for x in range(len(self.persons)):
            file.write(self.persons[x].name)
            file.write("\n")
            file.write(self.persons[x].surname)
            file.write("\n")
            file.write(str(self.persons[x].sex))
            file.write("\n")
            file.write(str(self.persons[x].age))
            file.write("\n")
            file.write(str(self.persons[x].height))
            file.write("\n")
        file.write(str(len(self.books)))
        file.write("\n")
        for x in range(len(self.books)):
            file.write(self.books[x].title)
            file.write("\n")
            file.write(self.books[x].author)
            file.write("\n")
        file.close()

    def readFromFile(self, file):
        self.persons.clear()
        numberOfPersons = int(file.readline())
        for x in range(numberOfPersons):
            name = file.readline().replace("\n", "")
            surname = file.readline().replace("\n", "")
            sex = file.readline().replace("\n", "")
            age = file.readline().replace("\n", "")
            height = file.readline().replace("\n", "")
            human = Person(name, surname, sex, age, height)
            self.persons.append(human)
        self.books.clear()
        numberOfBooks = int(file.readline())
        for x in range(numberOfBooks):
            title = file.readline().replace("\n", "")
            author = file.readline().replace("\n", "")
            book = Book(title, author)
            self.books.append(book)
        file.close()

    def removeRental(self, rentalNumber):
        if rentalNumber > len(self.bookRentals) or rentalNumber < 1:
            print("Rental does not exist")
            return
        del self.bookRentals[rentalNumber - 1]

    def removeBook(self, bookNumber):
        if bookNumber >= 1 and bookNumber <= len(self.books):
            if self.isBookInRental(self.books[bookNumber - 1]):
                raise BookInRentalException()
            del self.books[bookNumber - 1]
            print("Book number {} removed".format(bookNumber))
        else:
            raise InvalidBookNumberException()

    def isBookInRental(self, book):
        for rental in self.bookRentals:
            if rental.book == book:
                return True
        return False

    def isPersonInRental(self, person):
        for rental in self.bookRentals:
            if rental.person == person:
                return True
        return False
