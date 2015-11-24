# reddit_imgur
Downloads the top rated images of the day from a specified subreddit

## Install
* Checkout the source: git clone 'git://github.com/ncondo/reddit_imgur.git'
* Be sure to have the [PRAW](https://praw.readthedocs.org/en/stable/index.html) library installed
  - pip install praw or visit link above for more details
* Implemented and designed to run on python 3.x

## Getting started
* Install reddit_imgur
* Navigate to the directory where you just installed reddit_imgur
* run 'python3 reddit_imgur.py' to get images with default values
  - default subreddit is r/wallpaper
  - default min_score is 20 (will only download images with karma >= 20)
  - default limit is 10 (will only download max of 10 images per execution)

## Examples
* 'python3 reddit_imgur.py space' 
  - will download images from r/space with default min_score and limit values
* 'python3 reddit_imgur.py space 10 25'
  - will download images from r/space with min_score of 10 and limit of 25 images
  
