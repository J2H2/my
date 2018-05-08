def is_integer(number_string: str) -> bool:
    try:
        int(number_string)
        return True
    except ValueError:
        return False
