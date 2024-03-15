import unittest
import os
from orq_ai_sdk.exceptions import (
    OrqAIInvalidAPIException,
)

from orq_ai_sdk import Orq, OrqClientOptions
from orq_ai_sdk.util import parse_json
from orq_ai_sdk.models import Store, UserInfo


class TestOrq(unittest.TestCase):
    def setUp(self):
        self.valid_options = OrqClientOptions(api_key="valid_api_key")

    def test_init_with_valid_options(self):
        client = Orq(self.valid_options)
        self.assertEqual(client.deployments.options, self.valid_options)

    def test_init_with_no_api_key(self):
        os.environ["ORQ_API_KEY"] = ""
        invalid_options = OrqClientOptions(api_key=None)
        with self.assertRaises(OrqAIInvalidAPIException):
            Orq(invalid_options)

    def test_init_with_api_key_in_env(self):
        os.environ["ORQ_API_KEY"] = "valid_api_key"
        options = OrqClientOptions(api_key=None)
        client = Orq(options)
        self.assertEqual(client.deployments.options, options)


class TestOrqJsonParserUtil(unittest.TestCase):
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


class TestOrqModels(unittest.TestCase):

    def store_creation_with_valid_data():
        user_info = UserInfo(id=1)
        store = Store(api_key="123456", environment="production", user_info=user_info)
        assert store.api_key == "123456"
        assert store.environment == "production"
        assert store.user_info == user_info

    def store_creation_with_no_environment():
        user_info = UserInfo(id=1)
        store = Store(api_key="123456", user_info=user_info)
        assert store.api_key == "123456"
        assert store.environment is None
        assert store.user_info == user_info

    def store_creation_with_no_user_info():
        store = Store(api_key="123456", environment="production")
        assert store.api_key == "123456"
        assert store.environment == "production"
        assert store.user_info is None


if __name__ == "__main__":
    unittest.main()
