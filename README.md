# Reddit Image Downloader Bot

This is a simple bot that downloads images from new posts in a specified subreddit at a specified time. The bot is built using Python and can be run directly or deployed using Docker.

## How It Works

- The bot checks a specified subreddit for new posts.
- It downloads images from those posts and saves them to a local directory.
- The bot can be configured to run at a specific time daily.

## Prerequisites

- Python 3.7 or higher
- Docker (optional, for containerized deployment)

## How to Run

### Option 1: Running from Terminal

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-image-downloader.git
cd reddit-image-downloader
```

#### 2. Set Up Configuration

Create a `.env` file in the root directory and add your Reddit API credentials:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USER_AGENT=your_user_agent
```

#### 3. Install Dependencies

For Windows:
```
pip install -r requirements.txt
```

For Linux:
```bash
pip3 install -r requirements.txt
```

#### 4. Run the Bot

For Windows:
```
python main.py
```

For Linux:
```bash
python3 main.py
```

### Option 2: Using Docker

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-image-downloader.git
cd reddit-image-downloader
```

#### 2. Build the Docker Image

```bash
docker build -t reddit-image-downloader .
```

#### 3. Run the Docker Container

```bash
docker run -e CLIENT_ID=your_client_id -e CLIENT_SECRET=your_client_secret -e USER_AGENT=your_user_agent -v $(pwd)/posts:/app/posts reddit-image-downloader
```

Replace `your_client_id`, `your_client_secret`, and `your_user_agent` with your actual Reddit API credentials.

## Configuration

You can configure the following environment variables:

- `SUBREDDIT`: The subreddit to download images from (default: "pics")
- `SCHEDULE_TIME`: The time to run the bot daily (default: "00:00")

Set these variables in the `.env` file for terminal execution, or pass them as environment variables when running the Docker container.

## Notes

- The bot will create a `posts` directory where all downloaded images will be stored.
- You can change the `SUBREDDIT` and `SCHEDULE_TIME` by updating the environment variables or by passing them interactively when prompted.
- Make sure to comply with Reddit's API terms of service and the rules of the subreddit you're downloading from.

## Troubleshooting

If you encounter any issues, please check the following:

1. Ensure your Reddit API credentials are correct.
2. Check your internet connection.
3. Verify that you have the necessary permissions to write to the `posts` directory.

For any other problems, please open an issue on the GitHub repository.
