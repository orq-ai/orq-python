# CreateNotifierRequest

Create notifier request. `project_id`, `display_name`, and `type` are always required. The destination field required by `type` is captured in `oneOf`.


## Supported Types

### `models.EmailNotifierCreateRequest`

```python
value: models.EmailNotifierCreateRequest = /* values here */
```

### `models.SlackWebhookNotifierCreateRequest`

```python
value: models.SlackWebhookNotifierCreateRequest = /* values here */
```

### `models.GenericWebhookNotifierCreateRequest`

```python
value: models.GenericWebhookNotifierCreateRequest = /* values here */
```

