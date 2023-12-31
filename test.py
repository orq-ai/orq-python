import unittest
import os
from orquesta_sdk.exceptions import (
    OrquestaInvalidAPIException,
)

from orquesta_sdk import Orquesta, OrquestaClientOptions
from orquesta_sdk.util import parse_json


class TestOrquesta(unittest.TestCase):
    def setUp(self):
        self.valid_options = OrquestaClientOptions(api_key="valid_api_key")

    def test_init_with_valid_options(self):
        orquesta = Orquesta(self.valid_options)
        self.assertEqual(orquesta.deployments.options, self.valid_options)

    def test_init_with_no_api_key(self):
        os.environ["ORQUESTA_API_KEY"] = ""
        invalid_options = OrquestaClientOptions(api_key=None)
        with self.assertRaises(OrquestaInvalidAPIException):
            Orquesta(invalid_options)

    def test_init_with_api_key_in_env(self):
        os.environ["ORQUESTA_API_KEY"] = "valid_api_key"
        options = OrquestaClientOptions(api_key=None)
        orquesta = Orquesta(options)
        self.assertEqual(orquesta.deployments.options, options)


class TestOrquestaJsonParserUtil(unittest.TestCase):
    def test_parse_json(self):
        # Test case 1: Valid JSON object
        input_string = '{"name": "John", "age": 30}{"name": "John", "age": 30}'
        expected_output = {"name": "John", "age": 30}
        print(parse_json(input_string))
        assert parse_json(input_string) == [expected_output, expected_output]

        # Test case 2: Valid JSON objects separated by whitespace
        input_string = '{"name": "John", "age": 30}   {"name": "Jane", "age": 25}'
        expected_output = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        assert parse_json(input_string) == expected_output

        # Test case 3: Valid JSON objects with nested objects
        input_string = '{"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "New York"}}'
        expected_output = {
            "name": "John",
            "age": 30,
            "address": {"street": "123 Main St", "city": "New York"},
        }
        assert parse_json(input_string) == [expected_output]

        # Test case 4: Invalid JSON object
        input_string = '{"name": "John", "age": 30,}'
        expected_output = []
        assert parse_json(input_string) == expected_output

        # Test case 5: Empty input string
        input_string = ""
        expected_output = []
        assert parse_json(input_string) == expected_output

        # Test case 6: Input string with no JSON objects
        input_string = "This is a test string"
        expected_output = []
        assert parse_json(input_string) == expected_output

        print("All test cases pass")


if __name__ == "__main__":
    unittest.main()
