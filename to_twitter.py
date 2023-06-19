import tweepy
import requests

from random import choice

from gamepending_vids import get_vids
from secrets import TWITTER_BEARER_TOKEN, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

client = tweepy.Client(
  bearer_token=TWITTER_BEARER_TOKEN,
  consumer_key=TWITTER_CONSUMER_KEY,
  consumer_secret=TWITTER_CONSUMER_SECRET,
  access_token=TWITTER_ACCESS_TOKEN,
  access_token_secret=TWITTER_ACCESS_SECRET,
)
auth = tweepy.OAuth1UserHandler(
  consumer_key=TWITTER_CONSUMER_KEY,
  consumer_secret=TWITTER_CONSUMER_SECRET,
  access_token=TWITTER_ACCESS_TOKEN,
  access_token_secret=TWITTER_ACCESS_SECRET,
)
api = tweepy.API(auth)


def post_vid(video, thumb_filename=None):
    if thumb_filename is None:
        thumb_url = video.best_thumbnail.url
        img_format = thumb_url.split('.')[-1]
        img_file = f'thumb.{img_format}'
        with open(img_file, 'wb') as f:
            f.write(requests.get(thumb_url).content)
        print(f'Saved thumbnail for "{video.title}" as {img_file}')
    else:
        img_file = thumb_filename

    media = api.media_upload(img_file)
    res = client.create_tweet(text=f'from {video.title}\n{video.watchUrl}', media_ids=[media.media_id])
    print(res)


def post_random():
    post_vid(choice(get_vids()))


if __name__ == '__main__':
    post_random()

