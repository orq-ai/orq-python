import unittest
from orq_ai_sdk.messages import AssistantMessage, UserMessage


class TestMessages(unittest.TestCase):
    def test_assistant_message(self):
        content = "Hello, how can I assist you?"
        message = AssistantMessage(content=content)
        self.assertEqual(message.role, "assistant")
        self.assertEqual(message.content, content)
        self.assertEqual(
            message.to_dict(),
            {"role": "assistant", "content": "Hello, how can I assist you?"},
        )

    def test_user_message(self):
        content = "I need help with my account"
        message = UserMessage(content=content)
        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, content)
        self.assertEqual(
            message.to_dict(),
            {"role": "user", "content": "I need help with my account"},
        )
