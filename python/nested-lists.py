from collections import defaultdict


def get_second_lowest_grade(students_input):
    # https://www.hackerrank.com/challenges/nested-list/problem
    lowest_grade = None
    second_low = None
    students = defaultdict(list)

    for student in students_input:
        # ["Harry", 37.21]
        name = student[0]
        grade = student[1]
        students[grade].append(name)

        if not lowest_grade:
            lowest_grade = grade
        elif not second_low and grade != lowest_grade:
            second_low = grade

        if grade < lowest_grade:
            second_low = lowest_grade
            lowest_grade = grade
        elif second_low and grade < second_low and grade != lowest_grade:
            second_low = grade

    lowest_scores = students[second_low]
    # In cases multiples students match the second_low grade, returns the students by alphabetically order
    return sorted(lowest_scores)


input_test_case_1 = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39],
]
assert get_second_lowest_grade(input_test_case_1) == ["Berry", "Harry"]

input_test_case_2 = [
    ["Hina", 20],
    ["Shina", 20.1],
    ["Mina", 20.01],
    ["Tina", 20.001],
]
assert get_second_lowest_grade(input_test_case_2) == ["Tina"]

input_test_case_3 = [
  ["Rachel", -50],
  ["Mawer", -50],
  ["Sheen", -50],
  ["Shaheen", 51]
]
assert get_second_lowest_grade(input_test_case_3) == ["Shaheen"]

input_test_case_4 = [
    ["Harsh", 20],
    ["Beria", 20],
    ["Varun", 19],
    ["Kakunami", 19],
    ["Vikas", 21],
]
assert get_second_lowest_grade(input_test_case_4) == ["Beria", "Harsh"]
