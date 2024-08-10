from packages import *

def trim_zeros_around_ones(lst):
    first_index = None
    for i in range(len(lst) - 4):
        if lst[i:i+5] == [1, 1, 1, 1, 1]:
            first_index = i
            break
    
    if first_index is None:
        return []

    last_index = None
    for i in range(len(lst) - 4):
        if lst[i:i+5] == [1, 1, 1, 1, 1]:
            last_index = i + 4
            break

    if last_index is None:
        return []

    for i in range(last_index + 1, len(lst) - 4):
        if lst[i:i+5] == [1, 1, 1, 1, 1]:
            last_index = i + 4

    return lst[first_index:last_index + 1]

def two_lists_similarity_score(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    matches = sum(1 for i in range(len(list1)) if list1[i] == list2[i])
    
    score = (matches / len(list1))
    return score
