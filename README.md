# "THIS CODE WILL NOT WORK UNTIL YOU SET THE CORRECT FFMPEG PATH" so please check how to do it first -> [Installation](#installation)
![yt-audio-download-using-python](https://socialify.git.ci/samyakrajgruhi/yt-audio-download-using-python/image?font=KoHo&language=1&name=1&pattern=Transparent&theme=Dark)
# YouTube Audio Downloader

This Python script allows you to download audio from a YouTube video or an entire playlist in MP3 format. It uses the yt-dlp library and FFmpeg for audio extraction. You can specify a custom folder for saving the downloaded audio files.

## Features

- Supports both single YouTube videos and playlists.

- Downloads high-quality audio in MP3 format.

- Allows users to specify the download folder path.

- Automatically handles video-to-audio conversion using FFmpeg.
## Requirements
- Python 3.7 or higher

- Libraries:
    - yt-dlp

- FFmpeg installed on your system
## Installation
1. Install Python Dependencies :
```bash
pip install yt-dlp
```
2. Install FFmpeg

- Windows :
    - Run in terminal(Command Prompt [As Administrator]):
```bash
winget install ffmpeg
```
- Linux :
```bash
sudo apt update
sudo apt install ffmpeg
```

3. Clone or Download the script "_yt-audio-downloader.py_" on your system.



## Usage

Run the script.

### Example Workflow

1. Enter the YouTube Video or Playlist URL: Paste the URL when prompted.

2. Set the Download Folder Path:
- The program will ask you to specify a folder path where audio files should be saved.

3. Press Enter to use the default folder ./downloads/.
- This will create a folder named "downloads" in the same directory as the script is present in.

### Setting the Download Folder Path
- To set a custom folder path, type the full path when prompted.
Example for Windows:
- if you have a folder named "songs" in D drive :
```bash
D:/songs/
```
Example for Linux:
```bash
/home/yourname/Music
```
- Ensure the folder exists or the script will create it automatically.

### How to set path for ffmpeg :
1. Re-open Command Prompt as admin/Terminal after installing ffmpeg and run :
```bash
where ffmpeg
```
2.  Now copy the path till bin.
- For example: In my system, the output was ->
```bash
C:\Users\user\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin\ffmpeg.exe
```
- Then i will just copy -> 
```bash
C:\Users\user\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin
```
or simply just remove 'ffmpeg.exe' from the end

3. Now replace this with <YOU_NEED_TO_PUT_FFMPEG_PATH_HERE> in the script.

4. Now you can either replace every \ (backslash) with \\\ in the path string or write path as -> r"YOUR_FFMPEG_PATH"

5. If it doesnt show any warnings or errors on running the script then you are good to go or else you probably missed something, if not then [Contribute](#contributing).


## IMPORTANT

- Be Patient: Downloading audio from YouTube, especially for large playlists, may take some time depending on your internet speed and the number of videos.

- FFmpeg Configuration: Make sure FFmpeg is properly installed and its path is correctly set. You can specify its location directly in the script if needed.
## Contributing

Feel free to submit issues or feature requests via GitHub.
