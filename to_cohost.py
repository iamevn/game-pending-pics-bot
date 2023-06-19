import requests

from random import choice
from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock

from gamepending_vids import get_vids
from secrets import COHOST_COOKIE

user = User.loginWithCookie(COHOST_COOKIE)
project = user.getProject('game-pending-pics')


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

    blocks = [
        AttachmentBlock(img_file),
        MarkdownBlock(f'from [{video.title}]({video.watchUrl})'),
    ]
    newPost = project.post('', blocks, tags=['bot', 'gamepending', 'youtube'])
    print(f'posted at {newPost.url}')


def post_random():
    post_vid(choice(get_vids()))


if __name__ == '__main__':
    post_random()

