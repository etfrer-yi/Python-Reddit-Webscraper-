# The idea of having a separate config.py file for saving the confidential information below comes from a Stackoverflow post, but I forgot the origin.

import praw
import config

def return_crawled_text(subreddit, category, title_or_content, post_limit):
    reddit = praw.Reddit(
        client_id = config.client_id,
        client_secret = config.client_secret,
        username = config.username,
        password = config.password,
        user_agent = config.user_agent,
    )
    crawled_text = ""
    subreddit = reddit.subreddit(subreddit)
    category_to_submission_map = {
        "controversial": subreddit.controversial(limit=int(post_limit)),
        "gilded": subreddit.gilded(limit=post_limit),
        "hot": subreddit.hot(limit=post_limit),
        "new": subreddit.new(limit=post_limit),
        "rising":subreddit.rising(limit=post_limit),
        "top": subreddit.top(limit=post_limit)
    }

    submissions = category_to_submission_map[category]

    for submission in submissions:
        if not submission.stickied: 
            crawled_text += ' ' + submission.selftext if title_or_content == "content" else submission.title
    crawled_text = crawled_text.lower()
    return crawled_text 

