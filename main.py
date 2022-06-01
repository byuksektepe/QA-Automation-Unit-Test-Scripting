import requests

def api():

    url = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(url)

    print(response)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
