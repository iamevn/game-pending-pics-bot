from mastodon import Mastodon
from random import choice

from gamepending_vids import get_vids
from keys import MASTODON_ACCESS_TOKEN

m = Mastodon(access_token=MASTODON_ACCESS_TOKEN, api_base_url="https://botsin.space")


def post(video, img_file=None):
    if img_file is None:
        img_file = video.best_thumbnail.download()

    media = m.media_post(img_file)
    emoji = choice(['🐍🐱', '🐱🐍'])
    res = m.status_post(status=f'{emoji} {video.title}\n🔗 {video.watchUrl}', media_ids=[media])
    if 'uri' in res:
        print(f'posted to {res["uri"]}')
    else:
        print(res)


def post_random():
    post(choice(get_vids()))


if __name__ == '__main__':
    post_random()

