import json


def json_response(data, status=200):
    """Return a JSON response"""
    response_body = json.dumps(data)
    headers = [('Content-Type', 'application/json')]
    return status, headers, response_body.encode()
def get_json(environ):
    try:
        length = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(length)
        return json.loads(body)
    except:
        return None