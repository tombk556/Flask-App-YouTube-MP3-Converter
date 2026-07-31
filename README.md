# YouTube MP3 Downloader

Simple Flask app to download a YouTube video and convert it to MP3.

## Run locally

```bash
pip install -r requirements.txt
python3 app.py
```

Requires `ffmpeg` installed on your system.

App runs at http://localhost:5000

## Run with Docker

```bash
docker build -t ytmp3 .
docker run --rm -p 8000:8000 ytmp3
```

## Run with Docker Compose

```bash
docker compose up
```

App runs at http://localhost:8000
