import requests
import json

class rest_api:

    def start(self):

        url = "http://jira.<company name>/rest/api/latest/search?jql=reporter=dwesterveld"
        response = requests.get(url)

        return response
    pass

class analyze_jira_data_test:

    def start(self):

        json_data = open('./tests/test_docs/JiraData.json').read()
        data = json.loads(json_data)

        status_counts = {}
        for project in data['projects']:
            for issue in project['issues']:
                status = issue['status']
                if not status in status_counts.keys():
                    status_counts[status] = 1
                else:
                    status_counts[status] = status_counts[status] + 1

        print(status_counts)
