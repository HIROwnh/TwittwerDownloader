import subprocess
import sys

def install_deps():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

try:
    import yt_dlp
except ImportError:
    install_deps()
    import yt_dlp

def download_twitter_video(url: str, output_dir: str = ".") -> None:
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # max quality
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"Downloaded: {info.get('title', 'video')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python downloader.py <twitter_url> [output_dir]")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    download_twitter_video(url, output_dir)
