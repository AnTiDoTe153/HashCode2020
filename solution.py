import functools

class Book:

    def __init__(self, id, score):
        self.id = id
        self.score = score

class Library:

    def __init__(self, books, registrationTime, booksPerDay, id):
        self.books = books
        self.registrationTime = registrationTime
        self.booksPerDay = booksPerDay
        self.booksNumber = len(books)
        self.id = id


def parseFile(filePath):
    global B, L, D
    
    booksList = []
    librariesList = []

    inputFile = open(filePath, 'r')

    line = inputFile.readline()
    lineTokens = line.split(' ')

    B = int(lineTokens[0])
    L = int(lineTokens[1])
    D = int(lineTokens[2])


    for index, bookId in enumerate(inputFile.readline().split(' ')):
        booksList.append(Book(int(index), int(bookId)))

    for i in range(L):
        lineTokens = inputFile.readline().split(' ')
        N = int(lineTokens[0])
        T = int(lineTokens[1])
        M = int(lineTokens[2])

        ids = [booksList[int(x)] for x in inputFile.readline().split(' ')]

        newLibrary = Library(ids, T, M, i)
        librariesList.append(newLibrary)


    inputFile.close()

    return (librariesList, booksList)

def displayData(librariesList, booksList):
    print("B: " + str(B) + " L: " + str(L) + " D: " + str(D))
    print("\nBooks list:")
    for book in booksList:
        print("ID: " + str(book.id) + " SCORE: " + str(book.score))
    
    print("\nLibraries:")
    for index, library in enumerate(librariesList):
        print("ID: " + str(index) + " registrationTime: " + str(library.registrationTime) + " booksPerDay: " + str(library.booksPerDay) + " numberOfBooks: " + str(library.booksNumber))
        for book in library.books:
            print("BookID: " + str(book.id))
        print()

def basicSolution(librariesList, booksList):

    librariesList.sort(key=functools.cmp_to_key(compareLibrariesByRegistrationTimeAndBooksPerDay))
    for library in librariesList:
        library.books.sort(key=functools.cmp_to_key(compareBooksByScore))



def compareLibrariesByRegistrationTimeAndBooksPerDay(item1, item2):
    if item1.registrationTime == item2.registrationTime:
        result = item1.booksPerDay - item2.booksPerDay
        return result

    result = item1.registrationTime - item2.registrationTime
    return result

def compareBooksByScore(item1, item2):
    return item2.score - item1.score

def main():
    global B, L, D
    print('Put solution here')
    librariesList, booksList = parseFile('a_example.txt')
    displayData(librariesList, booksList)

    basicSolution(librariesList, booksList)



if __name__ == '__main__':
    main()