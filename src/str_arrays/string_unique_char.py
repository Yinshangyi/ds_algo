def check_string_all_unique_chars(string_to_check: str) -> bool:
    MAX_CHAR_POSSIBLE = 128

    if len(string_to_check) > MAX_CHAR_POSSIBLE:
        return False

    possible_chars = [False for n in range(0, MAX_CHAR_POSSIBLE)]

    for char in string_to_check:
        ascii_code = ord(char)
        if possible_chars[ascii_code]:
            return False
        possible_chars[ascii_code] = True
    return True
