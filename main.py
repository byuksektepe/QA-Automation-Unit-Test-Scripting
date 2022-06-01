import requests

class main:

    url = "https://jsonplaceholder.typicode.com/photos"

    def rest_api_get():


        response = requests.get(main.url)

        print(response.json())


    def rest_api_post():
        jsonPayload = {'albumId':1, 'title':'test',
                       'url':'thisisatesturl.com', 'thumbnailUrl':'thisisatesturl.com'}

        response = requests.post(main.url, json=jsonPayload)
        print(response.json())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.rest_api_post()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
