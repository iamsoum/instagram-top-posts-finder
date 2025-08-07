import instaloader
import pandas as pd

def get_top_posts(username, top_n=5):
    L = instaloader.Instaloader()
    L.load_session_from_file('iamthesoum')
    profile = instaloader.Profile.from_username(L.context, username)

    posts_data = []
    for post in profile.get_posts():
        posts_data.append({
            'url': post.url,
            'likes': post.likes,
            'comments': post.comments,
            'caption': post.caption
        })

    df = pd.DataFrame(posts_data)
    top_liked = df.sort_values('likes', ascending=False).head(top_n)
    top_commented = df.sort_values('comments', ascending=False).head(top_n)

    print(f"\nTop {top_n} Liked Posts:")
    for idx, row in top_liked.iterrows():
        print(f"URL: {row['url']}\nLikes: {row['likes']}\nComments: {row['comments']}\n")

    print(f"\nTop {top_n} Commented Posts:")
    for idx, row in top_commented.iterrows():
        print(f"URL: {row['url']}\nLikes: {row['likes']}\nComments: {row['comments']}\n")

if __name__ == "__main__":
    username = input("Enter the public Instagram username: ")
    get_top_posts(username)
