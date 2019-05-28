"""
ITCS 6114  - Fuzzy Interval Sorting
"""


def perform_fuzzy_sort(intervals_list, start, end):
    """
    Perform the sorting operation by calculating the pivot in this case the intersection and spliting the input list
    into 2 based on the intersection
    :param intervals_list:
    :param start: start list index for the sub list
    :param end: end list index for the sub list
    """
    if start < end:
        intersection = calculate_intersection(intervals_list, start, end)
        right_partition = perform_right_partition(intervals_list, start, end, intersection)
        left_partition = perform_left_partition(intervals_list, start, right_partition, intersection)
        perform_fuzzy_sort(intervals_list, start, left_partition - 1)
        perform_fuzzy_sort(intervals_list, right_partition + 1, end)

def calculate_intersection(intervals_list, start, end):
    """
    Calculates the intersections of the ranges to return an interval otherwise returns the interval at the end of the list
    based on Lomuto's paritioning algorithm
    :param intervals_list:
    :param start:
    :param end:
    :return: intersection of the interval items
    """
    intersection = intervals_list[end]
    for i in range(start, end):
        if intervals_list[i][0] <= intersection[1] and intervals_list[i][1] >= intersection[0]:
            if intervals_list[i][0] > intersection[0]:
                intersection = (intervals_list[i][0], intersection[1])
            if intervals_list[i][1] < intersection[1]:
                intersection = (intersection[0], intervals_list[i][1])
    return intersection

def perform_right_partition(intervals_list, pivot, end, intersection):
    """
    Splits the sublist based on the location of the intersection from its left side
    :param intervals_list:
    :param pivot:
    :param end:
    :param intersection:
    :return: New parition index for the right side of the intervals list
    """
    right_part_start = pivot - 1
    for j in range(pivot, end):
        if intervals_list[j][0] <= intersection[0]:
            right_part_start += 1
            intervals_list[right_part_start], intervals_list[j] = intervals_list[j], intervals_list[right_part_start]
    #Swap the variables
    intervals_list[right_part_start + 1], intervals_list[end] = intervals_list[end], intervals_list[right_part_start + 1]
    return right_part_start + 1

def perform_left_partition(intervals_list, start, right, intersection):
    """
    Splits the sublist based on the location of the intersection from its left side
    :param intervals_list:
    :param start:
    :param right:
    :param intersection:
    :return: New partition index for the left side of the parition list
    """
    left_part_start = start - 1
    for j in range(start, right):
        if intervals_list[j][1] < intersection[1]:
            left_part_start += 1
            intervals_list[left_part_start], intervals_list[j] = intervals_list[j], intervals_list[left_part_start]
    # Swap the variables
    intervals_list[left_part_start + 1], intervals_list[right] = intervals_list[right], intervals_list[left_part_start + 1]
    return left_part_start + 1

def perform_fuzzy_interval_test_cases(case_number, list_of_intervals):
    print("\nTest Case #{}\n\nInput Elements:\n".format(case_number))
    print(*list_of_intervals, sep='\n')
    perform_fuzzy_sort(list_of_intervals, 0, len(list_of_intervals) - 1)
    print("\nTest Case #{}\n\nOutput Elements:\n".format(case_number))
    print(*list_of_intervals, sep='\n')

def main():
    # Test Case 1
    list_of_intervals_1 = [(5,7),
                            (1,3),
                            (4,6),
                            (8,10)]
    perform_fuzzy_interval_test_cases(1, list_of_intervals_1)

    # Test Case 2
    list_of_intervals_2 = [(6, 7),
                            (9, 11),
                            (13, 14),
                            (3, 7),
                            (11, 15),
                            (13, 14),
                            (12, 14),
                            (14, 15),
                            (9, 15),
                            (5, 7),
                            (7, 9),
                            (1, 5),
                            (1, 9),
                            (6, 10)]
    perform_fuzzy_interval_test_cases(2, list_of_intervals_2)

if __name__ == '__main__':
    main()