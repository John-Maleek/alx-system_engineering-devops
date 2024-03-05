#!/usr/bin/python3
"""A function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit
    Returns:
        number of subscribers based on subreddit,
        or 0 if subreddit requested is invalid
    """
    headers = {'User-Agent': 'ALX'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    else:
        return 0
