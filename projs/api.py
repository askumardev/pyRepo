import requests

# Sample API request to JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

data = response.json()

for post in data:
    print("Title:", post['title'])
    print("Body:", post['body'])
    print("-" * 40) 


# python3 projs/api.py