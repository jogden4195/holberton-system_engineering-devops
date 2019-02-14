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
        'User-Agent': 'Mozilla/5.0 '
        '(Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 '
        '(KHTML, like Gecko) '
        'Chrome/39.0.2171.95 Safari/537.36',
        'Content-Type': 'application/json'}
    url = 'http://www.reddit.com/r/' + subreddit + '/hot.json'
    data = requests.get(url, headers=headers, allow_redirects=False)
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
