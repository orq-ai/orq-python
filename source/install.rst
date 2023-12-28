Installation
============
.. py:currentmodule:: orquesta-sdk

-  Install the latest version with pip::

    $ pip install orquesta-sdk

- Get your workspace API key

    You can get your workspace API key from the settings section in your Orquesta workspace. `https://my.orquesta.dev/<workspace>/settings/developers`

- Initialize the SDK

    Initialize the SDK with your workspace API key. You can also set the `ORQUESTA_API_KEY` environment variable to avoid passing the API key in the code.

    .. code-block:: python

        import os

        from orquesta_sdk import Orquesta, OrquestaClientOptions

        api_key = os.environ.get("ORQUESTA_API_KEY", "__API_KEY__")

        options = OrquestaClientOptions(
            api_key=api_key,
            ttl=3600,
            environment="production"
        )

        client = Orquesta(options)