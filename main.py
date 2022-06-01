import time

import requests
from tests.read_in_data import read_in_data_test_timing_data
from tests.google_chart_api import google_chart_api_test_timing_data

class main:

    url = "https://jsonplaceholder.typicode.com/photos"
    jsonPayload = {'albumId': 6000, 'title': 'test',
                   'url': 'thisisatesturl.com', 'thumbnailUrl': 'thisisatesturl.com'}

    def rest_api_get():

        response = requests.get(main.url)
        print(response.json())
    pass

    def rest_api_post():

        response = requests.post(main.url, json=main.jsonPayload)
        print(response.json())
    pass

    def rest_api_put():

        response = requests.put(main.url, json=main.jsonPayload)
        print(response.json())
    pass

    def rest_api_delete():
        response = requests.delete(main.url)
        print(response)
    pass

    def rest_api_auth():
        url = "https://api.github.com/user"
        response = requests.get(url)

        response = requests.get(url, auth=('djw-test', 'password1'))
        print(response.json())  #user data comes
    pass

    def ch1():

        response = requests.get(main.url)
        json_data = response.json()

        url_list = []
        for photo in json_data:
            url_list.append(photo['url'])

        # see list len
        list_len = len(url_list)
        print("Raw Length: "+str(list_len))

        # see set len
        set_len = len(set(url_list))
        print("Set Length: "+str(set_len)+" / Photos using same url: "+str(list_len-set_len))



if __name__ == '__main__':
    read_in_data_test = read_in_data_test_timing_data().start()
    google_chart_api_test = google_chart_api_test_timing_data().start()
    #main.ch1()

