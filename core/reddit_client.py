import os
import praw

def create_reddit_client():
    reddit = praw.Reddit(
        client_id=os.getenv('client_id'),
        client_secret=os.getenv('client_secret'),
        user_agent="myredditapp by /u/yourusername",
    )
    return reddit
