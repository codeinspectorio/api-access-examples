# Code Inspector API Access Examples

Code Samples to access the Code Inspector API.

## Python

There are two files that demonstrate how to authenticate
against the GraphQL API using Python:

 * [auth-api-key.py](auth-api-key.py): authentication using the access and secret keys
 * [auth-jwt.py](auth-jwt.py): authentication using username and password to get a JWT

These examples use [sgqlc](https://github.com/profusion/sgqlc) to query
the GraphQL API.

Below if the sequence of shell commands to run to create a virtual environment,
install the dependencies and run them. Keep in mind that you need to edit the 
files with your credentials in order for the examples to work.

```bash 
# cd python
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

< edit file auth-api-key.py with your credentials >

# python auth-api-key.py

< edit file auth-jwt.py with your credentials >

# python auth-jwt.py

```

# Contribute

Found a bug or want to suggest improvements? Feel free to open an issue.
Have more examples you want to add? Send us a pull requuest!

# Support

Have suggestion or questions? [Contact us](https://www.code-inspector.com/contact).