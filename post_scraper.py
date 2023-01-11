import instaloader 
from datetime import datetime 
from itertools import dropwhile, takewhile 
import csv 
class GetInstagramPosts:
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()
    def download_users_post_with_periods(self,username):
        posts = instaloader.Profile.from_username(self.L.context,username).get_posts()
        try:
            print(f"https://www.instagram.com/p/{posts[0].shortcode}")
        except:
            print(f"{username} dosen't have any posts or it is a private account!")