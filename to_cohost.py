from random import choice
from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock

from gamepending_vids import get_vids
from keys import COHOST_COOKIE

user = User.loginWithCookie(COHOST_COOKIE)
project = user.getProject('game-pending-pics')


def post(video, img_file=None):
    if img_file is None:
        img_file  = video.best_thumbnail.download()

    blocks = [
        AttachmentBlock(img_file),
        MarkdownBlock(f'from [{video.title}]({video.watchUrl})'),
    ]
    newPost = project.post('', blocks, tags=['bot', 'gamepending', 'youtube'])
    if hasattr(newPost, 'url'):
        print(f'posted at {newPost.url}')
    else:
        print(newPost)


def post_random():
    post(choice(get_vids()))


if __name__ == '__main__':
    post_random()

