"""
This script uses yt-dlp to download videos, by year,
from The Standup playlist on YouTube.
"""

import sys
import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all videos from a YouTube playlist.
    """
    ydl_opts = {
        'format': 'bv+ba',
        'outtmpl': '%(upload_date>%Y)s/%(title)s.%(ext)s',
        'noplaylist': False,
        'ignoreerrors': True,
        'download_archive': '/downloaded_videos.log',
        'remote-components': 'ejs:github',
        'concurrent-fragments': True,
        'no-mtime': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Depending on the year specified,
# set the appropriate playlist URL and output path.
if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PL2Fq-K0QdOQiJpufsnhEd1z3xOv2JMHuk"
    download_playlist(playlist)
    print("Downloaded all videos from The Standup.")
