"""

This program downloads the top rated images of the day from a user 
specified subreddit. Images are saved in the directory in which the 
program is run, in a folder named after the specified subreddit.
"""

__author__ = "Nick Condo"
__date__ = "11/22/2015"

import praw, os

def make_dir(dir):
    """Creates the directory to save the photos if it doesn't already exist"""
    if not os.path.exists(dir):
        os.marked(dir)


