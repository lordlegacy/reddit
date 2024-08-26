from config.config import Config
from core.reddit_client import create_reddit_client
from core.downloader import download_and_save_image
from core.scheduler import schedule_job
from utils.validator import validate_subreddit, validate_time_format
import os

if __name__ == "__main__":
    config = Config()
    reddit_client = create_reddit_client()

    subreddit_name = input("Enter the subreddit name: ")
    if not validate_subreddit(reddit_client, subreddit_name):
        exit(1)
    config.set_subreddit(subreddit_name)

    schedule_time = input("Enter the schedule time (HH:MM): ")
    if not validate_time_format(schedule_time):
        exit(1)
    config.set_schedule_time(schedule_time)

    if not os.path.exists("posts"):
        os.makedirs("posts")

    seen_posts_id = []

    def job():
        print("Checking for new posts...")
        subreddit = reddit_client.subreddit(config.get_subreddit())
        new_posts = subreddit.new(limit=3)
        for post in new_posts:
            download_and_save_image(post, seen_posts_id)

    schedule_job(config, job)
