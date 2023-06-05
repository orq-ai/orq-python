def is_invalid_api_key(key):
    return not key.startswith("RQST.")


def are_object_equals(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        keys1 = sorted(dict1.keys())
        keys2 = sorted(dict2.keys())

        if keys1 != keys2:
            return False

        for key in keys1:
            value1 = dict1[key]
            value2 = dict2[key]

            if isinstance(value1, dict) and isinstance(value2, dict):
                if not are_object_equals(value1, value2):
                    return False
            elif value1 != value2:
                return False

        return True

    return False
