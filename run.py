import praw
import requests, re, time,os

reddit = praw.Reddit(
    client_id="your-client-id",
    client_secret="clint secret",
    user_agent="user agent",
    #password="PASSWORD",
    #username="USERNAME",
)

seen_posts_id = []

def download_and_save_image(post, seen_posts_id):
    post_id = post.id

    if post_id in seen_posts_id:
        print(f"Skipping post (ID: {post_id}) - Already downloaded")
        return 

    seen_posts_id.append(post_id)
    url = post.url
    file_name = post.title + f" ({post.id})"
    file_name = re.sub(r'[^\w\-_\. ]', '_', file_name)  
    file_name = os.path.join("posts", file_name) + ".jpg" 

    print("File name:", file_name)
    print("Title:", post.title)
    print("ID:", post.id)
    print("URL:", post.url)

    r = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(r.content)
        print(f"Downloaded image: {file_name}")




def get_posts():

    subreddit = reddit.subreddit('soccerbanners')
    new_post = subreddit.new(limit=4)
    for post in new_post:
        download_and_save_image(post, seen_posts_id)

while True:
    get_posts()  
    time.sleep(10)  