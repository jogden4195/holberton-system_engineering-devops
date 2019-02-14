#!/usr/bin/python3
"""
Module for top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit
    """
    headers = {
        'User-Agent': 'Someone',
        'Content-Type': 'application/json'}
    url = 'http://www.reddit.com/r/' + subreddit + '/hot.json'
    data = requests.get(url, headers=headers)
    if data.status_code != 200:
        print('None')
        return
    data_json = data.json()
    posts = data_json['data']['children']
    if len(posts) == 0:
        print('None')
        return
    for p in posts[:9]:
        print(p['data']['title'])
