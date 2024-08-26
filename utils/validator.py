# utils/validator.py

import re
from prawcore.exceptions import NotFound

def validate_subreddit(reddit_client, subreddit_name):
    try:
        reddit_client.subreddit(subreddit_name).id
        return True
    except NotFound:
        print(f"Subreddit '{subreddit_name}' not found.")
        return False

def validate_time_format(schedule_time):
    if re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', schedule_time):
        return True
    else:
        print("Invalid time format. Please use HH:MM in 24-hour format.")
        return False
