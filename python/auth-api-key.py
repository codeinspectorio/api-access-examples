from sgqlc.endpoint.http import HTTPEndpoint

url = 'https://api.code-inspector.com/graphql'
headers = {
    'X-Access-Key': '<ACCESS-KEY>',
    'X-Secret-Key': '<SECRET-KEY>'
}

query = '{user {username} }'
variables = {}

endpoint = HTTPEndpoint(url, headers)
data = endpoint(query, variables)
print(data['data']['user']['username'])