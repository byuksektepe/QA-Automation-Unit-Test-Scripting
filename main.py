import requests

class main:

    url = "https://jsonplaceholder.typicode.com/photos"
    jsonPayload = {'albumId': 1, 'title': 'test',
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.rest_api_put()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
