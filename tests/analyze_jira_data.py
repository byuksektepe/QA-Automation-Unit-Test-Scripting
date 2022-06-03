import requests

class rest_api:
    def start(self):

        url = "http://jira.<company name>/rest/api/latest/search?jql=reporter=dwesterveld"
        response = requests.get(url)

        return response
    pass