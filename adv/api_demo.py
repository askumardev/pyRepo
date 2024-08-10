# python3 adv/api_demo.py

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Resource not found.')
elif response.status_code == 500:
    print('Server error.')
elif response.status_code == 401:
    print('Unauthorized. Authentication required.')
elif response.status_code == 403:
    print('Forbidden. Access denied.')
else:
    print(f'Error: {response.status_code}')