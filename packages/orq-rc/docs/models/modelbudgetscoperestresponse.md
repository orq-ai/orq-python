# ModelBudgetScopeRestResponse

Per-model cap. The value is the FULL model reference as callers send
 it ("openai/gpt-4o", or "workspaceKey@openai/gpt-4o" for private
 models) — NOT the Mongo `_id` of the model master-data document.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `model_id`         | *str*              | :heavy_check_mark: | N/A                |