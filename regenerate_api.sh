#!/bin/bash
__doc__="
Basic instructions to regenerate the openapi client
"

curl -o jellyfin-openapi-stable.json https://api.jellyfin.org/openapi/jellyfin-openapi-stable.json

uv pip install "openapi-python-client!=0.28.0"

mkdir -p jellyfin_apiclient_python/openapi/_generated

openapi-python-client generate \
  --path jellyfin-openapi-stable.json \
  --output-path ./jellyfin_apiclient_python/openapi/_generated \
  --meta=none \
  --overwrite

# Checks
python -c "if 1:
    from jellyfin_openapi.client import AuthenticatedClient
    from jellyfin_openapi.models import AuthenticateUserByName

    # auth = AuthenticateUserByName(username='jellyfin', pw='')
    from jellyfin_openapi import Client, AuthenticatedClient
    from jellyfin_openapi.api.user import authenticate_user_by_name
    from jellyfin_openapi.models import AuthenticateUserByName
"
