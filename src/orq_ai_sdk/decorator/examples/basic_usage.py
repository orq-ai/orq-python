"""Basic usage example of Orq decorator SDK."""

import time
from orq.decorator import init, get_client, traced


# Initialize the SDK
init(
    api_key="your-api-key-here"
)


# Simple function tracing
traced
def calculate_fibonacci(n: int) -> int:
    """Calculate fibonacci number recursively."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


# Custom span attributes
traced(
    name="process_user_data",
    attributes={"version": "1.0", "feature": "user-processing"}
)
def process_user(user_id: str, action: str) -> dict:
    """Process user data with custom attributes."""
    # Simulate some processing
    time.sleep(0.1)
    
    result = {
        "user_id": user_id,
        "action": action,
        "status": "completed",
        "timestamp": time.time()
    }
    
    return result


# Nested function calls
traced(name="fetch_data")
def fetch_user_data(user_id: str) -> dict:
    """Fetch user data from database."""
    # Simulate database query
    time.sleep(0.05)
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    }


traced(name="validate_data")
def validate_user_data(data: dict) -> bool:
    """Validate user data."""
    # Simulate validation
    time.sleep(0.02)
    return all(key in data for key in ["id", "name", "email"])


traced(name="save_data")
def save_user_data(data: dict) -> bool:
    """Save user data."""
    # Simulate save operation
    time.sleep(0.03)
    return True


traced(name="user_workflow", type="span.chain")
def complete_user_workflow(user_id: str) -> dict:
    """Complete user workflow with multiple steps."""
    # This creates nested spans
    data = fetch_user_data(user_id)
    
    if validate_user_data(data):
        save_user_data(data)
        return {"status": "success", "data": data}
    else:
        return {"status": "failed", "error": "validation_failed"}


# Error handling
traced(name="risky_operation")
def risky_operation(should_fail: bool = False):
    """Demonstrate error tracking."""
    if should_fail:
        raise ValueError("Operation failed as requested")
    return "Success!"


# Disable input/output capture for sensitive data
traced(
    name="process_sensitive_data",
    capture_input=False,
    capture_output=False
)
def process_sensitive_data(password: str, credit_card: str) -> str:
    """Process sensitive data without capturing it."""
    # The password and credit_card values won't be sent to Orq
    return "processed"


def main():
    """Run examples."""
    print("Running Orq decorator SDK examples...")
    
    # Example 1: Simple function
    print("\n1. Simple function tracing:")
    result = calculate_fibonacci(5)
    print(f"   Fibonacci(5) = {result}")
    
    # Example 2: Custom attributes
    print("\n2. Custom attributes:")
    result = process_user("user123", "update_profile")
    print(f"   Result: {result}")
    
    # Example 3: Nested traces
    print("\n3. Nested function calls:")
    result = complete_user_workflow("user456")
    print(f"   Workflow result: {result}")
    
    # Example 4: Error handling
    print("\n4. Error handling:")
    try:
        risky_operation(should_fail=True)
    except ValueError as e:
        print(f"   Caught expected error: {e}")
    
    # Example 5: Sensitive data
    print("\n5. Sensitive data handling:")
    result = process_sensitive_data("secret123", "4111111111111111")
    print(f"   Result: {result}")
    
    # Ensure all spans are sent
    get_client().flush()
    print("\nAll spans have been sent to Orq!")


if __name__ == "__main__":
    main()