def find_the_percentages(students_dict: dict, query_name: str) -> int | float:
    """
    https://www.hackerrank.com/challenges/finding-the-percentage/problem

    Given a dict of students containing their grades, return a student average grade
    e.g.:
        students_dict: {'Bob': [2, 9, 10], 'Jhon': [10, 11, 12]}
        query_name: 'Bob'

        return (2+9+10)/3 => 7.0
    """

    student_grades = students_dict[query_name]
    return sum(student_grades) / len(student_grades)


input_test_case_1 = (
    {
        "alpha": [20, 30, 40],
        "beta": [30, 50, 70],
    },
    "beta",
)
assert find_the_percentages(input_test_case_1[0], input_test_case_1[1]) == 50

input_test_case_2 = (
    {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60],
    },
    "Malika",
)
assert find_the_percentages(input_test_case_2[0], input_test_case_2[1]) == 56

input_test_case_3 = (
    {
        "Harsh": [25, 26.5, 28],
        "Anurag": [26, 28, 30],
    },
    "Harsh",
)
assert find_the_percentages(input_test_case_3[0], input_test_case_3[1]) == 26.5
