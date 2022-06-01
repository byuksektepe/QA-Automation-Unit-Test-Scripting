import requests

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

        print(response.json()) #gives auth error
        response = requests.get(url, auth=('djw-test', 'klklkllkl'))
        print(response.json())  #user data comes


if __name__ == '__main__':

    main.rest_api_auth()

