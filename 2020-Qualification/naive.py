




import numpy as np
import input_parser

res = input_parser.parse("./input-files/a_example.txt")
days = int(res['D'])
books_num = int(res['B'])
libraries_num = int(res['L'])
books_scores = np.asarray(res['scores'])

num_of_books_in_library = np.asarray(res['books_in_library'])
signup_time_for_library = np.asarray(res['signup_time_for_library'])
books_per_day_from_lib = np.asarray(res['books_per_day_from_lib'])
book_ids_for_library = np.asarray(res['book_ids_for_library'])


library_capacity = np.ceil(np.divide(num_of_books_in_library, books_per_day_from_lib ))
days_left_for_capacity = np.full(library_capacity.shape, days) - library_capacity

library_time_score = days_left_for_capacity - signup_time_for_library


# libraries_num =






# books_output = np.argsort(, axis=0)


# get books scores per library
def get_books_scores(book_ids_for_library, books_scores):
    lib_scores = list()
    for books_in_lib in book_ids_for_library:
        books_scores_in_library = books_scores[books_in_lib]
        lib_scores.append(books_scores_in_library)
        print (books_scores_in_library)
    return lib_scores


# calculate the end date of signup per libraries according to specfici order
def libraries_signup_end_date(libraries_sort):
    libraries_latancies_by_order = signup_time_for_library[libraries_sort]
    accumulated_days = np.add.accumulate(libraries_latancies_by_order)
    return accumulated_days

# calculate how much books each library can scan according to specficic order
def number_of_libraries_to_sign_up(libraries_sort, days):
    accumulated_days = libraries_signup_end_date(libraries_sort)
    accumulated_days = np.append(accumulated_days, days+1)
    return np.argmax(accumulated_days > days)


def get_num_of_scanned_books_per_library(num_of_books_for_shipment_per_library, books_per_day_from_lib, libraries_end_date, days):
    # TODO add number of actual books
    number_days_left_per_library = np.maximum(np.full(libraries_end_date.shape, days) - libraries_end_date , 0)
    number_of_books_sent_for_library = np.minimum(number_days_left_per_library * books_per_day_from_lib, num_of_books_for_shipment_per_library)
    return number_of_books_for_library


def


libraries_sort = np.argsort(library_time_score)[::-1]
libraries_end_date = libraries_signup_end_date(libraries_sort)




# print (book_ids_for_library )

# print(get_books_scores())

# def score_per_library():



