function addBook() {
    var author = document.getElementById("author").value;
    var title = document.getElementById("title").value;
    var url = window.location.origin + "/books";
    var params = {
        title: title,
        author: author
    };
    $.post(url, params);
}