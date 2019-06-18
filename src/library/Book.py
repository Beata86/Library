class Book():
    def __init__(self, title, author, numberOfPages):
        self.title = title
        self.author = author
        self.numberOfPages = numberOfPages

    def getAuthorAndBookTitle(self):
        return self.author + " " + self.title + ", number of pages: " \
               + str(self.numberOfPages)

    def getDescription(self):
        return "Book title: {}, book author: {}, number of pages: {}"\
            .format(self.title, self.author, self.numberOfPages)
