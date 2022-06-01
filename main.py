import requests

def rest_api():

    url = "https://jsonplaceholder.typicode.com/photos"
    response_get = requests.get(url)

    # print(response.json())
    jsonPayload = {'albumId':1, 'title':'test',
                   'url':'thisisatesturl.com', 'thumbnailUrl':'thisisatesturl.com'}

    response_post = requests.post(url, json=jsonPayload)
    response_post.json()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rest_api()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
