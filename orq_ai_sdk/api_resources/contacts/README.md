# Contacts

The Contacts API allows you to create and manage contact information in the orq.ai API. This is useful for associating
user data with AI interactions.

## Set the contact using the client

To set a contact ID in the store and create a contact simultaneously, use the exposed `set_contact` method from the
client:

```python:
client.set_contact(
    id="user123",
    display_name="John Doe",
    email="john@example.com",
    avatar_url="https://example.com/avatar.jpg",
    metadata={"role": "admin"}
)
```

This method combines setting the contact ID in the store and creating a contact in one operation.

## Creating a Contact

To create a contact, use the `create` method of the `client.contacts`:

```python
contact = client.contacts.create(
    external_id="user123",
    display_name="John Doe",
    email="john@example.com",
    avatar_url="https://example.com/avatar.jpg",
    metadata={"role": "admin"}
)
```

## Asynchronous Creation

For asynchronous operations, use the `acreate` method:

```python
contact = await client.contacts.acreate(
    external_id="user123",
    display_name="John Doe",
    email="john@example.com",
    avatar_url="https://example.com/avatar.jpg",
    metadata={"role": "admin"}
)
```

## Best Practices

1. Always provide a unique `external_id` for each contact. This helps in identifying and managing contacts in your
   system.

2. Handle errors appropriately when creating contacts, as network issues or validation errors may occur.

3. Use the asynchronous `acreate` method for better performance in asynchronous applications.

4. Ensure that the `email` and `avatar_url` fields, if provided, are in valid formats to avoid validation errors.

5. Use the `metadata` field to store additional information about the contact that doesn't fit into the standard fields.

## API Reference

### `create(external_id: str, display_name: str | None = None, email: str | None = None, avatar_url: str | None = None, metadata: dict | None = None) -> Contact`

Creates a new contact in the orq.ai API.

- `external_id`: str - Required. An external identifier for the user.
- `display_name`: str | None - Optional. The user's display name or full name.
- `email`: str | None - Optional. The user's email address.
- `avatar_url`: str | None - Optional. URL to the user's avatar image.
- `metadata`: dict | None - Optional. Additional key-value pairs for storing extra user information.

Returns a `Contact` object.

### `acreate(external_id: str, display_name: str | None = None, email: str | None = None, avatar_url: str | None = None, metadata: dict | None = None) -> Contact`

Asynchronously creates a new contact in the orq.ai API. Parameters are the same as `create`.

Returns a `Contact` object.

## Error Handling

- If `external_id` is not provided, a `ValueError` will be raised.
- If the API request fails, an HTTP error will be raised. You should handle these exceptions in your code.

## Example

```python
try:
    contact = client.contacts.create(
        external_id="user123",
        display_name="John Doe",
        email="john@example.com",
        avatar_url="https://example.com/avatar.jpg",
        metadata={"role": "admin", "department": "IT"}
    )
    print(f"Contact created: {contact.id}")
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```