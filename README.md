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




## 📦 Installation Guide

### Prerequisites

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **FFmpeg** - Required for merging video and audio streams

---

### Step 1: Install Python

#### Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check ✅ "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
```bash
   python --version
```

#### macOS:
```bash
# Using Homebrew
brew install python3

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

---

### Step 2: Clone or Download the Repository

#### Option A: Using Git
```bash
git clone https://github.com/rahul-lee/Rahul_Youtube_Downloader_Even_Copyrighted_Videos.git
cd Rahul_Youtube_Downloader_Even_Copyrighted_Videos
```

#### Option B: Download ZIP
1. Click the green **"Code"** button on GitHub
2. Select **"Download ZIP"**
3. Extract the ZIP file to your desired location
4. Open terminal/command prompt in that folder

---

### Step 3: Install Python Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Or install directly
pip install yt-dlp
```

**Verify installation:**
```bash
yt-dlp --version
```

---

### Step 4: Install FFmpeg

FFmpeg is essential for merging high-quality video and audio streams.

#### Windows (Recommended Methods):

**Method 1: Using Chocolatey (Easiest)**
```bash
# Install Chocolatey first: https://chocolatey.org/install
choco install ffmpeg
```

**Method 2: Using Winget**
```bash
winget install ffmpeg
```

**Method 3: Manual Installation**

1. **Download FFmpeg:**
   - Visit: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
   - Download: `ffmpeg-release-essentials.zip`

2. **Extract the Files:**
   - Extract to `C:\ffmpeg` (or any preferred location)
   - You should have a folder structure like: `C:\ffmpeg\bin\ffmpeg.exe`

3. **Add FFmpeg to System PATH:**

   **Option A: Using PowerShell (Quick)**
   
   Open PowerShell as **Administrator** and run:
```powershell
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\bin", "Machine")
```

   **Option B: Using GUI**
   
   - Press `Windows + R`, type `sysdm.cpl`, press Enter
   - Click the **"Advanced"** tab
   - Click **"Environment Variables"**
   - Under **"System variables"**, find and select **"Path"**
   - Click **"Edit"**
   - Click **"New"**
   - Add: `C:\ffmpeg\bin`
   - Click **"OK"** on all windows
   - **Important**: Restart your terminal/PowerShell

4. **Verify Installation:**
   
   Close and reopen your terminal, then run:
```bash
   ffmpeg -version
```
   
   You should see FFmpeg version information.

#### macOS:
```bash
# Using Homebrew
brew install ffmpeg

# Verify installation
ffmpeg -version
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg

# Verify installation
ffmpeg -version
```

---

### Step 5: Configure FFmpeg Path (Optional)

If you don't want to add FFmpeg to PATH, update the script with your FFmpeg location:

Open `rahul_youtube_video_downloader.py` and modify line 77:
```python
'ffmpeg_location': r'C:\ffmpeg\bin',  # Change this to your FFmpeg path
```

**Common paths:**
- Windows: `C:\ffmpeg\bin` or `C:\ffmpeg_8_0_essentials_build\bin`
- macOS: `/usr/local/bin` or `/opt/homebrew/bin`
- Linux: `/usr/bin`

---

### Step 6: Run the Script
```bash
# Windows
python rahul_youtube_video_downloader.py

# macOS/Linux
python3 rahul_youtube_video_downloader.py
```

---

## 🎯 Quick Start After Installation
```bash
# Navigate to the project directory
cd Rahul_Youtube_Downloader_Even_Copyrighted_Videos

# Run the script
python rahul_youtube_video_downloader.py

# Follow the on-screen prompts:
# 1. Enter YouTube video URL
# 2. Choose quality option (1-5)
# 3. Wait for download to complete
```

---

## 🔧 Troubleshooting

### "ffmpeg not found" Error

**Solution 1:** Verify FFmpeg is in PATH
```bash
ffmpeg -version
```
If this doesn't work, FFmpeg isn't in your PATH. Follow Step 4 again carefully.

**Solution 2:** Specify FFmpeg location in script
Edit line 77 in the script with your FFmpeg path.

### "yt-dlp not found" Error
```bash
# Reinstall yt-dlp
pip install --upgrade yt-dlp
```

### "Python not recognized" Error

Python isn't in your PATH. Reinstall Python and check "Add Python to PATH" during installation.

### Permission Denied Error (Linux/macOS)
```bash
chmod +x rahul_youtube_video_downloader.py
```

### Downloads Folder Not Created

The script automatically creates a `downloads` folder in the same directory. If it fails:
```bash
mkdir downloads
```

---

## 📁 Project Structure
```
Rahul_Youtube_Downloader_Even_Copyrighted_Videos/
│
├── rahul_youtube_video_downloader.py  # Main script
├── requirements.txt                    # Python dependencies
├── README.md                          # This file
├── LICENSE                            # License file
└── downloads/                         # Downloaded videos (auto-created)
```

---

## 🖥️ System Requirements

- **Operating System:** Windows 10/11, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python:** 3.7 or higher
- **RAM:** 2GB minimum
- **Storage:** Depends on video downloads
- **Internet:** Stable connection for downloading

---

## ⚙️ Environment Variables Summary

For the script to work properly, ensure these are in your system PATH:

| Tool | PATH Location (Example) |
|------|------------------------|
| Python | `C:\Python312\` or `/usr/local/bin/python3` |
| pip | `C:\Python312\Scripts\` |
| FFmpeg | `C:\ffmpeg\bin\` or `/usr/local/bin/` |

**Check your PATH:**

**Windows:**
```bash
echo %PATH%
```

**macOS/Linux:**
```bash
echo $PATH
```

---

## 🆘 Still Having Issues?

1. Check the [Issues](https://github.com/rahul-lee/Rahul_Youtube_Downloader_Even_Copyrighted_Videos/issues) page
2. Create a new issue with:
   - Your operating system
   - Python version (`python --version`)
   - Error message screenshot
   - Steps you've tried

---

## ✅ Verification Checklist

Before running the script, verify:

- [ ] Python is installed and in PATH
- [ ] pip is working (`pip --version`)
- [ ] yt-dlp is installed (`pip show yt-dlp`)
- [ ] FFmpeg is installed and in PATH (`ffmpeg -version`)
- [ ] You're in the project directory
- [ ] You have internet connection

If all checks pass, you're ready to download! 🚀

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The powerful download engine
- [FFmpeg](https://ffmpeg.org/) - Media processing framework 
- [FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/) - Alternative FFmpeg download for Windows users
