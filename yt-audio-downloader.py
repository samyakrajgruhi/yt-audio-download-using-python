import os
import yt_dlp

def download_audio_with_ytdlp(youtube_url, save_path):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "ffmpeg_location": "C:\\Users\\samya\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-7.1-full_build\\bin",
        "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video or playlist URL: ")
    save_path = input("Enter the folder path to save audio files (default: './downloads/'): ") or "./downloads"
    os.makedirs(save_path, exist_ok=True)
    download_audio_with_ytdlp(youtube_url, save_path)
