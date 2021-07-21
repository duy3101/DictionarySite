

import requests
import json

#key for oxford: a327e01ada6549688808399f6cc2304e
app_id = "a0ba505c"
app_key = "a327e01ada6549688808399f6cc2304e"

def main():
    url = make_url("apple")
    result = get_request(url)
    # for entry in result:
    print(result)

#make url to call oxford
def make_url(word):
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/"
    url += word
    url += "?fields=definitions&strictMatch=false"
    return url

#GET request from oxford
#convert result to json list
#return result
def get_request(url):
    response =requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    result = response.json()
    return result

def function():
    pass

def function2():
    pass

if __name__ == '__main__':
    main()
