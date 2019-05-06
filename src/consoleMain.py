from src.library.Library import *

def printRentals(bookRentals):
    for rent in bookRentals:
        print(rent.getRentalInformation())

def addRental(library):
    print("Enter person number")
    personNumber = int(input())
    print("Enter book number")
    bookNumber = int(input())
    try:
        library.addBookRental(bookNumber, personNumber)
    except InvalidPersonNumberException as exception:
        print(exception)

def printPersons(persons):
    print("There are {} persons in the list".format(len(persons)))
    for x in range(len(persons)):
        print("{}. ".format(x + 1), end ='')
        print(persons[x].getMessage())

def removeRental(library):
    print("enter rental number")
    rentalNumber = int(input())
    library.removeRental(rentalNumber)

def removeBook(library):
    print("enter book number")
    bookNumber = int(input())
    try:
        library.removeBook(bookNumber)
    except InvalidBookNumberException as exception:
        print(exception)

#
# def printMeanOfTheAge(list):
#     adultPeople = 0
#     suma = 0
#     for x in range(len(list)):
#         if list[x].age >= 18:
#             suma = suma + list[x].age
#             adultPeople = adultPeople + 1
#     print(suma/adultPeople)
#


def printMenu():
    print("-----------------------------------------")
    print("Naciśnij 1, zeby dodac osobe")
    print("Naciśnij 2, zeby wyswietlic liste")
    print("Naciśnij 3, żeby usunac osobę")
    print("Naciśnij 4, zeby wyszukać osoby")
    print("Naciśnij 5, zeby wyjść")
    print("Naciśnij 6, zeby zapisać listę osób i ksiazek do pliku")
    print("Naciśnij 7, zeby odczytać zapisaną listę do pliku")
    print("Naciśnij 8, zeby dodac ksiazke")
    print("Nasisnij 9, zeby wyswietlic liste dodanych ksiazek")
    print("Naciśnij 10, zeby wyswietlic liste wypozyczen")
    print("Nacisnij 11, zeby dodac wypozyczenie")
    print("Nacisnij 12, zeby usunac wypozyczenie")
    print("Nacisnij 13, zeby usunac ksiazke")
    print("-----------------------------------------")

def addBook(library):
    print("Enter title")
    title = input()
    print("Enter author")
    author = input()
    library.addBook(title, author)


def showBooksList(books):
    for b in range(len(books)):
        print("{}. ".format(b + 1), end='')
        print(books[b].getDescription())


def addNewPerson(library):
    print("What is your name?")
    name = input()
    print("What is your surname?")
    surname = input()
    print("How old are you?")
    old = input()
    print("What is your sex?")
    gender = input()
    print("What is your height?")
    height = input()
    library.addPerson(name, surname, gender, old, height)

def saveToFile(library):
    print("Enter file name")
    name = input()
    file = open(name, "w")
    library.saveToFile(file)

def readFile(library):
    print("Enter file's name")
    filename = input()
    file = open(filename, "r")
    library.readFromFile(file)

library = Library()

library.addBook("Zywot szczeniecia", "Kalafior Bancerz")
library.addBook("Sztuka dziadostwa", "Grzegorz Stelmaczonek")

library.addPerson("Ewa", "Bancerz","woman", 6, 175)
library.addPerson("Beata", "Bancerz","woman", 18, 168)
library.addPerson("Grzegorz", "Stelmaczonek","man", 35, 179)
library.addPerson("Kris", "Lineham","man", 26, 183)
library.addPerson("Roman", "Bancerz","man", 60, 190)

library.addBookRental(1, 1)

while True:
    printMenu()
    choice = int(input())

    if choice == 1:
        addNewPerson(library)

    if choice == 2:
        printPersons(library.persons)

    if choice == 5:
        break

    if choice == 3:
        print("With person do you remove?:")
        number = int(input())
        try:
            library.removePerson(number)
        except InvalidPersonNumberException as exception:
            print(exception)

    if choice == 4:
        print("Write age From")
        ageFrom = int(input())
        print("Write age To")
        ageTo = int(input())
        print("Write height from")
        heightFrom = int(input())
        print("Write height to")
        heightTo = int(input())
        foundPersons = library.findPersons(ageFrom, ageTo, heightFrom, heightTo)
        printPersons(foundPersons)

    if choice == 6:
        saveToFile(library)

    if choice == 7:
        readFile(library)

    if choice == 8:
        addBook(library)

    if choice == 9:
        showBooksList(library.books)

    if choice == 10:
        printRentals(library.bookRentals)

    if choice == 11:
        addRental(library)

    if choice == 12:
        removeRental(library)

    if choice == 13:
        removeBook(library)