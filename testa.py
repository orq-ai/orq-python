import time

import openai

from orquesta_sdk import OrquestaClient, OrquestaClientOptions
from orquesta_sdk.helpers import orquesta_openai_parameters_mapper
from orquesta_sdk.prompts import OrquestaPromptMetrics

openai.api_key = "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"

# ORQUESTA_API_KEY and OPENAI_API_KEY should be set as environment variables
# before using the library

# Initialize Orquesta client
options = OrquestaClientOptions(
    api_key="RQST.2abc62ce4fdd4db4967d1ee3bbaabd8d.0OZd0jCsHdsGQN8pqGoJU9eXW28"
)

client = OrquestaClient(options)

prompt = client.prompts.query(
    key="job-description-summary",
    context={"environments": "production"},
    variables={
        "jobDescription": "Passionate and self-driven Senior Full-Stack Developer with a focus on NodeJS + React or similar technologies. Bring at least 5 years of experience in full-stack development and a willingness to learn React. This remote position offers the flexibility to work from anywhere while contributing to groundbreaking technology solutions."
    },
)

if prompt.has_error:
    print("There was an error while fetching the prompt")

# Start time of the completion request
start_time = time.time()

completion = openai.ChatCompletion.create(
    **orquesta_openai_parameters_mapper(prompt.value),
    model=prompt.value.get("model"),
    messages=prompt.value.get("messages"),
)

# End time of the completion request
end_time = time.time()

# Calculate the difference (latency) in milliseconds
latency = (end_time - start_time) * 1000

# Report the metrics back to Orquesta
metrics = OrquestaPromptMetrics(
    economics={
        "total_tokens": completion.usage.get("total_tokens"),
        "completion_tokens": completion.usage.get("completion_tokens"),
        "prompt_tokens": completion.usage.get("prompt_tokens"),
    },
    llm_response=completion.choices[0].message.content,
    latency=latency,
    metadata={
        "finish_reason": completion.choices[0].finish_reason,
    },
)

prompt.add_metrics(metrics=metrics)
