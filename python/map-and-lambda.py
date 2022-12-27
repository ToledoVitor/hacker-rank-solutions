def fibonnacci(number):
    """
    https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

    Generate a list of the first N fibonacci numbers, with 0 being the first
    number. Then, apply the map function and a lambda expression to cube each
    fibonacci number and print the list.
    """

    return_list = [0, 1]
    if number > 15:
        # shouldn't deal with this complexity
        return []

    if number <= 2:
        return return_list[:number]

    while len(return_list) < number:
        last = return_list[-1]
        penultimate = return_list[-2]
        return_list.append(last + penultimate)
    
    return return_list

cube = lambda x: x**3 

def print_fibonnacci(number_input):
    return list(map(cube, fibonnacci(number_input)))


input_test_case_1 = 5
assert print_fibonnacci(input_test_case_1) == [0, 1, 1, 8, 27]

input_test_case_2 = 1
assert print_fibonnacci(input_test_case_2) == [0]

input_test_case_3 = 2
assert print_fibonnacci(input_test_case_3) == [0, 1]
