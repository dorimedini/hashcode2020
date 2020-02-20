import numpy as np
import input_parser


def total_library_scores(dataset):
    r = []
    for l in range(dataset['L']):
        scores = np.array([dataset['scores'][bID] for bID in dataset['book_ids_for_library'][l]])
        r.append(np.sum(scores))
    return r


def missing_books(dataset):
    counter = 0
    for book in range(dataset['B']):
        if book not in dataset['books_to_libraries_containing']:
            counter += 1
    return counter


# # get books scores per library
# def get_books_scores(book_ids_for_library, books_scores):
#     lib_scores = list()
#     for books_in_lib in book_ids_for_library:
#         books_scores_in_library = books_scores[books_in_lib]
#         lib_scores.append(books_scores_in_library)
#         print(books_scores_in_library)
#     return lib_scores


# calculate the end date of signup per libraries according to specfici order
def get_libraries_signup_end_date(libraries_sort, signup_time_for_library):
    libraries_latancies_by_order = signup_time_for_library[libraries_sort]
    accumulated_days = np.add.accumulate(libraries_latancies_by_order)
    return accumulated_days


# calculate how much books each library can scan according to specficic order
def get_number_of_libraries_to_sign_up(libraries_sort, days, signup_time_for_library):
    accumulated_days = get_libraries_signup_end_date(libraries_sort, signup_time_for_library)
    accumulated_days = np.append(accumulated_days, days + 1)
    return np.argmax(accumulated_days > days)


def get_num_of_scanned_books_per_library(num_of_books_for_shipment_per_library, books_per_day_from_lib,
                                         libraries_end_date, days):
    # TODO add number of actual books
    number_days_left_per_library = np.maximum(np.full(libraries_end_date.shape, days) - libraries_end_date, 0)
    number_of_books_sent_for_library = np.minimum(number_days_left_per_library * books_per_day_from_lib,
                                                  num_of_books_for_shipment_per_library)
    return number_of_books_sent_for_library


def print_output(library_order, book_order_per_library, num_of_books_for_shipment_per_library, books_per_day_from_lib,
                 libraries_end_date, days, output_file, signup_time_for_library):
    # Prints the output as requested.
    with open(output_file, "w") as f:
        num_of_scanned_books_per_library = get_num_of_scanned_books_per_library(num_of_books_for_shipment_per_library,
                                                                                books_per_day_from_lib,
                                                                                libraries_end_date, days)
        num_of_libraries = get_number_of_libraries_to_sign_up(library_order, days, signup_time_for_library)

        f.write(str(num_of_libraries) + '\n')
        for library, num_of_scanned_books, books_to_scan in zip(library_order, num_of_scanned_books_per_library,
                                                                book_order_per_library):
            f.write(str(library) + " " + str(num_of_scanned_books) + '\n')
            # f.write(' '.join([str(b) for b in books_to_scan]) + '\n')
            print(books_to_scan)
            print("*"*30, str(books_to_scan)[1:-1])
            f.write(str(books_to_scan)[1:-1] + '\n')

def parse_file(filename):
    res = input_parser.parse(filename)
    days = int(res['D'])
    books_num = int(res['B'])
    libraries_num = int(res['L'])
    books_scores = np.asarray(res['scores'])

    num_of_books_in_library = np.asarray(res['books_in_library'])
    signup_time_for_library = np.asarray(res['signup_time_for_library'])
    books_per_day_from_lib = np.asarray(res['books_per_day_from_lib'])
    book_ids_for_library = np.asarray(res['book_ids_for_library'])

    return (days, books_num, libraries_num, books_scores, num_of_books_in_library, signup_time_for_library,
            books_per_day_from_lib, book_ids_for_library)
