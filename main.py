from itertools import count
from data import data_list
from book import Book


def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def create_book_list(data_list):
    book_list = []
    for dictionary in data_list:
        new_book = Book(dictionary)
        book_list.append(new_book)
    return book_list


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    lowest_number_of_reviews = min(books_2018, key=lambda book: book.number_of_reviews)
    print(
        f"The book with the lowest number of reviews in 2018 was {lowest_number_of_reviews.name} with a total of {lowest_number_of_reviews.number_of_reviews} reviews")


def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    list_of_fiction_books = list(filter(lambda book: book.genre == "Fiction", book_list))
    number_of_fiction_books = len(list_of_fiction_books)
    list_of_non_fiction_books = list(filter(lambda book: book.genre == "Non Fiction", book_list))
    number_of_non_fiction_books = len(list_of_non_fiction_books)
    if number_of_fiction_books > number_of_non_fiction_books:
        print(f"The genre that appeared most in the top 50's list is Fiction")
    else:
        print(f"The genre that appeared most in the top 50's list is Non-Fiction, appearing {len(list_of_non_fiction_books)} times")


def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    list_of_book_names = [book.name for book in book_list]
    name_count_list = []
    for name in list_of_book_names:
        list_of_book_names.count(name)
        name_count_list.append({"name": name, "count": list_of_book_names.count(name)})
    appeared_most = name_count_list[0]
    for each in name_count_list:
        if each['count'] > appeared_most['count']:
            appeared_most = each
        else:
            continue
    print(f"The book that has appeared the most in the top 50's list is {appeared_most['name']} and it appeared {appeared_most['count']} times")
# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
