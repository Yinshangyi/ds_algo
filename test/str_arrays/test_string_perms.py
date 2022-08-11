from src import is_strings_permutations, sort_string


def test_sort_string():
    input = "bcaed"
    output = sort_string(input)
    assert output == "abcde"


def test_strings_are_permutations():
    str1 = "azerty"
    str2 = "aerzyt"
    is_perms = is_strings_permutations(str1, str2)
    assert is_perms == True


def test_strings_are_not_permutations():
    str1 = "azerty"
    str2 = "azevby"
    is_perms = is_strings_permutations(str1, str2)
    assert is_perms == False
