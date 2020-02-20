import numpy as np


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
