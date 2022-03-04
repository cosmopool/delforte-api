def capitalize_dict_keys(dictionary: dict) -> dict:
    d = {}
    for key in dictionary.keys():
        d[key.capitalize()] = dictionary[key]

    return d
