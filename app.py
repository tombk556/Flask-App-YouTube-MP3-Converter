import os
from flask import Flask, request, render_template, send_file, url_for
from src.downloader import YouTubeMp3Downloader
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input url
       url = request.form.get("url")
       print("URL: ", url)
       # getting input song
       song = request.form.get("song")
       # getting input artist
       artist = request.form.get("artist")
       # audio file name
       audio_file_name = f"{song} - {artist}"
       print("Audio File Name: ", audio_file_name)
       obj = YouTubeMp3Downloader(url_link=url, name=audio_file_name)
       obj.download()
       audio_file = f"audio/{audio_file_name}.mp3"
       return send_file(audio_file, as_attachment=True), os.remove(audio_file)
    return render_template("index.html")
 
if __name__=='__main__':
   app.run(debug=True)