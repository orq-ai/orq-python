# AuthMode

Where the AWS credentials come from. integration reads static AWS access keys from the integration named by integration_id, which is required with it. pod-identity resolves credentials from the AWS default credential chain of the deployment, such as EKS Pod Identity, IAM Roles for Service Accounts or the instance metadata service, and ignores integration_id; set assume_role_arn to assume a role in another account and assume_role_external_id to pass the external ID that role's trust policy requires.

## Example Usage

```python
from orq_ai_sdk.models import AuthMode
value: AuthMode = "integration"
```


## Values

- `"integration"`
- `"pod-identity"`
