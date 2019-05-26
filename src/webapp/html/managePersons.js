function addPerson() {
    var nameInput = document.getElementById("name");
    var surnameInput = document.getElementById("surname");
    var genderInput = document.getElementById("gender");
    var ageInput = document.getElementById("age");
    var heightInput = document.getElementById("height");
    var messageInput = document.getElementById("addPersonMessage");
    var params = {
        name: nameInput.value,
        surname: surnameInput.value,
        gender: genderInput.value,
        age: ageInput.value,
        height: heightInput.value
    };
    if (!params.name || !params.surname || !params.gender || !params.age || !params.height) {
        messageInput.innerHTML = "Wprowadź wymagane dane";
        return;
    }
    if (!isPositiveInteger(params.age) || !isPositiveInteger(params.height)) {
        messageInput.innerHTML = "Wprowadź dodatanią liczbę całkowitą";
        return;
    }

    $.ajax({
        url: window.location.origin + "/persons",
        data: params,
        type: 'POST',
        success: function() {
            messageInput.innerHTML = '';
            nameInput.value = '';
            surnameInput.value = '';
            genderInput.value = '';
            ageInput.value = '';
            heightInput.value = '';
            messageInput.innerHTML = 'Osoba została dodana';
            loadPersons();
        }
    });
}

function loadPersons() {
    var url = window.location.origin + "/persons";
    $.getJSON(url, displayPersons)
}

function displayPersons(persons) {
    var personsContainer = document.getElementById("persons");
    personsContainer.innerHTML = "";
    persons.forEach(displayPerson);
}

function displayPerson(person) {
    var personsContainer = document.getElementById("persons");
    var div = document.createElement("li");
    div.innerHTML = person.name + " " + person.surname + ", płeć: " + person.gender + ', wiek: ' + person.age + ", wzrost: " + person.height;
    personsContainer.appendChild(div);
}

function removePerson() {
    var personNumberInput = document.getElementById("personNumberToRemove");
    if (isNaN(parseInt(personNumberInput.value)) || !Number.isInteger(parseFloat(personNumberInput.value))) {
        document.getElementById("removePersonMessage").innerHTML = "Wpisz poprawny numer osoby";
        return;
    }
    var personsContainer = document.getElementById("persons");
    var personNumber = parseInt(personNumberInput.value);
    if (personNumber < 1 || personNumber > personsContainer.childElementCount) {
        document.getElementById("removePersonMessage").innerHTML = "Nie ma takiego numeru osoby";
        return;
    }
    $.ajax({
        url: window.location.origin + "/persons?personNumber=" + personNumberInput.value,
        type: 'DELETE',
        success: function() {
            personNumberInput.value = '';
            document.getElementById("removePersonMessage").innerHTML = "Osoba została usunięta";
            loadPersons();
        },
        error: function(response) {
            document.getElementById("removePersonMessage").innerHTML = response.responseText;
        }
    });
}

function isPositiveInteger(value) {
    return !isNaN(parseInt(value)) && Number.isInteger(parseFloat(value)) && parseInt(value) > 0
}