from input_parser import parse
import numpy as np
from utils import parse_file, initial_library_scores


def solve_c():
    (days, books_num, libraries_num, books_scores, num_of_books_in_library, signup_time_for_library,
     books_per_day_from_lib, book_ids_for_library) = parse_file("inputs/c_incunabula.txt")
    res = parse("inputs/c_incunabula.txt")
    # Sort by (total_book_score/signup_time), then do greedy
    # print (initial_library_scores(res))
    scores = initial_library_scores(res)
    sorted_libs = np.flip(np.argsort([score[0] for score in scores]))
    sorted_books = book_ids_for_library[sorted_libs]
    return (sorted_libs, sorted_books , num_of_books_in_library, books_per_day_from_lib,
            days, signup_time_for_library)
