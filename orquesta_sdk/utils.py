import json

from .exceptions import OrquestaException


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


def dict_cleanup(input_dict):
    return {k: v for k, v in input_dict.items() if v is not None}


def extract_json(byte_string):
    try:
        decoded_string = byte_string.decode("utf-8")
        if decoded_string.startswith("data: "):
            json_str = decoded_string[6:]  # Remove the 'data: ' prefix
            json_obj = json.loads(json_str)
            return json_obj
        else:
            return None
    except json.JSONDecodeError:
        return None
    except UnicodeDecodeError:
        return None


def notify_error(response):
    error = response.json()

    if "error" not in error and "message" not in error:
        response.raise_for_status()

    raise OrquestaException(
        name=error["name"],
        message=error["message"],
        provider_error_message=error.get("provider_error_message", None),
        code=error["error_code"],
    )
