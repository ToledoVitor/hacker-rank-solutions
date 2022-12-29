import re


def filter_valid_emails(emails_list: list) -> list:
    """
    https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

    Given N email addresses return a list containing all valid emails.
    When more than one email is valid, return the valid emails in alphabetically order

    The email must follow the order: username@websitename.extension

    Username: Any letter, digits and _ or -;
    Webstie: Any letter or digit;
    Extension: Any letter (with maximum of 3);

    e.g.:
        emails_list: ["name.surname@gmail.com", "anonymous123@yahoo.co.uk", "anonymous123@...uk", "...@domain.us"]

        return ["anonymous123@yahoo.co.uk", "name.surname@gmail.com"]
    """

    regex = '[A-Za-z0-9\-\_]+@[A-Za-z0-9]*(\.[A-Za-z]{2,3})+$'

    valid_emails = [email for email in emails_list if re.match(regex, email)]
    return sorted(valid_emails)


input_test_case_1 = [
    "lara@hackerrank.com",
    "brian-23@hackerrank.com",
    "britts_54@hackerrank.com",
]
assert filter_valid_emails(input_test_case_1) == [
    "brian-23@hackerrank.com",
    "britts_54@hackerrank.com",
    "lara@hackerrank.com"
]


input_test_case_2 = [
    "name_surname@gmail.com",
    "anonymous123@yahoo.co.uk",
    "anonymous123@...uk",
    "...@domain.us"
]
assert filter_valid_emails(input_test_case_2) == ["anonymous123@yahoo.co.uk", "name_surname@gmail.com"]


input_test_case_3 = [
    "iu89_in.plus@google.com",
    "ill@google.com",
    "fill@google1.com",
]
assert filter_valid_emails(input_test_case_3) == ["fill@google1.com", "ill@google.com"]


input_test_case_4 = [
    "fjladfk_iasdfad234@sdlkjf23335.in",
    "ha@git@int.cz",
    "prashant24_@gmail.com",
]
assert filter_valid_emails(input_test_case_4) == ["fjladfk_iasdfad234@sdlkjf23335.in", "prashant24_@gmail.com"]


input_test_case_5 = [
    "learn.point@learningpoint.net",
    "learnpoint@learningpoint.net",
    "learnpoint@learningpoint.net1",
]
assert filter_valid_emails(input_test_case_5) == ["learnpoint@learningpoint.net"]
