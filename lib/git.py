import requests

def get_user_events(user):
    return requests.get(f'https://api.github.com/users/{user}/events').json()
