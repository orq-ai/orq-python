from agents import Agent, HandoffInputData, Runner, function_tool, handoff, trace as agent_trace   
from agents.extensions import handoff_filters
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

import random
import os

from orq_ai_sdk.openai_agents_instrumentation import OpenAIAgentsInstrumentor

# Set up OpenTelemetry with console exporter for debugging
tracer_provider = TracerProvider()

exporter = os.environ['EXPORTER'] or 'console'

if exporter == 'console':
    tracer_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
elif exporter == 'otlp':
    tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))

# Instrument OpenAI agents with our enhanced processor
OpenAIAgentsInstrumentor().instrument(tracer_provider=tracer_provider)

@function_tool
def random_number_tool(max: int) -> int:
    """Return a random integer between 0 and the given maximum."""
    return random.randint(0, max)

def spanish_handoff_message_filter(handoff_message_data: HandoffInputData) -> HandoffInputData:
    """Filter messages during handoff to Spanish agent"""
    # Remove tool-related messages from the message history
    handoff_message_data = handoff_filters.remove_all_tools(handoff_message_data)

    # Remove the first two items from the history for demonstration
    history = (
        tuple(handoff_message_data.input_history[2:])
        if isinstance(handoff_message_data.input_history, tuple)
        else handoff_message_data.input_history
    )

    return HandoffInputData(
        input_history=history,
        pre_handoff_items=tuple(handoff_message_data.pre_handoff_items),
        new_items=tuple(handoff_message_data.new_items),
    )

# Define agents with specific roles
first_agent = Agent(
    name="Assistant",
    instructions="Be extremely concise.",
    tools=[random_number_tool],
    model='gpt-4o'
)

spanish_agent = Agent(
    name="Spanish Assistant",
    instructions="You only speak Spanish and are extremely concise.",
    handoff_description="A Spanish-speaking assistant.",
    model='gpt-4o'
)

second_agent = Agent(
    name="Assistant",
    instructions="Be a helpful assistant. If the user speaks Spanish, handoff to the Spanish assistant.",
    handoffs=[handoff(spanish_agent, input_filter=spanish_handoff_message_filter)],
    model='gpt-4o'
)

async def run_multi_agent_workflow():
    """Execute a complex multi-agent workflow with tracing"""
    # Trace the entire workflow as a single operation
    with agent_trace(workflow_name="Multi-Agent Message Filtering"):
        print("🤖 Starting multi-agent workflow...")
        
        # Step 1: Initial conversation
        result = await Runner.run(first_agent, input="Hi, my name is Sora.")
        print("✅ Step 1: Initial greeting completed")

        # Step 2: Tool usage (random number generation)
        result = await Runner.run(
            first_agent,
            input=result.to_input_list() + [
                {"content": "Can you generate a random number between 0 and 100?", "role": "user"}
            ],
        )
        print("✅ Step 2: Random number generation completed")

        # Step 3: Information query
        result = await Runner.run(
            second_agent,
            input=result.to_input_list() + [
                {"content": "I live in New York City. What's the population of the city?", "role": "user"}
            ],
        )
        print("✅ Step 3: Information query completed")

        # Step 4: Language switch triggers handoff
        result = await Runner.run(
            second_agent,
            input=result.to_input_list() + [
                {"content": "Por favor habla en español. ¿Cuál es mi nombre y dónde vivo?", "role": "user"}
            ],
        )
        print("✅ Step 4: Spanish handoff completed")

    print("\n📊 Final conversation history:")
    for i, message in enumerate(result.to_input_list(), 1):
        print(f"{i}. {message['role']}: {message['content'][:100]}...")

async def main():
    # Run the workflow
    await run_multi_agent_workflow()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())