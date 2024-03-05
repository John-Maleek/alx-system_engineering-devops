#!/usr/bin/python3
""" A function that queries the Reddit API """

import requests


def top_ten(subreddit):
    """Prints the titles of the first
    10 hot posts listed for a given
    subreddit.
    """
    headers = {'User-Agent': 'ALX'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    payload = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=payload)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
