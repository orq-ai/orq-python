import unittest

from orquesta_sdk.helpers import OrquestaOpenAIPromptParameters, orquesta_openai_parameters_mapper, \
    OrquestaCoherePromptParameters, orquesta_cohere_parameters_mapper, orquesta_anthropic_parameters_mapper, \
    OrquestaAnthropicPromptParameters


class TestMappers(unittest.TestCase):
    params = {
        "model": 'curie',
        "temperature": 0.5,
        "maxTokens": 50,
        "topP": 0.3,
        "topK": 1,
        "frequencyPenalty": 0.5,
        "presencePenalty": 0.5
    }

    def test_openai_mapper(self):

        actual = orquesta_openai_parameters_mapper(self.params)
        self.assertTrue(isinstance(actual, OrquestaOpenAIPromptParameters))
        self.assertEqual(self.params['model'], actual.model)
        self.assertEqual(self.params['temperature'], actual.temperature)
        self.assertEqual(self.params['maxTokens'], actual.max_tokens)
        self.assertEqual(self.params['topP'], actual.top_p)
        self.assertEqual(self.params['frequencyPenalty'], actual.frequency_penalty)
        self.assertEqual(self.params['presencePenalty'], actual.presence_penalty)

    # Tests for other mappers

    def test_cohere_mapper(self):
        actual = orquesta_cohere_parameters_mapper(self.params)
        self.assertTrue(isinstance(actual, OrquestaCoherePromptParameters))
        self.assertEqual(self.params['model'], actual.model)
        self.assertEqual(self.params['temperature'], actual.temperature)
        self.assertEqual(self.params['maxTokens'], actual.max_tokens)
        self.assertEqual(self.params['topP'], actual.p)
        self.assertEqual(self.params['topP'], actual.p)
        self.assertEqual(self.params['frequencyPenalty'], actual.frequency_penalty)
        self.assertEqual(self.params['presencePenalty'], actual.presence_penalty)

    def test_anthropic_mapper(self):
        actual = orquesta_anthropic_parameters_mapper(self.params)
        self.assertTrue(isinstance(actual, OrquestaAnthropicPromptParameters))
        self.assertEqual(self.params['model'], actual.model)
        self.assertEqual(self.params['temperature'], actual.temperature)
        self.assertEqual(self.params['maxTokens'], actual.max_tokens_to_sample)
        self.assertEqual(self.params['topP'], actual.top_p)
        self.assertEqual(self.params['topK'], actual.top_k)
