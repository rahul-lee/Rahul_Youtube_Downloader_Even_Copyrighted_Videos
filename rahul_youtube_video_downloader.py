import yt_dlp
import os

def list_formats(url):
    """List all available formats for a YouTube video"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            print(f"\nTitle: {info.get('title', 'Unknown')}")
            print(f"Duration: {info.get('duration', 0)} seconds")
            print("\nAvailable formats:")
            print("-" * 80)
            print(f"{'ID':<10} {'Extension':<12} {'Resolution':<15} {'FPS':<8} {'Size':<15}")
            print("-" * 80)
            
            for f in formats:
                format_id = f.get('format_id', 'N/A')
                ext = f.get('ext', 'N/A')
                resolution = f.get('resolution', 'audio only')
                fps = f.get('fps', 'N/A')
                filesize = f.get('filesize', 0)
                
                if filesize:
                    size_mb = f"{filesize / (1024*1024):.2f} MB"
                else:
                    size_mb = "Unknown"
                
                print(f"{format_id:<10} {ext:<12} {resolution:<15} {str(fps):<8} {size_mb:<15}")
            
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def download_video(url, quality='best'):
    """
    Download YouTube video
    
    Parameters:
    url (str): YouTube video URL
    quality (str): Quality option - 'best', 'worst', or specific format ID
                   - 'best': Best quality (video+audio)
                   - 'bestvideo': Best video only
                   - 'bestaudio': Best audio only
                   - '1080p', '720p', '480p', '360p': Specific resolution
                   - Format ID: Specific format from list_formats()
    """
    
    # Create downloads folder if it doesn't exist
    download_path = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_path, exist_ok=True)
    
    # Configure yt-dlp options based on quality
    if quality == 'best':
        format_string = 'best'  # Single file with video+audio (no ffmpeg needed)
    elif quality == 'bestvideo':
        format_string = 'bestvideo'
    elif quality == 'bestaudio':
        format_string = 'bestaudio'
    elif quality in ['1080p', '720p', '480p', '360p', '240p', '144p']:
        height = quality[:-1]  # Remove 'p'
        format_string = f'bestvideo[height<={height}]+bestaudio/best[height<={height}]'
    else:
        format_string = quality  # Assume it's a format ID
    
    ydl_opts = {
        'format': format_string,
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [download_progress_hook],
        'merge_output_format': 'mp4',  # Merge to mp4 if separate video/audio
        'ffmpeg_location': r'C:\ffmpeg_8_0_essentials_build\bin',  # Specify ffmpeg location
    }
    
    try:
        print(f"\nDownloading video with quality: {quality}")
        print(f"Download location: {download_path}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\n✓ Downloaded: {info.get('title', 'Unknown')}")
            return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False

def download_progress_hook(d):
    """Hook to display download progress"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rProgress: {percent} | Speed: {speed} | ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print("\n✓ Download completed, now processing...")

def main():
    print("=" * 80)
    print("YouTube Video Downloader")
    print("=" * 80)
    
    url = input("\nEnter YouTube video URL: ").strip()
    
    if not url:
        print("Error: No URL provided")
        return
    
    print("\nOptions:")
    print("1. List all available formats")
    print("2. Download best quality (video + audio)")
    print("3. Download specific resolution (1080p, 720p, 480p, 360p, etc.)")
    print("4. Download audio only")
    print("5. Download by format ID")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == '1':
        list_formats(url)
        
        # Ask if user wants to download after listing
        download_choice = input("\nDo you want to download? (y/n): ").strip().lower()
        if download_choice == 'y':
            format_id = input("Enter format ID or quality (e.g., '137' or '1080p' or 'best'): ").strip()
            download_video(url, format_id if format_id else 'best')
    
    elif choice == '2':
        download_video(url, 'best')
    
    elif choice == '3':
        resolution = input("Enter resolution (e.g., 1080p, 720p, 480p): ").strip()
        download_video(url, resolution)
    
    elif choice == '4':
        download_video(url, 'bestaudio')
    
    elif choice == '5':
        format_id = input("Enter format ID: ").strip()
        download_video(url, format_id)
    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()