import instaloader 
from datetime import datetime 
from itertools import dropwhile, takewhile 
import csv
import re  
class GetInstagramPosts:
    accoutns = []
    posts = []
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()
    def download_users_post_with_periods(self,username):
        user_posts = []
        posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
        try:
            for post in posts:
                print(post.shortcode)
                user_posts.append(post.shortcode)
        except:
            pass
        if len(user_posts) > 0:
            with open("ids_after_filter.txt","a",encoding="utf-8") as f:
                f.write(f"https://www.instagram.com/p/{user_posts[0]}")
                f.write("\n")
    def run(self):
        with open("results.txt","r",encoding="utf-8") as f:
            for item in f.readlines():
                item = re.sub("\s{1,1000}","",item)
                if item not in self.accoutns:
                    print(item)
                    self.accoutns.append(item)
        for item in self.accoutns:
            bot.download_users_post_with_periods(item)
if __name__ == "__main__":
    bot = GetInstagramPosts()
    bot.run()
    