import json
from typing import Any, List, Dict

from .exceptions import OrquestaException



def dict_cleanup(input_dict):
    return {k: v for k, v in input_dict.items() if v is not None}


def extract_json(byte_string) -> List[Dict[str, Any]]:
    results = []
    brace_count = 0
    current_object = ""
    in_string = False

    input_string = byte_string.decode("utf-8")
    json_str = input_string[6:]  # Remove the 'data: ' prefix

    for char in json_str:
        if char == '"' and (len(current_object) == 0 or current_object[-1] != "\\"):
            in_string = not in_string

        if char == "{" and not in_string:
            brace_count += 1
        if char == "}" and not in_string:
            brace_count -= 1

        current_object += char

        if brace_count == 0 and current_object != "":
            try:
                parsed = json.loads(current_object)
                results.append(parsed)
                current_object = ""
            except json.JSONDecodeError:
                continue

    return results


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
