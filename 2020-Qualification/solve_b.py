import scoring
from input_parser import parse
import numpy as np


def solve_b():
    res = parse("inputs/b_read_on.txt")
    days = int(res['D'])
    books_num = int(res['B'])
    libraries_num = int(res['L'])
    books_scores = np.asarray(res['scores'])

    num_of_books_in_library = np.asarray(res['books_in_library'])
    signup_time_for_library = np.asarray(res['signup_time_for_library'])
    books_per_day_from_lib = np.asarray(res['books_per_day_from_lib'])
    book_ids_for_library = np.asarray(res['book_ids_for_library'])

    sorted_libs = np.argsort(signup_time_for_library)
    print(sorted_libs)
    print(signup_time_for_library[sorted_libs])
    return sorted_libs, books_per_day_from_lib
