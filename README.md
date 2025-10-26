# YouTube Video Downloader 🎥

A Python-based command-line tool for downloading YouTube videos in various quality formats using yt-dlp.

## 📋 Description

This project provides an easy-to-use interface for downloading YouTube videos with flexible quality options. Users can list all available formats, download videos in specific resolutions (1080p, 720p, 480p, etc.), extract audio only, or select custom format IDs for precise control over the download quality.

## ✨ Features

- **Multiple Quality Options**: Download videos in best quality, specific resolutions, or by format ID
- **Format Listing**: View all available formats with details (resolution, file size, FPS, extension)
- **Audio Extraction**: Download audio-only files
- **Progress Tracking**: Real-time download progress with speed and ETA
- **Automatic Merging**: Combines separate video and audio streams into MP4 format
- **User-Friendly Interface**: Interactive menu-driven command-line interface
- **Error Handling**: Robust error handling with clear feedback

## 🛠️ Technologies Used

- **Python 3.7+**
- **yt-dlp**: YouTube video download library
- **FFmpeg**: Media processing and merging (optional but recommended)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

2. Install required dependencies:
```bash
pip install yt-dlp
```

3. (Optional) Install FFmpeg for best quality downloads:
   - Download from [FFmpeg official site](https://ffmpeg.org/download.html)
   - Add to system PATH or update the script with FFmpeg location

## 🚀 Usage

Run the script:
```bash
python youtube_downloader.py
```

Choose from the available options:
1. List all available formats
2. Download best quality (video + audio)
3. Download specific resolution (1080p, 720p, 480p, 360p, etc.)
4. Download audio only
5. Download by format ID

## 📝 Example
```
Enter YouTube video URL: https://www.youtube.com/watch?v=example
Options:
1. List all available formats
2. Download best quality (video + audio)
Enter your choice (1-5): 2

Downloading video with quality: best
Progress: 45.2% | Speed: 2.5MiB/s | ETA: 00:15
```

## ⚠️ Legal Disclaimer

This tool is for personal use only. Downloading copyrighted content without permission may violate YouTube's Terms of Service and copyright laws. Use responsibly and only download:
- Your own content
- Content with appropriate licenses (e.g., Creative Commons)
- Content where you have explicit permission

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name
- GitHub: [@rahul-lee](https://github.com/rahul-lee)

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful download engine
- [FFmpeg](https://ffmpeg.org/) - Media processing framework 
- [FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/) - Alternative FFmpeg download for Windows users
