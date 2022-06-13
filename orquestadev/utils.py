def is_invalid_api_key(key):
    return not key.startswith('RQST')
