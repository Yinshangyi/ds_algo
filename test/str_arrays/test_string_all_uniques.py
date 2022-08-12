from src.str_arrays.string_unique_char import check_string_all_unique_chars


def test_string_all_unique_chars_ok():
    all_unique = check_string_all_unique_chars("azerty")
    assert all_unique == True


def test_string_not_all_unique_chars():
    all_unique = check_string_all_unique_chars("azzrty")
    assert all_unique == False


def test_string_chars_more_than_alphabet():
    all_unique = check_string_all_unique_chars("azerty" * 500)
    assert all_unique == False
