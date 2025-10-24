# OpenAI Agents Instrumentation

A comprehensive OpenTelemetry instrumentation package for OpenAI agents with enhanced agent span input/output tracking capabilities.

## Overview

This package provides automatic tracing and telemetry for OpenAI agents using OpenTelemetry. It captures detailed execution traces including agent interactions, LLM calls, tool executions, and handoffs between agents.

## Project Structure

```
openai_agents_instrumentation/
├── __init__.py          # Package entry point and exports
├── constants.py         # Attribute names and span kind definitions
├── instrumentor.py      # Main instrumentation class
├── processor.py         # Custom tracing processor implementation
```

## Files and Their Purposes

### `__init__.py`

**Purpose**: Package initialization and public API definition.

**Key Features**:
- Validates required dependencies (OpenTelemetry and OpenAI Agents)
- Exports the main `OpenAIAgentsInstrumentor` class
- Provides helpful error messages if dependencies are missing

**Exports**:
- `OpenAIAgentsInstrumentor`: The main instrumentation class

### `constants.py`

**Purpose**: Centralized definition of attribute names and span classifications.

**Key Components**:

#### `SpanAttributes` (Enum)
Defines all attribute names used when setting span attributes in OpenTelemetry traces.

**GenAI Semantic Convention Attributes**:
- `OPERATION_NAME`: Operation name (e.g., "agent_run", "llm_call")
- `REQUEST_MODEL`: LLM model identifier
- `USAGE_INPUT_TOKENS`: Number of input tokens consumed
- `USAGE_OUTPUT_TOKENS`: Number of output tokens generated
- `TOOL_NAME`: Name of the tool being called
- `TOOL_CALL_ID`: Unique identifier for tool calls
- `GEN_AI_AGENT_NAME`: Agent name following GenAI conventions

**Orq Custom Attributes**:
- `KIND`: Type of span (workflow, agent, llm, tool, etc.)
- `INPUT_VALUE`: Formatted input data for the span
- `OUTPUT_VALUE`: Formatted output data for the span
- `AGENT_NAME`: Agent name (Orq-specific convention)

#### `SpanKind` (Enum)
Defines the different types of spans that can be created.

**Values**:
- `WORKFLOW`: Top-level workflow/trace
- `AGENT`: Agent execution span
- `LLM`: Large Language Model call span
- `TOOL`: Tool/function execution span
- `GENERIC`: Generic/unknown span type
- `CHAIN`: Chain of operations

### `instrumentor.py`

**Purpose**: Main instrumentation class that sets up and manages OpenTelemetry tracing for OpenAI agents.

**Key Class**: `OpenAIAgentsInstrumentor`

#### Methods

##### `__init__(self, tracer_provider: Optional[TracerProvider] = None)`
Initializes the instrumentor with an optional tracer provider.

**Parameters**:
- `tracer_provider`: Optional OpenTelemetry tracer provider. If not provided, uses the global tracer provider.

**Example**:
```python
instrumentor = OpenAIAgentsInstrumentor()
```

##### `instrument(self) -> None`
Activates instrumentation by setting up the custom tracing processor.

**Behavior**:
- Creates an `EnhancedOpenAIAgentsProcessor` instance
- Sets it as the global tracing processor for OpenAI agents
- Enables automatic trace collection for all agent operations

**Example**:
```python
instrumentor = OpenAIAgentsInstrumentor()
instrumentor.instrument()
```

##### `uninstrument(self) -> None`
Deactivates instrumentation and cleans up resources.

**Behavior**:
- Removes the custom tracing processor
- Stops automatic trace collection
- Flushes any pending traces

**Example**:
```python
instrumentor.uninstrument()
```

### `processor.py`

**Purpose**: Core tracing logic that processes OpenAI agent events and creates OpenTelemetry spans with enhanced input/output tracking.

**Key Class**: `EnhancedOpenAIAgentsProcessor`

Extends OpenAI agents' `TracingProcessor` to provide comprehensive span tracking with detailed input/output capture.

#### Type Aliases

- `SpanInputData`: Union[str, List[Dict], Dict] - Represents span input data
- `SpanOutputData`: Union[str, List[Dict], Dict] - Represents span output data
- `UsageData`: object - Token usage information
- `ErrorData`: Optional[Dict] - Error information for failed spans

#### Instance Variables

##### Span Tracking
- `_tracer`: OpenTelemetry tracer instance
- `_root_spans`: Dict mapping trace IDs to root span objects
- `_otel_spans`: Dict mapping span IDs to OpenTelemetry span objects
- `_tokens`: Dict mapping span IDs to context tokens for proper nesting

##### Agent Input/Output Tracking
- `_agent_spans`: Dict mapping span IDs to agent names for agent-type spans
- `_span_hierarchy`: Dict mapping child span IDs to their parent agent span IDs
- `_agent_inputs`: Dict storing the first LLM input for each agent span
- `_agent_outputs`: Dict storing the last LLM output for each agent span

#### Public Methods

##### `on_trace_start(self, trace: Trace) -> None`
Called when a new trace is initiated.

**Behavior**:
- Creates a root-level workflow span
- Sets appropriate attributes for the trace
- Stores the span for later access

##### `on_trace_end(self, trace: Trace) -> None`
Called when a trace completes.

**Behavior**:
- Sets the span status to OK
- Ends the root span
- Cleans up trace tracking data

##### `on_span_start(self, span: Span[SpanData]) -> None`
Called when a new span begins within a trace.

**Behavior**:
- Creates an OpenTelemetry span with proper parent context
- Sets span kind and operation name attributes
- Tracks agent spans and hierarchy for input/output aggregation
- Initializes agent input/output tracking if needed

##### `on_span_end(self, span: Span[SpanData]) -> None`
Called when a span completes.

**Behavior**:
- Updates span name and attributes
- Routes to appropriate handler based on span type
- Collects input/output data for agent spans
- Sets span status and end time
- Cleans up span tracking data

#### Private Methods - Span Handlers

##### `_handle_agent_span(self, otel_span: OtelSpan, data: AgentSpanData, span_id: str) -> None`
Processes agent-type spans with enhanced input/output tracking.

**Key Features**:
- Sets agent name attributes
- Aggregates first LLM input and last LLM output from child spans
- Formats input as JSON message array
- Formats output using `_format_llm_output`
- Cleans up tracking data after processing

##### `_handle_response_span(self, otel_span: OtelSpan, data: ResponseSpanData) -> None`
Processes LLM response spans.

**Key Features**:
- Extracts and sets model information
- Formats response output data
- Formats input data with system instructions
- Extracts token usage information
- Collects data for parent agent spans

##### `_handle_generation_span(self, otel_span: OtelSpan, data: GenerationSpanData) -> None`
Processes LLM generation spans.

**Key Features**:
- Sets model attribute
- Formats input messages with system instructions
- Formats output messages
- Extracts token usage
- Collects data for parent agent spans

##### `_handle_function_span(self, otel_span: OtelSpan, data: FunctionSpanData) -> None`
Processes tool/function call spans.

**Key Features**:
- Sets tool name attribute
- Sets tool call ID if available
- Captures function input and output

##### `_handle_handoff_span(self, otel_span: OtelSpan, data: HandoffSpanData) -> None`
Processes agent handoff spans (currently minimal implementation).

**Purpose**: Placeholder for future handoff-specific attributes.

#### Private Methods - Data Formatting

##### `_format_llm_input(self, data: SpanData) -> Optional[SpanInputData]`
Formats LLM input data to include system messages from instructions.

**Behavior**:
- Checks if input already contains a system message
- Prepends system message from agent instructions if not present
- Returns formatted message array suitable for LLM APIs

**Input Format**:
```python
[
    {"role": "system", "content": "Agent instructions..."},
    {"role": "user", "content": "User message..."}
]
```

##### `_format_llm_output(self, output_data: SpanOutputData) -> List[Dict[str, object]]`
Formats LLM output into a standardized structure.

**Output Format**:
```python
[
    {
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "Response text..."
        },
        "finish_reason": "stop"
    }
]
```

**Handles**:
- String outputs
- Message objects with content
- Tool call outputs
- Multiple output items

##### `_extract_text_from_output(self, output_data: SpanOutputData) -> Optional[str]`
Extracts plain text content from various output formats.

**Behavior**:
- Handles string, list, and object outputs
- Extracts text from nested content structures
- Returns concatenated text or None

#### Private Methods - Utilities

##### `_collect_agent_data(self, span_id: str, data: SpanData, *data_types: str) -> None`
Aggregates input/output data from child spans to parent agent spans.

**Strategy**:
- First LLM input: Captures only the first input for each agent
- Last LLM output: Always updates to the latest output (last one wins)

**Data Types**:
- `"input"`: Captures formatted LLM input
- `"output"`: Captures LLM output or response output

##### `_find_parent_agent_span(self, parent_id: Optional[str]) -> Optional[str]`
Recursively finds the nearest parent agent span in the hierarchy.

**Use Case**: Links LLM and tool spans to their parent agent for data aggregation.

##### `_get_span_name(self, span: Span[SpanData]) -> str`
Extracts a meaningful name for the span.

**Special Cases**:
- Handoff spans: "handoff to {target_agent_name}"
- Other spans: Uses name attribute or "unknown"

##### `_get_span_kind(self, data: SpanData) -> str`
Determines the appropriate span kind based on data type.

**Mapping**:
- `AgentSpanData` → `SpanKind.AGENT`
- `FunctionSpanData` → `SpanKind.TOOL`
- `GenerationSpanData` → `SpanKind.LLM`
- `ResponseSpanData` → `SpanKind.LLM`
- `HandoffSpanData` → `SpanKind.TOOL`
- Others → `SpanKind.GENERIC`

##### `_get_span_status(self, span: Span[SpanData]) -> Status`
Determines span status based on error information.

**Returns**:
- `Status(StatusCode.ERROR)` with description if span has errors
- `Status(StatusCode.OK)` otherwise

##### `_set_usage_attributes(self, otel_span: OtelSpan, usage: UsageData) -> None`
Sets token usage attributes on the span.

**Attributes Set**:
- Input tokens consumed
- Output tokens generated

##### `_as_utc_nano(self, dt: str) -> int`
Converts ISO format datetime string to nanoseconds since epoch.

**Use Case**: OpenTelemetry requires timestamps in nanoseconds (UTC).

#### Lifecycle Methods

##### `force_flush(self) -> None`
Forces immediate flush of all queued spans/traces (currently no-op).

##### `shutdown(self) -> None`
Called when the application stops (currently no-op).

## Usage Example

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from orq_ai_sdk.openai_agents_instrumentation import OpenAIAgentsInstrumentor

# Set up OpenTelemetry
tracer_provider = TracerProvider()
span_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
span_processor = BatchSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

# Instrument OpenAI agents
instrumentor = OpenAIAgentsInstrumentor(tracer_provider)
instrumentor.instrument()

# Your OpenAI agents code here
# All agent operations will now be automatically traced

# Clean up when done
instrumentor.uninstrument()
```

## Key Features

### Enhanced Agent Span Tracking
- Automatically aggregates first LLM input and last LLM output for agent spans
- Provides complete visibility into agent reasoning flow
- Maintains proper parent-child relationships in span hierarchy

### Comprehensive Data Capture
- LLM inputs with system instructions
- LLM outputs in standardized format
- Token usage tracking
- Tool calls and their arguments
- Agent handoffs

### Flexible Output Formatting
- Supports multiple output formats (strings, objects, lists)
- Extracts structured data from OpenAI response objects
- Handles tool calls and regular messages

### Error Tracking
- Captures and reports span errors
- Sets appropriate status codes
- Includes error descriptions in traces

## Dependencies

- `opentelemetry-sdk`: OpenTelemetry SDK for Python
- `opentelemetry-exporter-otlp`: OTLP exporter for sending traces
- `opentelemetry-instrumentation`: Base instrumentation utilities
- `openai-agents`: OpenAI agents framework

## Architecture Notes

### Span Hierarchy

```
Workflow (root)
└── Agent
    ├── LLM Generation
    │   └── Usage data
    ├── Tool Call
    │   ├── Input
    │   └── Output
    └── Response
        └── Output
```

### Data Flow

1. Agent span starts → Initialize tracking
2. Child LLM/Tool spans execute → Collect input/output
3. Agent span ends → Aggregate and format data
4. Span data exported to OpenTelemetry collector

## Design Decisions

### Why First Input / Last Output?
For agent spans, we capture:
- **First LLM input**: Represents the initial context/instructions given to the agent
- **Last LLM output**: Represents the final result/decision from the agent

This provides the most relevant information for understanding agent behavior without overwhelming the trace with intermediate steps.

### Why Separate Format Methods?
`_format_llm_input` and `_format_llm_output` are separate because:
- They handle different data structures
- Input needs system message injection
- Output needs standardization across multiple formats
- Maintains single responsibility principle

### Why Track Hierarchy?
The hierarchy tracking (`_span_hierarchy`, `_agent_spans`) enables:
- Proper input/output aggregation from child to parent spans
- Understanding which LLM calls belong to which agent
- Supporting nested agent architectures
