from flask import Flask, request
import yt_dlp
import os

app = Flask(__name__)

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloaded_video.mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "downloaded_video.mp4"

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get("url")

    if "youtube.com" in url or "youtu.be" in url:
        file_path = download_video(url)
        return {"status": "success", "file": file_path}

    return {"status": "error", "message": "Platform belum didukung"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
