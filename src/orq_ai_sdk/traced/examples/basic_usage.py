"""Basic usage example of Orq decorator SDK."""

import time
from traced import init, get_client, traced


# Initialize the SDK
init(
    api_key="your-api-key-here",
    debug = True,
    enabled = True
)

# Custom span attributes
@traced(
    name="Custom lLM",
    attributes={"version": "1.0", "feature": "user-processing"}
)
def process_user(user_id: str, action: str) -> dict:
    print('process user')
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

@traced
def calculate_fibonacci(n: int) -> int:
    """Calculate fibonacci number recursively."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

# Disable input/output capture for sensitive data
@traced(
    capture_input=False,
    capture_output=False
)
def process_sensitive_data(password: str, credit_card: str) -> str:
    """Process sensitive data without capturing it."""
    # The password and credit_card values won't be sent to Orq
    return "processed"

def main():
    process_user('1234', 'test')
    calculate_fibonacci(1)
    process_sensitive_data("111111", "1234567")

if __name__ == '__main__':
    main()