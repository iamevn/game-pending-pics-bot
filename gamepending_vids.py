from googleapiclient.discovery import build
from dataclasses import dataclass

from secrets import YT_DATA_API_KEY

yt = build('youtube', 'v3', developerKey=YT_DATA_API_KEY)
channel_id ='UCgciOJ_c_eiOT8uqOzOLFRQ'
# uploads_playlist = yt.channels().list(part='contentDetails', id=channel_id).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
uploads_playlist = 'UUgciOJ_c_eiOT8uqOzOLFRQ'


@dataclass
class Thumbnail:
    name: str
    url: str
    width: int
    height: int


@dataclass
class VideoInfo:
    title: str
    description: str
    channelTitle: str
    videoId: str
    thumbnails: dict[str, Thumbnail]

    @classmethod
    def fromSnippet(cls, snippet: dict) -> 'VideoInfo':
        return cls(
                title = snippet['title'],
                description = snippet['description'],
                channelTitle = snippet['channelTitle'],
                videoId = snippet['resourceId']['videoId'],
                thumbnails = {k: Thumbnail(name=k, url=v['url'], width=v['width'], height=v['height']) for k, v in snippet['thumbnails'].items()},
            )

    @property
    def best_thumbnail(this) -> Thumbnail:
        return max(this.thumbnails.values(), key=lambda t: t.width)

    @property
    def watchUrl(this) -> str:
        return f'https://www.youtube.com/watch?v={this.videoId}'


def get_snippets() -> dict:
    PAGE_SIZE = 50
    req = yt.playlistItems().list(part='snippet', playlistId=uploads_playlist, maxResults=PAGE_SIZE)
    page = req.execute()
    yield from (item['snippet'] for item in page['items'])
    while 'nextPageToken' in page:
        req = yt.playlistItems().list(part='snippet', playlistId=uploads_playlist, maxResults=PAGE_SIZE, pageToken=page['nextPageToken'])
        page = req.execute()
        yield from (item['snippet'] for item in page['items'])


def pretty(vid: VideoInfo) -> str:
    return f'{vid.title} {vid.best_thumbnail.url}'


def get_vids() -> list[VideoInfo]:
    return [VideoInfo.fromSnippet(snippet) for snippet in get_snippets()]

