

class Library:

    def __init__(self, books, registrationTime, booksPerDay):
        self.books = books
        self.registrationTime = registrationTime
        self.booksPerDay = booksPerDay
        self.booksNumber = len(books)


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

    booksList = [int(x) for x in inputFile.readline().split(' ')]


    for i in range(L):
        lineTokens = inputFile.readline().split(' ')
        N = int(lineTokens[0])
        T = int(lineTokens[1])
        M = int(lineTokens[2])

        ids = [int(x) for x in inputFile.readline().split(' ')]

        newLibrary = Library(ids, T, M)
        librariesList.append(newLibrary)


    inputFile.close()

    return (librariesList, booksList)

def main():
    global B, L, D
    print('Put solution here')
    librariesList, booksList = parseFile('a_example.txt')
    print("B: " + str(B) + " L: " + str(L) + " D: " + str(D))
    print("\nBooks list:")
    for index, book in enumerate(booksList):
        print("ID: " + str(index) + " SCORE: " + str(book))
    
    print("\nLibraries:")
    for index, library in enumerate(librariesList):
        print("ID: " + str(index) + " registrationTime: " + str(library.registrationTime) + " booksPerDay: " + str(library.booksPerDay) + " numberOfBooks: " + str(library.booksNumber))
        for book in library.books:
            print("BookID: " + str(book))
        print()



if __name__ == '__main__':
    main()