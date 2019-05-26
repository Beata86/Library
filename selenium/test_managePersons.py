import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_ManagePersons(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000/cleanup")
        self.driver.get("http://localhost:5000/html/managePersons.html")
        self.expectedPersons = [
            "Ewa Kisiel, płeć: kobieta, wiek: 26, wzrost: 170",
            "Rafał Kowalski, płeć: mężczyzna, wiek: 38, wzrost: 180",
            "Wiesław Paleta, płeć: mężczyzna, wiek: 35, wzrost: 179",
            "Elżbieta Domagała, płeć: kobieta, wiek: 45, wzrost: 165",
            "Jan Wiśniewski, płeć: mężczyzna, wiek: 60, wzrost: 184"
        ]

    def tearDown(self):
        self.driver.quit()

    # success cases
    def test_shouldDisplayPersons(self):
        self.assertEqual("Osoby", self.driver.title)
        self.verifyExpectedPersons()

    def test_shouldAddPerson(self):
        self.driver.find_element_by_id("name").send_keys("Andrzej")
        self.driver.find_element_by_id("surname").send_keys("Leszczyński")
        self.driver.find_element_by_id("gender").send_keys("mężczyzna")
        self.driver.find_element_by_id("height").send_keys("175")
        self.driver.find_element_by_id("age").send_keys("80")

        self.driver.find_element_by_id("addPersonButton").click()
        self.expectedPersons.append("Andrzej Leszczyński, płeć: mężczyzna, wiek: 80, wzrost: 175")
        self.verifyExpectedPersons()
        self.assertEqual("Osoba została dodana", self.driver.find_element_by_id("addPersonMessage").text)
        self.assertEqual("", self.driver.find_element_by_id("name").text)
        self.assertEqual("", self.driver.find_element_by_id("surname").text)
        self.assertEqual("", self.driver.find_element_by_id("gender").text)
        self.assertEqual("", self.driver.find_element_by_id("height").text)
        self.assertEqual("", self.driver.find_element_by_id("age").text)

    def test_shouldRemovePerson(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("2")
        self.driver.find_element_by_id("removePersonButton").click()
        del self.expectedPersons[1]
        self.verifyExpectedPersons()
        self.assertEqual("Osoba została usunięta", self.driver.find_element_by_id("removePersonMessage").text)
        self.assertEqual("", self.driver.find_element_by_id("personNumberToRemove").text)

    # remove person - person number format fail cases
    def test_shouldNotRemovePersonWithNegativeNumber(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("-1")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Nie ma takiego numeru osoby", self.driver.find_element_by_id("removePersonMessage").text)

    def test_shouldNotRemovePersonWithNumberZero(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("0")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Nie ma takiego numeru osoby", self.driver.find_element_by_id("removePersonMessage").text)

    def test_shouldNotRemovePersonThatDoesNotExist(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("100")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Nie ma takiego numeru osoby", self.driver.find_element_by_id("removePersonMessage").text)

    def test_personNumberFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("tekst")
        self.assertEqual("", self.driver.find_element_by_id("personNumberToRemove").text)

    def test_shouldNotRemovePersonWithFloatingPointNumber(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("2.3")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Wpisz poprawny numer osoby", self.driver.find_element_by_id("removePersonMessage").text)

    def test_shouldNotRemovePersonInRental(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("1")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Osoba aktualnie wypożycza książkę",
                         self.driver.find_element_by_id("removePersonMessage").text)

    def test_shouldNotRemovePersonWithEmptyFieldNumber(self):
        self.driver.find_element_by_id("personNumberToRemove").send_keys("")
        self.driver.find_element_by_id("removePersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Wpisz poprawny numer osoby", self.driver.find_element_by_id("removePersonMessage").text)

    # add person - fail cases
    def test_shouldNotAddPersonWithoutHeightAndAge(self):
        self.driver.find_element_by_id("name").send_keys("Andrzej")
        self.driver.find_element_by_id("surname").send_keys("Leszczyński")
        self.driver.find_element_by_id("gender").send_keys("mężczyzna")
        self.driver.find_element_by_id("height").send_keys("")
        self.driver.find_element_by_id("age").send_keys("")
        self.driver.find_element_by_id("addPersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Wprowadź wymagane dane", self.driver.find_element_by_id("addPersonMessage").text)

    def test_shouldNotAddPersonWithFloatingPointHeight(self):
        self.driver.find_element_by_id("name").send_keys("Andrzej")
        self.driver.find_element_by_id("surname").send_keys("Leszczyński")
        self.driver.find_element_by_id("gender").send_keys("mężczyzna")
        self.driver.find_element_by_id("height").send_keys("175.5")
        self.driver.find_element_by_id("age").send_keys("80")
        self.driver.find_element_by_id("addPersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addPersonMessage").text)

    def test_personHeightFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("height").send_keys("tekst")
        self.assertEqual("", self.driver.find_element_by_id("height").text)

    def test_shouldNotAddPersonWithFloatingPointAge(self):
        self.driver.find_element_by_id("name").send_keys("Andrzej")
        self.driver.find_element_by_id("surname").send_keys("Leszczyński")
        self.driver.find_element_by_id("gender").send_keys("mężczyzna")
        self.driver.find_element_by_id("height").send_keys("175")
        self.driver.find_element_by_id("age").send_keys("12.5")
        self.driver.find_element_by_id("addPersonButton").click()
        self.verifyExpectedPersons()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addPersonMessage").text)

    def test_personAgeFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("age").send_keys("tekst")
        self.assertEqual("", self.driver.find_element_by_id("age").text)

    def verifyExpectedPersons(self):
        persons = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='persons']/*")))
        self.assertEqual(len(self.expectedPersons), len(persons))
        for i in range(len(persons)):
            self.assertEqual(self.expectedPersons[i], persons[i].text)


