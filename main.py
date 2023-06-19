from random import choice

from gamepending_vids import get_vids, pretty
import to_cohost
import to_twitter


def multi_upload(video):
    print(pretty(video))
    thumbnail = video.best_thumbnail.download()
    print(f'Saved thumbnail as {thumbnail}')

    try:
        to_cohost.post(video, thumbnail)
    except Exception as e:
        print(e)
    try:
        to_twitter.post(video, thumbnail)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    video = choice(get_vids())
    multi_upload(video)
