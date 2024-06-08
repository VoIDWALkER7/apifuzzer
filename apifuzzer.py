import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url='https://jsonplaceholder.typicode.com/posts/1')
        
        if res.status_code == 404:
            # Avoiding infinite recursion by breaking the loop or taking another action
            print("404 Not Found. Exiting loop.")
            loop()
        
        print(res.status_code)
        try:
            data = res.json()
            print(data)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print("Response content is not valid JSON")

loop()
