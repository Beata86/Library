function addBook() {
    var authorInput = document.getElementById("author");
    var titleInput = document.getElementById("title");
    var addBookMessage = document.getElementById("addBookMessage");
    var params = {
        title: titleInput.value,
        author: authorInput.value
    };
    if (!params.title || !params.author) {
        addBookMessage.innerHTML = "Wprowadź wymagane dane";
        return;
    }
    $.ajax({
        url: window.location.origin + "/books",
        data: params,
        type: 'POST',
        success: function() {
            titleInput.value = '';
            authorInput.value = '';
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
    div.innerHTML = book.author + ", '" + book.title + "'";
    booksContainer.appendChild(div);
}

function removeBook() {
    var bookNumberInput = document.getElementById("bookNumberToRemove");
    if (!isPositiveInteger(bookNumberInput.value)) {
        document.getElementById("removeBookMessage").innerHTML = "Wpisz poprawny numer wypożyczenia";
        return;
    }
    var booksContainer = document.getElementById("books");
    var bookNumber = parseInt(bookNumberInput.value);
    if (bookNumber > booksContainer.childElementCount) {
        document.getElementById("removeBookMessage").innerHTML = "Nie ma takiego numeru wypożyczenia";
        return;
    }
    $.ajax({
        url: window.location.origin + "/books?bookNumber=" + bookNumberInput.value,
        type: 'DELETE',
        success: function() {
            bookNumberInput.value = '';
            document.getElementById("removeBookMessage").innerHTML = "Wypożyczenie zostało usunięte";
            loadBooks();
        }
    });
}

function isPositiveInteger(value) {
    return !isNaN(parseInt(value)) && Number.isInteger(parseFloat(value)) && parseInt(value) > 0
}
