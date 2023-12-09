import json
import requests

import access.endpoint


api_address = "https://the-one-api.dev/v2"
api_key = {"Authorization": "Bearer Dtc0sK3rWKVp2asbK0PS"}


def make_request(key_endpoint, id_research=''):

    temporary_dict = access.endpoint.create_endpoints(id_research)
    address_requested = f'{api_address}{temporary_dict[key_endpoint][0]}'

    try:
        request = requests.get(address_requested, headers=api_key)
        dict_required = json.loads(request.text)

    except Exception as ex:
        dict_required = {'docs': [{'name': 'Error on request', '_id': f'{ex}'}], 'total': 'xx',
                         'limit': 'xx', 'offset': 'xx', 'page': 'xx', 'pages': 'xx'}

    return dict_required
