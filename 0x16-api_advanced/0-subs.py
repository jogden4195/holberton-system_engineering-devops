#!/usr/bin/python3
"""
Module for number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for
    a given subreddit
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 '
        '(Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 '
        '(KHTML, like Gecko) '
        'Chrome/39.0.2171.95 Safari/537.36',
        'Content-Type': 'application/json'}
    url = 'http://www.reddit.com/r/' + subreddit + '/about/.json'
    data = requests.get(url, headers=headers)
    if not data:
        return 0
    else:
        data_json = data.json()
        return data_json['data']['subscribers']
