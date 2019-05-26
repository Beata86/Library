import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_ManageBooks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000/cleanup")
        self.driver.get("http://localhost:5000/html/manageBooks.html")
        self.expectedBooks = [
            "Eileen Ormsby, 'Darknet'",
            "Marek Krajewski, 'Dziewczyna o czterech palcach'",
            "Katarzyna Gacek, '\"W\" jak morderstwo'",
            "Maciej Wasielewski, 'Niewidzialna Ręka'",
            "Robert Małecki, 'Wada'"
        ]

    def tearDown(self):
        self.driver.quit()

    # success cases
    def test_shouldDisplayBooks(self):
        assert "Książki" in self.driver.title
        self.verifyExpectedBooks()

    def test_shouldAddBook(self):
        self.driver.find_element_by_id("author").send_keys("Łukasz Orbitowski")
        self.driver.find_element_by_id("title").send_keys("Kult")
        self.driver.find_element_by_id("addBookButton").click()
        self.expectedBooks.append("Łukasz Orbitowski, 'Kult'")
        self.verifyExpectedBooks()
        self.assertEqual("Książka została dodana", self.driver.find_element_by_id("addBookMessage").text)
        self.assertEqual("", self.driver.find_element_by_id("author").text)
        self.assertEqual("", self.driver.find_element_by_id("title").text)

    def test_shouldRemoveBook(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("5")
        self.driver.find_element_by_id("removeBookButton").click()
        del self.expectedBooks[4]
        self.verifyExpectedBooks()
        self.assertEqual("Książka została usunięta", self.driver.find_element_by_id("removeBookMessage").text)

    # add book - fail cases
    def test_shouldNotAddBookWithoutAnAuthor(self):
        self.driver.find_element_by_id("title").send_keys("Kult")
        self.driver.find_element_by_id("addBookButton").click()
        self.assertEqual("Wprowadź wymagane dane", self.driver.find_element_by_id("addBookMessage").text)
        self.verifyExpectedBooks()

    def test_shouldNotAddBookWithoutATitle(self):
        self.driver.find_element_by_id("author").send_keys("Łukasz Orbitowski")
        self.driver.find_element_by_id("addBookButton").click()
        self.assertEqual("Wprowadź wymagane dane", self.driver.find_element_by_id("addBookMessage").text)
        self.verifyExpectedBooks()

    # remove book - book number format fail cases
    def test_shouldNotRemoveBookWithFloatingPointNumber(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("5.5")
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Wpisz poprawny numer książki", self.driver.find_element_by_id("removeBookMessage").text)

    def test_shouldNotRemoveBookWithoutANumber(self):
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Wpisz poprawny numer książki", self.driver.find_element_by_id("removeBookMessage").text)

    def test_bookNumberFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("test")
        self.assertEqual("", self.driver.find_element_by_id("bookNumberToRemove").text)

    # remove book - book number range fail cases
    def test_shouldNotRemoveBookWithNegativeNumber(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("-1")
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Wpisz poprawny numer książki", self.driver.find_element_by_id("removeBookMessage").text)

    def test_shouldNotRemoveBookNumberZero(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("0")
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Wpisz poprawny numer książki", self.driver.find_element_by_id("removeBookMessage").text)

    def test_shouldNotRemoveBookThatDoesNotExist(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("100")
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Nie ma takiego numeru książki", self.driver.find_element_by_id("removeBookMessage").text)

    def test_shouldNotRemoveBookInRental(self):
        self.driver.find_element_by_id("bookNumberToRemove").send_keys("3")
        self.driver.find_element_by_id("removeBookButton").click()
        self.verifyExpectedBooks()
        self.assertEqual("Książka jest aktualnie w wypożyczeniu", self.driver.find_element_by_id("removeBookMessage").text)

    def verifyExpectedBooks(self):
        books = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='books']/*")))
        self.assertEqual(len(self.expectedBooks), len(books))
        for i in range(len(books)):
            self.assertEqual(self.expectedBooks[i], books[i].text)