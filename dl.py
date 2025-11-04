import yt_dlp

video_url = input("Введите URL видео: ")
choice = input("MP4 или MP3? (1/2): ")

if choice == "1":
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
    }
else:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

yt_dlp.YoutubeDL(ydl_opts).download([video_url])
