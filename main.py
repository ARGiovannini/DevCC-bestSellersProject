from itertools import count
from timeit import repeat
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
    print('')
    print("*******************************************************************")
    print('')
    bonus_analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    bonus_analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    bonus_analysis_three(books)


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
    name_author_dictionary = {}
    for book in book_list:
        name_author_dictionary.update({book.name: book.author})
    list_of_authors = list(name_author_dictionary.values())
    author_count_list = []
    for author in list_of_authors:
        author_count_list.append({"author": author, "count": list_of_authors.count(author)})
    appeared_most = author_count_list[0]
    for each in author_count_list:
        if each['count'] > appeared_most['count']:
            appeared_most = each
    print(f"The author that has the highest number of distinct titles in the top 50's list is {appeared_most['author']} and they have {appeared_most['count']} titles!")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")
    year = 2009
    while year < 2020:
        book_year_list = list(filter(lambda book: book.year == year, book_list))
        highest_rating = max(book_year_list, key = lambda book: book.user_rating)
        highest_rating_list = list(filter(lambda book: book.user_rating == highest_rating.user_rating, book_year_list))
        top_book = max(highest_rating_list, key = lambda book: book.number_of_reviews)
        print(f"In {year}, '{top_book.name}' was the top book.")
        year += 1

def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")
    list_of_books_list = []
    year = 2009
    while year < 2020:
        new_book_list = list(filter(lambda book: book.year == year, book_list))
        list_of_books_list.append(new_book_list)
        year +=1
    a = 0
    while a < len(list_of_books_list) - 1:
        for book in list_of_books_list[a]:
            b = 1
            for second_book in list_of_books_list[a + b]:
                if book.name == second_book.name:
                    b += 1
                    if a + b >= len(list_of_books_list):
                        break
                    for third_book in list_of_books_list[a + b]:
                        if book.name == third_book.name:
                            b += 1
                            if a + b >= len(list_of_books_list):
                                break
                            for fourth_book in list_of_books_list[a + b]:
                                if book.name == fourth_book.name:
                                    b += 1
                                    if a + b >= len(list_of_books_list):
                                        break
                                    for fifth_book in list_of_books_list[a + b]:
                                        if book.name == fifth_book.name:
                                            b += 1
                                            if a + b >= len(list_of_books_list):
                                                break
                                            for sixth_book in list_of_books_list[a + b]:
                                                if book.name == sixth_book.name:
                                                    b += 1
                                                    if a + b >= len(list_of_books_list):
                                                        break
                                                    for seventh_book in list_of_books_list[a + b]:
                                                        if book.name == seventh_book.name:
                                                            b += 1
                                                            if a + b >= len(list_of_books_list):
                                                                break
                                                            for eigth_book in list_of_books_list[a + b]:
                                                                if book.name == eigth_book.name:
                                                                    b += 1
                                                                    if a + b >= len(list_of_books_list):
                                                                        break
                                                                    for ninth_book in list_of_books_list[a + b]:
                                                                        if book.name == ninth_book.name:
                                                                            b += 1
                                                                            if a + b >= len(list_of_books_list):
                                                                                break
                                                                            for tenth_book in list_of_books_list[a + b]:
                                                                                if book.name == tenth_book.name:
                                                                                    print(f"{book.name} has appeared the most number of times consecutively, a total of 10 years in a row")
                                                                                    break

                                                            
                else:
                    continue
        a += 1

            


run_analysis(data_list)