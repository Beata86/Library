function findBooks() {
    var findBooksInput = document.getElementById("findBooks");
    var url = window.location.origin + "/books/find?value=" + findBooksInput.value;
    $.getJSON(url, displayBooks);
}

function addBook() {
    var authorInput = document.getElementById("author");
    var titleInput = document.getElementById("title");
    var numberOfPagesInput = document.getElementById("numberOfPages");
    var addBookMessage = document.getElementById("addBookMessage");
    var params = {
        title: titleInput.value,
        author: authorInput.value,
        numberOfPages: numberOfPages.value
    };
    if (!params.title || !params.author || !params.numberOfPages) {
        addBookMessage.innerHTML = "Wprowadź wymagane dane";
        return;
    }
    if (!isPositiveInteger(params.numberOfPages)) {
        addBookMessage.innerHTML = "Wprowadź poprawną liczbę stron";
        return;
    }
    $.ajax({
        url: window.location.origin + "/books",
        data: params,
        type: 'POST',
        success: function() {
            titleInput.value = '';
            authorInput.value = '';
            numberOfPages.value = '';
            addBookMessage.innerHTML = 'Książka została dodana';
            loadBooks();
        }
    });
}

function loadBooks() {
    var url = window.location.origin + "/books";
    $.getJSON(url, displayBooks)
}

function displayBooks(books) {
    var booksContainer = document.getElementById("books");
    booksContainer.innerHTML = "";
    books.forEach(displayBook);
}

function displayBook(book) {
    var booksContainer = document.getElementById("books");
    var div = document.createElement("li");
    div.innerHTML = book.author + ", '" + book.title + "', liczba stron: " + book.numberOfPages;
    booksContainer.appendChild(div);
}

function removeBook() {
    var bookNumberInput = document.getElementById("bookNumberToRemove");
    if (!isPositiveInteger(bookNumberInput.value)) {
        document.getElementById("removeBookMessage").innerHTML = "Wpisz poprawny numer książki";
        return;
    }
    var booksContainer = document.getElementById("books");
    var bookNumber = parseInt(bookNumberInput.value);
    if (bookNumber > booksContainer.childElementCount) {
        document.getElementById("removeBookMessage").innerHTML = "Nie ma takiego numeru książki";
        return;
    }
    $.ajax({
        url: window.location.origin + "/books?bookNumber=" + bookNumberInput.value,
        type: 'DELETE',
        success: function() {
            bookNumberInput.value = '';
            document.getElementById("removeBookMessage").innerHTML = "Książka została usunięta";
            loadBooks();
        },
        error: function(response) {
            document.getElementById("removeBookMessage").innerHTML = response.responseText;
        }
    });
}

function isPositiveInteger(value) {
    return !isNaN(parseInt(value)) && Number.isInteger(parseFloat(value)) && parseInt(value) > 0
}
