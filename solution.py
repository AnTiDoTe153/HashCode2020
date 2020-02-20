
class Book:

    def __init__(self, id, score):
        self.id = id
        self.score = score


class Library:

    def __init__(self, books, registrationTime, booksPerDay):
        self.books = books
        self.registrationTime = registrationTime
        self.booksPerDay = booksPerDay
        self.booksNumber = len(books)



def main():
    print('Put solution here')



if __name__ == '__main__':
    main()