# environment variables can be set in .env file by using the following format:
# VARIABLE_NAME=VARIABLE_VALUE
# example:
# port=/tes/tport123
# baudrate=123456

# # read all environment variables from .env file
environment_variables = {}
with open('.env') as f:
    for line in f:
        if line[0] != '#':
            key, value = line.split('=')
            environment_variables[key] = value.strip()