import os
import urllib.request
import yt_dlp


class YouTubeMp3Downloader:
    def __init__(self, url_link: str, name: str, ) -> None:

        self.url_link = url_link
        self.name = name

    def download(self):
        """
        download audio from youtube and convert it into mp3,
        stored in audio_content with self.name
        """
        os.makedirs("audio_content", exist_ok=True)
        mp3_file = f"audio_content/{self.name}.mp3"

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"audio_content/{self.name}.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url_link, download=True)

        # download the thumbnail
        thumbnail_url = info.get("thumbnail")
        if thumbnail_url:
            urllib.request.urlretrieve(thumbnail_url, "thumbnail.jpg")

        return mp3_file
