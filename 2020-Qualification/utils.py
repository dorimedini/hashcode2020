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
                                         libraries_end_date, days, book_order_per_library=None):
    # TODO add number of actual books
    number_days_left_per_library = np.maximum(np.full(libraries_end_date.shape, days) - libraries_end_date, 0)
    number_of_books_sent_for_library = np.minimum(
        np.multiply(number_days_left_per_library, books_per_day_from_lib, dtype=np.int64),
        num_of_books_for_shipment_per_library)
    if book_order_per_library is not None:
        actual_books_sent = [len(s) for s in book_order_per_library]
        number_of_books_sent_for_library = np.minimum(
            number_of_books_sent_for_library,
            actual_books_sent)
    print(number_of_books_sent_for_library)
    return number_of_books_sent_for_library


def print_output(library_order, book_order_per_library, num_of_books_for_shipment_per_library, books_per_day_from_lib,
                 libraries_end_date, days, output_file, signup_time_for_library):
    # Prints the output as requested.
    with open(output_file, "w") as f:
        num_of_scanned_books_per_library = get_num_of_scanned_books_per_library(num_of_books_for_shipment_per_library,
                                                                                books_per_day_from_lib,
                                                                                libraries_end_date, days,
                                                                                book_order_per_library)
        num_of_libraries = get_number_of_libraries_to_sign_up(library_order, days, signup_time_for_library)

        f.write(str(num_of_libraries) + '\n')
        for library, num_of_scanned_books, books_to_scan in zip(library_order, num_of_scanned_books_per_library,
                                                                book_order_per_library):
            if num_of_scanned_books > 0:
                f.write(str(library) + " " + str(num_of_scanned_books) + '\n')
                f.write(' '.join([str(b) for b in books_to_scan[:num_of_scanned_books]]) + '\n')


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


def initial_library_scores(dataset):
    '''gets a dataset and computes the initial score per library'''
    signup_time = dataset['signup_time_for_library']
    total_time = dataset['D']
    num_books = dataset['books_in_library']
    books_per_day = dataset['books_per_day_from_lib']
    books_in_libraries = dataset['book_ids_for_library']
    scores = []
    for library in range(dataset['L']):
        books_scores = np.sort(np.array([(dataset['scores'][bID], bID) for bID in books_in_libraries[library]]))
        if signup_time[library] > total_time:
            scores.append((0, []))
        else:
            if (total_time-signup_time[library])<num_books[library]/books_per_day[library]:
                books_score =books_score[:(total_time-signup_time[library])*books_per_day[library]]
            score = np.sum([score for (score, book) in books_scores]) / signup_time[library]    
            books = [book for (score, book) in books_scores]
            scores.append((score, books))
    return scores


def update_scores(scores, dataset, num_remaining_days, library):
    books_uploaded = scores[library][1]
    books_with_libraries = dataset['books_to_libraries_containing']
    for book in books_uploaded:
        libraries = books_with_libraries[book]
        for book_library in libraries:
            signup_time = dataset['signup_time_for_library'][book_library]
            books_per_day = dataset['books_per_day_from_lib'][book_library]
            if signup_time > num_remaining_days:
                scores[book_library] = (0, [])
            else:
                score_to_remove = 0
                for remove_book in books_uploaded:
                    if remove_book in scores[book_library][1]:
                        score_to_remove+= dataset['scores'][remove_book]
                        scores[book_library][1].remove(remove_book)
                books = scores[book_library][1]
                if (num_remaining_days - signup_time) < len(books)/books_per_day:
                    books_to_remove = books[(num_remaining_days - signup_time[library]) * books_per_day:]
                    books = scores[book_library][1][:(num_remaining_days - signup_time[library]) * books_per_day]
                    score_to_remove += np.sum([dataset['scores'][bID] for bID in books_to_remove])
                scores[book_library] = (scores[book_library][0] - score_to_remove/signup_time, books)
    scores[library] = (0, [])