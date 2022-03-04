def validate_id(id: int):
    is_string = isinstance(id, str)
    is_empty = id == None
    is_negative_or_zero = isinstance(id, int) and id <= 0

    if is_negative_or_zero or is_empty or is_string:
        return False
    else:
        return True
