class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getAuthorAndBookTitle(self):
        return self.author + " " + self.title

    def getDescription(self):
        return "Book title : {}, book author: {}".format(self.title, self.author)
