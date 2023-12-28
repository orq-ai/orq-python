Configuration
-------------
.. py:currentmodule:: orquesta_sdk

Configuration is handled via the ``OrquestaClientOptions`` class

.. code:: python

    # Configure client options example

    from orquesta_sdk import OrquestaClientOptions

    options = OrquestaClientOptions(
        api_key=api_key,
        environment="production"
    )
    
Configuration settings:

.. _api_key:

api_key
~~~~~~~~

The API key to use for authentication.

.. note::
    If you are using the Orquesta API, you must provide an API key. You can also declare ``ORQUESTA_API_KEY`` as environment variable with the API key

environment
~~~~~~~~~~~~~~

The environment to append as part of the context attributes in every request.
