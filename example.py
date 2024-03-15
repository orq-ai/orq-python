import asyncio

""" import asyncio

from orq_ai_sdk import Orq, OrqClientOptions

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6ImUzYTIwMmE2LTQ2MWItNDQ3Yy1hYmUyLTAxOGJhNGQwNGNkMCIsImlhdCI6MTcwNjc4NDAzNzgxOX0.p_qCAoL0fWPZy1RxC4_MlX0PO8vf4TLmfbTTMEaAVR0"

options = OrqClientOptions(
    api_key=api_key,
    environment="production",
)

client = Orq(options)


async def main():

    # Streaming
    # deployment_stream = client.deployments.ainvoke_with_stream(
    #     key="gpt_function_generator",
    #     context={"environments": []},
    #     metadata={"custom-field-name": "custom-metadata-value"},
    # )

    # async for chunk in deployment_stream:
    #     print("Received data:", chunk)

    #     if getattr(chunk, "is_final", False):
    #         print("Stream is finished")
    #         deployment_stream.aclose()
    #         break

    deployment = await client.deployments.ainvoke(
        key="gpt_function_generator",
        context={"environments": []},
    )

    await deployment.aadd_metrics(metadata={"chain_id": "2330"})


# Run the main function
asyncio.run(main())


# deployment_stream = client.deployments.invoke_with_stream(
#     key="gpt_function_generator",
#     context={"environments": []},
#     metadata={"custom-field-name": "custom-metadata-value"},
# )

# for chunk in deployment_stream:
#     print("Received data:", chunk)

#     if getattr(chunk, "is_final", False):
#         print("Stream is finished")
#         break

# deployment = client.deployments.invoke(
#     key="gpt_function_generator",
#     context={"environments": []},
#     metadata={"custom-field-name": "custom-metadata-value"},
# )

# print(deployment)
 """

from orq_ai_sdk import AsyncOrqAI

client = AsyncOrqAI(
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6ImUzYTIwMmE2LTQ2MWItNDQ3Yy1hYmUyLTAxOGJhNGQwNGNkMCIsImlhdCI6MTcwNjc4NDAzNzgxOX0.p_qCAoL0fWPZy1RxC4_MlX0PO8vf4TLmfbTTMEaAVR0",
    environment="production",
)


async def main():
    prompt_config = await client.deployments.get_config(
        key="gpt_function_generator",
        context={"environments": []},
    )

    print(prompt_config)


asyncio.run(main())
