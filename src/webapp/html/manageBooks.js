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
    $.get(url, displayBooks)

}

function displayBooks(books) {
    var booksContainer = document.getElementById("books");
    var node = document.createElement("div");
    node.innerHTML = "nic nie napisze";
    booksContainer.appendChild(node);
}