import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_ManageRentals(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000/cleanup")
        self.driver.get("http://localhost:5000/html/manageRentals.html")
        self.expectedRentals = [
            "Wiesław Paleta - Eileen Ormsby, 'Darknet'",
            "Ewa Kisiel - Marek Krajewski, 'Dziewczyna o czterech palcach'",
            "Elżbieta Domagała - Katarzyna Gacek, '\"W\" jak morderstwo'",
            "Jan Wiśniewski - Maciej Wasielewski, 'Niewidzialna Ręka'",
            "Wiesław Paleta - Maciej Wasielewski, 'Niewidzialna Ręka'"
        ]

    def tearDown(self):
        self.driver.quit()

    # success cases
    def test_shouldDisplayRentals(self):
        self.assertEqual("Wypożyczenia", self.driver.title)
        self.verifyExpectedRentals()

    def test_shouldAddRental(self):
        self.driver.find_element_by_id("personNumber").send_keys("1")
        self.driver.find_element_by_id("bookNumber").send_keys("1")

        self.driver.find_element_by_id("addRentalButton").click()
        self.expectedRentals.append("Ewa Kisiel - Eileen Ormsby, 'Darknet'")
        self.verifyExpectedRentals()
        self.assertEqual("Wypożyczenie zostało dodane", self.driver.find_element_by_id("addRentalMessage").text)
        self.assertEqual("", self.driver.find_element_by_id("personNumber").text)
        self.assertEqual("", self.driver.find_element_by_id("bookNumber").text)

    def test_shouldRemoveRental(self):
        self.driver.find_element_by_id("rentalNumberToRemove").send_keys("1")
        self.driver.find_element_by_id("removeRentalButton").click()
        del self.expectedRentals[0]
        self.verifyExpectedRentals()
        self.assertEqual("Wypożyczenie zostało usunięte", self.driver.find_element_by_id("removeRentalMessage").text)
        self.assertEqual("", self.driver.find_element_by_id("rentalNumberToRemove").text)

    # add rental - rental number format fail cases
    def test_shouldNotAddRentalWithFloatingPointPersonNumber(self):
        self.driver.find_element_by_id("personNumber").send_keys("1.5")
        self.driver.find_element_by_id("bookNumber").send_keys("1")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addRentalMessage").text)

    def test_shouldNotAddRentalWithFloatingPointBookNumber(self):
        self.driver.find_element_by_id("personNumber").send_keys("1")
        self.driver.find_element_by_id("bookNumber").send_keys("2.3")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addRentalMessage").text)


    def test_shouldNotAddRentalWithNegativeBookNumber(self):
        self.driver.find_element_by_id("personNumber").send_keys("1")
        self.driver.find_element_by_id("bookNumber").send_keys("-2")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addRentalMessage").text)

    def test_shouldNotAddRentalWithNegativePersonNumber(self):
        self.driver.find_element_by_id("personNumber").send_keys("-1")
        self.driver.find_element_by_id("bookNumber").send_keys("2")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź dodatanią liczbę całkowitą", self.driver.find_element_by_id("addRentalMessage").text)

    def test_shouldNotAddRentalWithoutABookNumber(self):
        self.driver.find_element_by_id("personNumber").send_keys("1")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź wymagane dane", self.driver.find_element_by_id("addRentalMessage").text)

    def test_shouldNotAddRentalWithoutAPersonNumber(self):
        self.driver.find_element_by_id("bookNumber").send_keys("1")
        self.driver.find_element_by_id("addRentalButton").click()
        self.verifyExpectedRentals()
        self.assertEqual("Wprowadź wymagane dane", self.driver.find_element_by_id("addRentalMessage").text)

    def test_personNumberFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("personNumber").send_keys("tekst")
        self.assertEqual("", self.driver.find_element_by_id("personNumber").text)

    def test_bookNumberFieldShouldNotAcceptText(self):
        self.driver.find_element_by_id("bookNumber").send_keys("tekst")
        self.assertEqual("", self.driver.find_element_by_id("bookNumber").text)

    def verifyExpectedRentals(self):
        rentals = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='rentals']/*")))
        self.assertEqual(len(self.expectedRentals), len(rentals))
        for i in range(len(rentals)):
            self.assertEqual(self.expectedRentals[i], rentals[i].text)
