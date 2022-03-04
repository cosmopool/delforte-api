def to_camel_case(text: str, separator: str) -> str:
    tmp = text.split(separator)
    if len(text) == 0:
        return text
    return tmp[0] + ''.join(i.capitalize() for i in tmp[1:])
