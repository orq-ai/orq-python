from orquesta_sdk import Orquesta, OrquestaClientOptions

### Intialize the Orquesta client

client_options = OrquestaClientOptions(
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6ImUzYTIwMmE2LTQ2MWItNDQ3Yy1hYmUyLTAxOGJhNGQwNGNkMCIsImlhdCI6MTY5NzEyNTQ1NDczN30.3kBW_RfS104S2DAlSvPpr3tQiq15nTxNuUv2gE0Nxd0",
    environment="production",
)

client = Orquesta(options=client_options)

deployment = client.deployments.invoke_with_stream(
    key="withFallback", metadata={"name": "test"}
)

for chunk in deployment:
    if chunk.is_final:
        print("Stream is finished")
