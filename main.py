import requests
from gamepending_vids import get_vids, pretty
from random import choice
import to_cohost
import to_twitter


def multi_upload(video):
    print(pretty(video))
    thumb_url = video.best_thumbnail.url
    img_format = thumb_url.split('.')[-1]
    thumbnail = f'thumb.{img_format}'
    with open(thumbnail, 'wb') as f:
        f.write(requests.get(thumb_url).content)
    print(f'Saved thumbnail as {thumbnail}')

    try:
        to_cohost.post_vid(video, thumbnail)
    except e:
        print(e)
    try:
        to_twitter.post_vid(video, thumbnail)
    except e:
        print(e)


if __name__ == '__main__':
    video = choice(get_vids())
    multi_upload(video)
