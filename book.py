class Book:
    def __init__(self, book_dictionary) -> None:
        self.name = book_dictionary["name"]
        self.author = book_dictionary["author"]
        self.user_rating = book_dictionary["user_rating"]
        self.number_of_reviews = book_dictionary["number_of_reviews"]
        self.price = book_dictionary["price"]
        self.year = book_dictionary["year"]
        self.genre = book_dictionary["genre"]
