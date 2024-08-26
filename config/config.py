
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.subreddit = None
        self.schedule_time = None

    def set_subreddit(self, subreddit):
        self.subreddit = subreddit

    def set_schedule_time(self, schedule_time):
        self.schedule_time = schedule_time

    def get_subreddit(self):
        return self.subreddit or os.getenv('SUBREDDIT')

    def get_schedule_time(self):
        return self.schedule_time or os.getenv('SCHEDULE_TIME')
