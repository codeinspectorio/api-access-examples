from sgqlc.endpoint.http import HTTPEndpoint

url = 'https://api.code-inspector.com/graphql'

# Getting the JWT first
query = '''
mutation{
  authentication(identifier:"<USERNAME>", password: "<PASSWORD>"){
    token
    error
  }
}
'''
variables = {}

endpoint = HTTPEndpoint(url)
data = endpoint(query, variables)
token = data['data']['authentication']['token']


# Querying with the JWT
query = '''
{
   user {
      username
   }
}
'''

headers = {
    'Authorization': token
}

endpoint = HTTPEndpoint(url, headers)
data = endpoint(query, variables)

print(data)