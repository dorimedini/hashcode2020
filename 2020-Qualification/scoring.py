from utils import total_library_scores


def c_score(dataset):
    '''return the score for dataset c'''
    scores = total_library_scores(dataset)
    scores = scores/dataset['signup_time_for_library']
    return scores

