import numpy as np


def total_library_scores(dataset):
    r = []
    for l in range(dataset['L']):
        scores = np.array([dataset['scores'][bID] for bID in dataset['book_ids_for_library'][l]])
        r.append(np.sum(scores))
    return r


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
        if signup_time[library]>total_time:
            scores.append((-1,[]))
        else:
            if (total_time-signup_time[library])*books_per_day[library]<num_books[library]:
                books_score =books_score[:(total_time-signup_time[library])*books_per_day[library]]
            score = np.sum([score for (score, book) in books_scores]) / books_per_day[library]
            books = [book for (score, book) in books_scores]
            scores.append((score, books))
    return scores
