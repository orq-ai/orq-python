def orquesta_openai_parameters_mapper(prompt):
    parameters = {
        "temperature": prompt.get("temperature"),
        "max_tokens": prompt.get("maxTokens"),
        "top_p": prompt.get("topP"),
        "frequency_penalty": prompt.get("frequencyPenalty"),
        "presence_penalty": prompt.get("presencePenalty"),
    }

    functions = prompt.get("functions", None)

    if functions is not None:
        parameters["functions"] = functions

    return parameters


def orquesta_cohere_parameters_mapper(prompt):
    return {
        "temperature": prompt.get("temperature"),
        "max_tokens": prompt.get("maxTokens"),
        "k": prompt.get("topK"),
        "p": prompt.get("topP"),
        "frequency_penalty": prompt.get("frequencyPenalty"),
        "presence_penalty": prompt.get("presencePenalty"),
    }


def orquesta_anthropic_parameters_mapper(prompt):
    return {
        "temperature": prompt.get("temperature"),
        "max_tokens_to_sample": prompt.get("maxTokens"),
        "top_k": prompt.get("topK"),
        "top_p": prompt.get("topP"),
    }


def orquesta_replicate_parameters_mapper(prompt):
    return {
        "temperature": prompt.get("temperature"),
        "max_length": prompt.get("maxTokens"),
        "top_p": prompt.get("topP"),
        "repetition_penalty": prompt.get("repetitionPenalty"),
    }


def orquesta_google_parameters_mapper(prompt):
    return {
        "temperature": prompt.get("temperature"),
        "maxOutputTokens": prompt.get("maxTokens"),
        "topK": prompt.get("topK"),
        "topP": prompt.get("topP"),
    }


def orquesta_huggingface_parameters_mapper(prompt):
    return {
        "temperature": prompt.get("temperature"),
        "max_new_tokens": prompt.get("maxTokens"),
        "top_p": prompt.get("topP"),
        "top_k": prompt.get("topK"),
        "repetition_penalty": prompt.get("repetitionPenalty"),
    }
