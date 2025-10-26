# YouTube Video Downloader 🎥

A powerful Python-based command-line tool for downloading YouTube videos in various quality formats using yt-dlp.

## 📋 Overview

Since YouTube officially restricted third-party downloading tools and extensions, accessing high-quality video downloads has become challenging. YouTube now requires a Premium subscription to download videos within their app, and most external software solutions demand premium accounts for high-quality downloads. (Tubemate shows ads all the time 😟)

**This Python script provides a free alternative** that enables you to:
- Download YouTube videos directly in high quality (up to 1080p)
- Extract audio-only files
- Choose from multiple quality options without any subscription
- Its Ads Free!
- Download videos with a simple, user-friendly command-line interface 

No premium accounts. No subscription fees. Just straightforward video downloading.

## ✨ Key Features

- **Multiple Quality Options**: Download videos in best quality, specific resolutions (1080p, 720p, 480p, 360p, etc.), or by custom format ID
- **Format Browser**: List all available video/audio formats with detailed specifications (resolution, file size, FPS, codec)
- **Audio Extraction**: Download audio-only files for music, podcasts, or lectures
- **Progress Tracking**: Real-time download progress with speed, percentage, and ETA
- **Smart Merging**: Automatically combines separate video and audio streams into MP4 format using FFmpeg
- **Interactive Menu**: User-friendly command-line interface with clear options
- **Robust Error Handling**: Informative error messages and graceful failure recovery
- **Batch Downloads**: Support for downloading entire playlists (coming soon)

## 🎯 Why Use This Tool?

| Feature | YouTube Premium | Other Tools | This Script |
|---------|----------------|-------------|-------------|
| Cost | ₹129-199/month | $5-20/month | **FREE** |
| Quality | Up to 1080p | Limited | **Up to 1080p** |
| Audio Only | ✅ | Limited | **✅** |
| No Account Needed | ❌ | ❌ | **✅** |
| Open Source | ❌ | ❌ | **✅** |


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

**For Personal/Educational Use Only**

This tool can download copyrighted content, but doing so without permission violates YouTube's Terms of Service and may violate copyright laws. 

**Use Responsibly - Only Download:**
- ✅ Your own content
- ✅ Creative Commons licensed content  
- ✅ Content with explicit owner permission
- ✅ Public domain content

**The author assumes no liability for misuse. Users are solely responsible for ensuring legal compliance in their jurisdiction.**

Downloading copyrighted material without authorization may result in legal consequences, DMCA takedowns, or account suspension. When in doubt, don't download.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 💖 Support the Project

If you find this tool helpful and would like to support its development, consider buying me a coffee!

**UPI ID (India):**  `rahultaker90-5@okhdfcbank`

**Google Pay
<img width="399" height="396" alt="image" src="https://github.com/user-attachments/assets/6a8d1879-145d-4503-8b9e-f97c0285a9f6" />


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name
- GitHub: [@rahul-lee](https://github.com/rahul-lee)

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful download engine
- [FFmpeg](https://ffmpeg.org/) - Media processing framework 
- [FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/) - Alternative FFmpeg download for Windows users
