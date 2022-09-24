"""
Bookrecs.py
Takes given ratings.txt and given booklist.txt and matches the ratings for each person
with the books. Then sorts these entries by lastname first name, and then book title.
Then the program asks for input of which person, a different operator ('<, >, =') and
then an integerreferring to the ratings between -5 to 5. The program returns the
appropriate searched for criteria.
"""
def main():
    """program starts here"""
    t_books = []
    books = []
    t_ratings = []
    ratings = {}
    with open("booklist.txt", "r") as file:  # creates list of books
        for line in file:
            t_books.append(line.strip().split(','))
    file.close()
    with open("ratings.txt", "r") as file:  # creates list of ratings
        for line in file:
            t_ratings.append(line.strip().split(','))
    file.close()

    for book in t_books:  # splits author string to sort by last name
        book[0] = book[0].split()
        books.append(book)

    while True:  # loop iterates through t_ratings list and changes it into ratings dict
        key = t_ratings.pop(0)
        value = t_ratings.pop(0)
        ratings[key[0].lower()] = value[0]
        if len(t_ratings) <= 1:
            break

    input_person = input('Please enter a name: ').lower()
    input_symbol = input("Please enter a symbol: ('<, =, >') ")
    input_integer = input("Please enter the rating integer: (From: '-5, 5') ")

    if ratings.get(input_person) is None:  # draws error for input person missing
        print('Person not found, please try again')
        exit()

    if int(input_integer) > 5 or int(input_integer) < -5:  # draws error for input number range
        print('Please enter an integer from -5 to 5')
        exit()

    if input_symbol != '=' and input_symbol != '>' and input_symbol != '<':  # draws error for input symbol
        print("Please enter either '<', '>' or '='")
        exit()

    selected_book_ratings = []  # sorts the books according to author last name

    def rate_books(books_list, person_ratings):
        person_ratings = person_ratings.split()
        rated_books = list(zip(books_list, person_ratings))  
        rated_books = sorted(rated_books, key=lambda x: (x[0][0][-1], x[0][0][0], x[0][1]))  # sorts rated_books list by last, first, book title

        if input_symbol == '<':  # logic for correct books displayed
            for item in rated_books:
                if item[1] <= input_integer:
                    selected_book_ratings.append(item)
        elif input_symbol == '>':
            for item in rated_books:
                if item[1] >= input_integer:
                    selected_book_ratings.append(item)
        elif input_symbol == '=':
            for item in rated_books:
                if item[1] == input_integer:
                    selected_book_ratings.append(item)
        else:
            print('Please enter a valid symbol')
        for item in selected_book_ratings:
            int(item[1])
        for item in selected_book_ratings:
            author = ' '.join(item[0][0])
            title = ''.join(item[0][1])
            rating = item[1]
            book = author + ', ' + title + ', ' + rating
            print(book)
    rate_books(books, ratings[input_person])

if __name__ == "__main__":
    main()
