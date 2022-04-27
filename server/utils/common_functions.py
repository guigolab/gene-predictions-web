import os
from flask import current_app as app

API_KEY = os.getenv('API_KEY')

def resolve_params(allowed_params, **params):
  # add default params if not present
  for k,v in params.items():
    if k in allowed_params.keys():
        allowed_params[k] = v
  return allowed_params


def auth_request(api_key):
  return api_key == API_KEY
