Really basic code to upload a random thumbnail from Game Pending's YouTube channel to
[@game-pending-pics](https://cohost.org/game-pending-pics) on cohost and [@GamePendingPics](https://twitter.com/GamePendingPics) on twitter.

Needs a [cohost cookie](https://github.com/valknight/Cohost.py#retrieving-your-cookie)
and a [YouTube Data API key](https://developers.google.com/youtube/v3/docs)
to be set in [`secrets.py`](secrets.py).

Also needs a bunch of twitter keys in there, god help you if you need to set this up yourself.
I was only able to set this up because I had keys from an old project already set up years ago I wasn't using.
You can't make a new project now thanks to fucking Elon Musk. I've heard 1st party API keys are floating around ripped from iOS/android apps but I don't know who I'd ask for help getting those.

You'll probably want to change the `channel_id`, `uploads_playlist`,
and cohost `project` if you use this.

