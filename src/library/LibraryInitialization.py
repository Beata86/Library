

def initializeLibrary(library):
    library.addBook("Darknet", "Eileen Ormsby")
    library.addBook("Dziewczyna o czterech palcach", "Marek Krajewski")
    library.addBook("\"W\" jak morderstwo", "Katarzyna Gacek")
    library.addBook("Niewidzialna Ręka", "Maciej Wasielewski")
    library.addBook("Wada", "Robert Małecki")

    library.addPerson("Ewa", "Kisiel", "kobieta", 26, 170)
    library.addPerson("Rafał", "Kowalski", "mężczyzna", 38, 180)
    library.addPerson("Wiesław", "Paleta", "mężczyzna", 35, 179)
    library.addPerson("Elżbieta", "Domagała", "kobieta", 45, 165)
    library.addPerson("Jan", "Wiśniewski", "mężczyzna", 60, 184)

    library.addBookRental(1, 3)
    library.addBookRental(2, 1)
    library.addBookRental(3, 4)
    library.addBookRental(4, 5)
    library.addBookRental(4, 3)
