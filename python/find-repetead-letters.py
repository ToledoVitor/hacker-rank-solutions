def find_the_letters(array: list) -> list:
    '''
    Returns the letters that are present in all the given strings.
    Also consider repetition, and returns if are two of the same letter
    in all words.

    :array - list[str]
    :return - list[str]
    '''

    testing_array = [list(name) for name in array]
    base_string = testing_array[0]

    solution = []
    while len(base_string) > 0:
        letter = base_string.pop()
        in_all_words = True

        for name in testing_array[1:]:
            try:
                name.remove(letter)
            except:
                in_all_words = False

        if in_all_words:
            solution.append(letter)

    return sorted(solution)


test_list = ['ellie', 'nelli', 'celli']
expected_solution = ['e','i','l','l']

assert find_the_letters(test_list) == expected_solution
