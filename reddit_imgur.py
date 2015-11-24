"""

This program downloads the top rated images of the day from a user 
specified subreddit. Images are saved in the directory in which the 
program is run, in a folder named after the specified subreddit.
"""

__author__ = "Nick Condo"
__date__ = "11/22/2015"

import os
import requests
import praw

def make_dir(subreddit):
    """Create the directory to save the photos if it doesn't exist.

    Keyword arguments:
    subreddit -- the name of the directory to create
    """
    if not os.path.exists(subreddit):
        os.makedirs(subreddit)


def download_image(url, filename):
    """Download the image and save to local directory

    Keyword arguments:
    url -- the url of the image to download
    filename -- the name that the image will be saved as locally
    """
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        with open(filename, 'wb') as fo:
            for chunk in r.iter_content(4096):
                fo.write(chunk)


