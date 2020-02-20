import numpy as np
import input_parser
import utils
import solve_c
#
# res = input_parser.parse("./inputs/b_read_on.txt")
# days = int(res['D'])
# books_num = int(res['B'])
# libraries_num = int(res['L'])
# books_scores = np.asarray(res['scores'])
#
# num_of_books_in_library = np.asarray(res['books_in_library'])
# signup_time_for_library = np.asarray(res['signup_time_for_library'])
# books_per_day_from_lib = np.asarray(res['books_per_day_from_lib'])
# book_ids_for_library = np.asarray(res['book_ids_for_library'])
#
# library_capacity = np.ceil(np.divide(num_of_books_in_library, books_per_day_from_lib))
# days_left_for_capacity = np.full(library_capacity.shape, days) - library_capacity
#
# library_time_score = days_left_for_capacity - signup_time_for_library

# libraries_num =


# books_output = np.argsort(, axis=0)


(libraries_sort, books_sort, num_of_books_in_library, books_per_day_from_lib,
 days, signup_time_for_library) = solve_b.solve_b()
# libraries_sort = np.argsort(library_time_score)[::-1]
libraries_end_date = utils.get_libraries_signup_end_date(libraries_sort, signup_time_for_library)

# print (book_ids_for_library )

# print(get_books_scores())

# def score_per_library():
utils.print_output(libraries_sort, books_sort, num_of_books_in_library, books_per_day_from_lib,
                   libraries_end_date, days, 'out.txt', signup_time_for_library)
