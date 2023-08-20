from random import choice

from gamepending_vids import get_vids, pretty


def multi_upload(video):
    print(pretty(video))
    thumbnail = video.best_thumbnail.download()
    print(f'Saved thumbnail as {thumbnail}')

    try:
        import to_cohost
        to_cohost.post(video, thumbnail)
    except Exception as e:
        print(e)
    try:
        import to_twitter
        to_twitter.post(video, thumbnail)
    except Exception as e:
        print(e)
    try:
        import to_mastodon
        to_mastodon.post(video, thumbnail)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    video = choice(get_vids())
    multi_upload(video)

