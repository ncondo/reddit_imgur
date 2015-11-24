"""

This program downloads the top rated images of the day from a user 
specified subreddit. Images are saved in the directory in which the 
program is run, in a folder named after the specified subreddit.
"""

__author__ = "Nick Condo"
__date__ = "11/22/2015"

import os
import re
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
    """Download the image and save to local directory.

    Keyword arguments:
    url -- the url of the image to download
    filename -- the name that the image will be saved as locally
    """
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        with open(filename, 'wb') as fo:
            for chunk in r.iter_content(4096):
                fo.write(chunk)


def get_submissions(subreddit, min_score=20, limit=20):
    """Check specified subreddit for submissions that meet the 
        requirements for downloading.

    Keyword arguments:
    subreddit -- the subreddit from which to download images
    min_score -- the min reddit score that qualifies for downloading
    limit -- the max images to download per execution
    """
    r = praw.Reddit('reddit_imgur scraper: v1.0 (by /u/reddit_imgur)')
    submissions = r.get_subreddit(subreddit).get_top_from_day(limit=limit)

    imgur_url_pattern = re.compile(r'(http://i.imgur.com/(.*))(\?.*)?')
    make_dir(subreddit)
    for submission in submissions:
        # Skip if we've already dowloaded image
        if os.path.isfile('%s/reddit_%s_%s_*' % (subreddit, subreddit, submission.id)):
            continue
        # Skip if score doesn't meet min score requirement
        if submission.score < min_score:
            continue
        if 'http://i.imgur.com/' in submission.url:
            s = imgur_url_pattern.search(submission.url)
            imgur_file_name = s.group(2)
            if '?' in imgur_file_name:
                imgur_file_name = imgur_file_name[:imgur_file_name.find('?')]
            filename = './%s/reddit_%s_%s_%s' % (subreddit, subreddit,
                                                 submission.id, imgur_file_name)
            download_image(submission.url, filename)


