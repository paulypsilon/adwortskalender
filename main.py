import os
import requests
from atproto import Client

BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASS = os.getenv("BLUESKY_PASS")

def post_bluesky(text):
    client = Client()
    client.login(BLUESKY_USER, BLUESKY_PASS)
    client.send_post(text)

def main():
    text = f"Testtext"
    
    print("Posting:", text)
    post_bluesky(text)

if __name__ == "__main__":
    main()
