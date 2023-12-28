from orquesta_sdk import Orquesta, OrquestaClientOptions

### Intialize the Orquesta client

options = OrquestaClientOptions(
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6ImUzYTIwMmE2LTQ2MWItNDQ3Yy1hYmUyLTAxOGJhNGQwNGNkMCIsImlhdCI6MTY5NzEyNTQ1NDczN30.3kBW_RfS104S2DAlSvPpr3tQiq15nTxNuUv2gE0Nxd0",
    environment="production",
)

client = Orquesta(options)

deployment = client.deployments.get_config(
    key="withFallback",
    context={"environments": "production", "country": "NLD"},
    inputs={"firstname": "John", "city": "New York"},
    metadata={"customer_id": "Qwtqwty90281"},
)

print(deployment.to_dict())

deployment.add_metrics(
    chain_id="c4a75b53-62fa-401b-8e97-493f3d299316",
    conversation_id="ee7b0c8c-eeb2-43cf-83e9-a4a49f8f13ea",
    user_id="e3a202a6-461b-447c-abe2-018ba4d04cd0",
    feedback={"score": 100},
    metadata={
        "custom": "custom_metadata",
        "chain_id": "ad1231xsdaABw",
    },
    usage={
        "prompt_tokens": 100,
        "completion_tokens": 900,
        "total_tokens": 1000,
    },
    performance={
        "latency": 9000,
        "time_to_first_token": 250,
    },
)

# for chunk in deployment:
#     if chunk.is_final:
#         print("Stream is finished")
