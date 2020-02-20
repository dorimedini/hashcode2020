import scoring
import utils
import numpy as np


def solve_b():
    (days, books_num, libraries_num, books_scores, num_of_books_in_library, signup_time_for_library,
     books_per_day_from_lib, book_ids_for_library) = utils.parse_file("inputs/b_read_on.txt")

    sorted_libs = np.argsort(signup_time_for_library)
    # print(sorted_libs)
    # print(signup_time_for_library[sorted_libs])

    return (sorted_libs, book_ids_for_library, num_of_books_in_library, books_per_day_from_lib,
            days, signup_time_for_library)
