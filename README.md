# Reddit Image Downloader Bot

This is a simple bot that downloads images from new posts in a specified subreddit at a specified time. The bot is built using Python and can be easily deployed using Docker.

## How It Works

- The bot checks a specified subreddit for new posts.
- It downloads images from those posts and saves them to a local directory.
- The bot can be configured to run at a specific time daily.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit.git
cd reddit
```

### 2. Set Up Configuration

Create a .env file in the root directory and add your Reddit API credentials:
```
client_id=your_client_id
client_secret=your_client_secret
```

### 3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the bot
```
python main.py
```

## NOTE
- The bot will create a posts directory where all downloaded images will be stored.
- You can change the SUBREDDIT and SCHEDULE_TIME by updating the environment variables or by passing them interactively when prompted.
