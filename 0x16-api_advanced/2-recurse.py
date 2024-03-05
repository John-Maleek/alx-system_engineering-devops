#!/usr/bin/python3
""" A recursive function that queries the Reddit API """

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    global after
    headers = {'User-Agent': 'ALX'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    payload = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=payload)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
