function addRental() {
    var bookNumberInput = document.getElementById("bookNumber");
    var personNumberInput = document.getElementById("personNumber");
    var messageInput = document.getElementById("addRentalMessage");
    var params = {
        bookNumber: bookNumberInput.value,
        personNumber: personNumberInput.value
    };
    if (!params.bookNumber || !params.personNumber) {
        messageInput.innerHTML = "Wprowadź wymagane dane";
        return;
    }
    if (!isPositiveInteger(params.bookNumber) || !isPositiveInteger(params.personNumber)) {
        messageInput.innerHTML = "Wprowadź dodatanią liczbę całkowitą";
        return;
    }
    $.ajax({
        url: window.location.origin + "/rentals",
        data: params,
        type: 'POST',
        success: function() {
            bookNumberInput.value = '';
            personNumberInput.value = '';
            messageInput.innerHTML = 'Wypożyczenie zostało dodane';
            loadRentals();
        },
        error: function(response) {
            messageInput.innerHTML = response.responseText;
        }
    });
}

function loadRentals() {
    var url = window.location.origin + "/rentals";
    $.getJSON(url, displayRentals)
}

function displayRentals(rentals) {
    var rentalsContainer = document.getElementById("rentals");
    rentalsContainer.innerHTML = "";
    rentals.forEach(displayRental);
}

function displayRental(rental) {
    var rentalsContainer = document.getElementById("rentals");
    var div = document.createElement("li");
    div.innerHTML = rental.person.name + " " + rental.person.surname + " - " + rental.book.author + ", '" + rental.book.title + "'";
    rentalsContainer.appendChild(div);
}

function removeRental() {
    var rentalNumberInput = document.getElementById("rentalNumberToRemove");
    if (!isPositiveInteger(rentalNumberInput.value)) {
        document.getElementById("removeRentalMessage").innerHTML = "Wpisz poprawny numer wypożyczenia";
        return;
    }
    var rentalsContainer = document.getElementById("rentals");
    var rentalNumber = parseInt(rentalNumberInput.value);
    if (rentalNumber > rentalsContainer.childElementCount) {
        document.getElementById("removeRentalMessage").innerHTML = "Nie ma takiego numeru wypożyczenia";
        return;
    }
    $.ajax({
        url: window.location.origin + "/rentals?rentalNumber=" + rentalNumberInput.value,
        type: 'DELETE',
        success: function() {
            rentalNumberInput.value = '';
            document.getElementById("removeRentalMessage").innerHTML = "Wypożyczenie zostało usunięte";
            loadRentals();
        }
    });
}

function isPositiveInteger(value) {
    return !isNaN(parseInt(value)) && Number.isInteger(parseFloat(value)) && parseInt(value) > 0
}
