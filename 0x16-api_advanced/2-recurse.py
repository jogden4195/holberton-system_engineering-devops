#!/usr/bin/python3
"""
Module for recurse
"""
import requests


def recurse(subreddit, hot_list=[], tynext=None):
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
    if tynext:
        url += '?after=' + tynext
    data = requests.get(url, headers=headers)
    if data.status_code != 200:
        return
    data_json = data.json()
    posts = data_json['data']['children']
    for p in posts:
        hot_list.append(p['data']['title'])
    if data_json['data']['after']:
        grande = data_json['data']['after']
        return recurse(subreddit,
                       hot_list=hot_list,
                       tynext=grande)
    else:
        return hot_list
