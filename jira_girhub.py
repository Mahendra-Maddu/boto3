# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://mahendra-maddu.atlassian.net/rest/api/3/issue"
    API_TOKEN = "ATATT3xFfGF0JxFn5OgLFMdjgFKIgxyhaBTPjiieBa5qQQfarN6R-qnVMj7f5Dc0twIDTl9jLDmHvOCqb4iNVJg44uQn3-CoOU_4FanURoUqwrPQcmrC9YnKlU8td7yKq3oWKpYUhYiGLu0A4Soh_ELi2j-jX8_uEDB089ltesI9UrQnz_0nDi4=4BA39607"

    auth = HTTPBasicAuth("mahendramaddu5@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "text123",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "DV"
        },
        "issuetype": {
            "id": "10011"
        },
        "summary": "Issue",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
