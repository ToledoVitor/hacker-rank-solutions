def hash_tuples(integer_list: list[int], number_of_elements: int) -> int:
    """
    https://www.hackerrank.com/challenges/python-tuples/problem

    Given a list of integers, and the list size, create a tuple containing all
    integers in list and return the tuple hash value.

    e.g.:
        number_of_elements: 2
        integer_list: [1, 2]
        return 3713081631934410656
    """

    to_tuple = tuple(integer_list) 
    return hash(to_tuple)


input_test_case_1 = ([1, 2], 2)
assert hash_tuples(input_test_case_1[0], input_test_case_1[1]) == -3550055125485641917

input_test_case_1 = ([2,3,4,5], 4)
assert hash_tuples(input_test_case_1[0], input_test_case_1[1]) == 7852972215226871095
