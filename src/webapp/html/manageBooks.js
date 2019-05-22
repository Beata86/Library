function addBook() {
    var author = document.getElementById("author").value;
    var title = document.getElementById("title").value;
    var url = window.location.origin + "/books";
    var params = {
        title: title,
        author: author
    };
    $.post(url, params, loadBooks);
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
    div.innerHTML = book.author + " " + book.title;
    booksContainer.appendChild(div);
}