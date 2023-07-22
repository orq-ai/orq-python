class OrquestaOpenAIPromptParameters:
    def __init__(self, parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.max_tokens = parameters.get("maxTokens")
        self.top_p = parameters.get("topP")
        self.frequency_penalty = parameters.get("frequencyPenalty")
        self.presence_penalty = parameters.get("presencePenalty")


class OrquestaCoherePromptParameters:
    def __init__(self, parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.max_tokens = parameters.get("maxTokens")
        self.k = parameters.get("topK")
        self.p = parameters.get("topP")
        self.frequency_penalty = parameters.get("frequencyPenalty")
        self.presence_penalty = parameters.get("presencePenalty")


class OrquestaAnthropicPromptParameters:
    def __init__(self, parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.max_tokens_to_sample = parameters.get("maxTokens")
        self.top_k = parameters.get("topK")
        self.top_p = parameters.get("topP")


class OrquestaReplicatePromptParameters:
    def __init__(self, parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.max_length = parameters.get("maxTokens")
        self.top_p = parameters.get("topP")
        self.repetition_penalty = parameters.get("repetitionPenalty")


class OrquestaGooglePromptParameters:
    def __init__(self, parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.maxOutputTokens = parameters.get("maxTokens")
        self.topK = parameters.get("topK")
        self.topP = parameters.get("topP")


class OrquestaHuggingFacePromptParameters:
    def __init__(self,parameters: dict):
        self.model = parameters.get("model")
        self.temperature = parameters.get("temperature")
        self.max_new_tokens = parameters.get("maxTokens")
        self.top_p = parameters.get("topP")
        self.top_k = parameters.get("topK")
        self.repetition_penalty = parameters.get("repetitionPenalty")


def orquesta_openai_parameters_mapper(prompt) -> OrquestaOpenAIPromptParameters:
    return OrquestaOpenAIPromptParameters(prompt)


def orquesta_cohere_parameters_mapper(prompt) -> OrquestaCoherePromptParameters:
    return OrquestaCoherePromptParameters(prompt)


def orquesta_anthropic_parameters_mapper(prompt: dict) -> OrquestaAnthropicPromptParameters:
    return OrquestaAnthropicPromptParameters(prompt)


def orquesta_replicate_parameters_mapper(prompt: dict) -> OrquestaReplicatePromptParameters:
    return OrquestaReplicatePromptParameters(prompt)


def orquesta_google_parameters_mapper(prompt: dict) -> OrquestaGooglePromptParameters:
    return OrquestaGooglePromptParameters(prompt)


def orquesta_huggingface_parameters_mapper(prompt: dict) -> OrquestaHuggingFacePromptParameters:
    return OrquestaHuggingFacePromptParameters(prompt)
