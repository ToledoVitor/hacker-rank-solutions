def check_subset(set_A: set, set_B: set) -> bool:
    """
    https://www.hackerrank.com/challenges/py-check-subset/problem

    Given two sets elements, A and B, returns if element A is a subset of element B
    e.g.:
        students_dict: {'Bob': [2, 9, 10], 'Jhon': [10, 11, 12]}
        query_name: 'Bob'

        return (2+9+10)/3 => 7.0
    """
    return set_A.issubset(set_B)


input_test_case_1 = (
  {1, 2, 3, 5, 6},
  {9, 8, 5, 6, 3, 2, 1, 4, 7},
)
assert check_subset(input_test_case_1[0], input_test_case_1[1]) == True
