from bisect import bisect_left, bisect_right

def count_index(li, left_value, right_value):
    left_index = bisect_left(li, left_value)
    right_index = bisect_right(li, right_value)
    return right_index - left_index