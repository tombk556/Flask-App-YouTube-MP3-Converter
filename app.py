import os
from flask import Flask, jsonify, request, render_template, send_file, redirect, url_for
from src.downloader import YouTubeMp3Downloader
from src.changeMeta import ChangeMetaData
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=["POST"])
def process():
    url = request.form['url']
    title = request.form['title']
    artist = request.form['artist']
    audio_file_name = f"{artist} - {title}"
    obj = YouTubeMp3Downloader(url_link=url, name=audio_file_name)
    obj.download()
    audio_file = f"audio_content/{audio_file_name}.mp3"
    ChangeMetaData(audiofile = audio_file).change(title=title, artist=artist)
    audio_file = f"audio_content/{audio_file_name}.mp3" 
    return send_file(audio_file, as_attachment=True), os.remove(f'audio_content/{audio_file_name}.mp3'), os.remove('./thumbnail.jpg')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
