"""
YouTube Music Downloader
========================
Downloads a YouTube video as MP3 with embedded thumbnail + ID3 tags.
Also saves the thumbnail as a .jpg beside the MP3.

Usage:
    python downloader_script.py <YouTube URL or search query>

Examples:
    python downloader_script.py https://www.youtube.com/watch?v=xxx
    python downloader_script.py "Shape of You Ed Sheeran"

Output folders:
    allSongs/    – MP3 file + thumbnail jpg (main library)
    Downloads/   – copy of MP3 + thumbnail  (shown on Downloads page in app)
    imgs/covers/ – copy of thumbnail for the player UI

Dependencies (install once):
    pip install yt-dlp mutagen Pillow requests
"""

import sys
import os
import re
import io
import sqlite3
import shutil
import requests

try:
    import yt_dlp
except ImportError:
    print("yt-dlp not found. Run:  pip install yt-dlp")
    sys.exit(1)

try:
    from mutagen.mp3 import MP3
    from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TRCK, ID3NoHeaderError
except ImportError:
    print("mutagen not found. Run:  pip install mutagen")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Run:  pip install Pillow")
    sys.exit(1)


# CONFIG
OUTPUT_FOLDER    = "allSongs"
DOWNLOADS_FOLDER = "Downloads"
COVERS_FOLDER    = os.path.join("imgs", "covers")
DB_PATH          = "Spotify.db"
FALLBACK_IMG     = os.path.join("imgs", "notifi.png")

os.makedirs(OUTPUT_FOLDER,    exist_ok=True)
os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)
os.makedirs(COVERS_FOLDER,    exist_ok=True)


def sanitize(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()


def seconds_fmt(secs: float) -> str:
    m, s = divmod(int(secs), 60)
    return f"{m:02d}:{s:02d}"


def download_thumbnail(url: str, save_path: str) -> bool:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content)).convert("RGB")
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        top  = (h - side) // 2
        img  = img.crop((left, top, left + side, top + side))
        img  = img.resize((500, 500), Image.LANCZOS)
        img.save(save_path, "JPEG", quality=90)
        print(f"   Thumbnail saved -> {save_path}")
        return True
    except Exception as e:
        print(f"   Thumbnail download failed: {e}")
        return False


def embed_tags(mp3_path: str, title: str, artist: str, album: str, thumb_path: str):
    try:
        try:
            tags = ID3(mp3_path)
        except ID3NoHeaderError:
            tags = ID3()
        tags[TIT2.FrameID] = TIT2(encoding=3, text=title)
        tags[TPE1.FrameID] = TPE1(encoding=3, text=artist)
        tags[TALB.FrameID] = TALB(encoding=3, text=album)
        if os.path.exists(thumb_path):
            with open(thumb_path, "rb") as f:
                tags[APIC.FrameID] = APIC(
                    encoding=3, mime="image/jpeg",
                    type=3, desc="Cover", data=f.read()
                )
        tags.save(mp3_path, v2_version=3)
        print(f"   ID3 tags embedded")
    except Exception as e:
        print(f"   Tag embedding failed: {e}")


def get_duration_str(mp3_path: str) -> str:
    try:
        return seconds_fmt(MP3(mp3_path).info.length)
    except Exception:
        return "00:00"


def update_database(title, duration, mp3_path, thumb_path, artist, album,
                    dl_mp3_path, dl_thumb_path):
    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        # ── all_songs_data (6 cols) ──
        cur.execute("""CREATE TABLE IF NOT EXISTS all_songs_data (
            Name VARCHAR(100), DURATION VARCHAR(10), FILE_PATH VARCHAR(200),
            IMG_PATH VARCHAR(200), Artist VARCHAR(100), Album VARCHAR(100)
        )""")
        cur.execute("PRAGMA table_info(all_songs_data)")
        if "Album" not in [r[1] for r in cur.fetchall()]:
            cur.execute("ALTER TABLE all_songs_data ADD COLUMN Album VARCHAR(100) DEFAULT ''")
            con.commit()
            print(f"   Migrated all_songs_data: added Album column")

        cur.execute("SELECT FILE_PATH FROM all_songs_data WHERE FILE_PATH = ?", (mp3_path,))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO all_songs_data VALUES (?,?,?,?,?,?)",
                        (title, duration, mp3_path, thumb_path, artist, album))
            con.commit()
            print(f"   Added to all_songs_data")
        else:
            print(f"   Already in all_songs_data, skipping")

        # ── Downloads (5 cols — matches your app's table) ──
        cur.execute("""CREATE TABLE IF NOT EXISTS Downloads (
            Name VARCHAR(100), DURATION VARCHAR(10), FILE_PATH VARCHAR(200),
            IMG_PATH VARCHAR(200), Artist VARCHAR(100)
        )""")
        cur.execute("SELECT FILE_PATH FROM Downloads WHERE FILE_PATH = ?", (dl_mp3_path,))
        if cur.fetchone() is None:
            cur.execute(
                "INSERT INTO Downloads (Name, DURATION, FILE_PATH, IMG_PATH, Artist) VALUES (?,?,?,?,?)",
                (title, duration, dl_mp3_path, dl_thumb_path, artist)
            )
            con.commit()
            print(f"   Added to Downloads table")
        else:
            print(f"   Already in Downloads, skipping")

        con.close()
    except Exception as e:
        print(f"   DB update failed: {e}")


def download(query: str):
    if not query.startswith("http"):
        query = f"ytsearch1:{query}"

    print(f"\nResolving: {query}")

    with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(query, download=False)

    if "entries" in info:
        info = info["entries"][0]

    title  = sanitize(info.get("title",    "Unknown Title"))
    artist = sanitize(info.get("uploader", "Unknown Artist"))
    if info.get("artist"):
        artist = sanitize(info["artist"])
    album     = sanitize(info.get("album", info.get("playlist_title", "Unknown Album")))
    thumb_url = ""
    for t in reversed(info.get("thumbnails", [])):
        if t.get("url"):
            thumb_url = t["url"]
            break

    print(f"   Title  : {title}")
    print(f"   Artist : {artist}")
    print(f"   Album  : {album}")

    mp3_filename   = f"{title}.mp3"
    thumb_filename = f"{title}.jpg"

    mp3_path      = os.path.abspath(os.path.join(OUTPUT_FOLDER,    mp3_filename))
    thumb_path    = os.path.abspath(os.path.join(OUTPUT_FOLDER,    thumb_filename))
    dl_mp3_path   = os.path.abspath(os.path.join(DOWNLOADS_FOLDER, mp3_filename))
    dl_thumb_path = os.path.abspath(os.path.join(DOWNLOADS_FOLDER, thumb_filename))
    cover_path    = os.path.abspath(os.path.join(COVERS_FOLDER,    thumb_filename))

    # ffmpeg location
    ffmpeg_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(ffmpeg_dir, "ffmpeg.exe")):
        ffmpeg_dir = ""

    print(f"\nDownloading audio...")
    ydl_opts_dl = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(OUTPUT_FOLDER, f"{title}.%(ext)s"),
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
        "ffmpeg_location": ffmpeg_dir,
        "quiet": False,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts_dl) as ydl:
        ydl.download([info["webpage_url"]])

    if not os.path.exists(mp3_path):
        print(f"MP3 not found: {mp3_path}")
        return

    print(f"   MP3 saved -> {mp3_path}")

    # Copy MP3 to Downloads/ folder
    print(f"\nCopying to Downloads folder...")
    try:
        shutil.copy2(mp3_path, dl_mp3_path)
        print(f"   Copied -> {dl_mp3_path}")
    except Exception as e:
        print(f"   Copy failed: {e}")
        dl_mp3_path = mp3_path  # fallback

    # Download thumbnail
    print(f"\nDownloading thumbnail...")
    thumb_ok = False
    if thumb_url:
        thumb_ok = download_thumbnail(thumb_url, thumb_path)
        if thumb_ok:
            try: shutil.copy2(thumb_path, dl_thumb_path)
            except Exception: dl_thumb_path = thumb_path
            try: shutil.copy2(thumb_path, cover_path)
            except Exception: pass

    final_thumb    = thumb_path    if thumb_ok else FALLBACK_IMG
    dl_final_thumb = dl_thumb_path if thumb_ok else FALLBACK_IMG

    # Embed tags in both copies
    print(f"\nEmbedding tags...")
    embed_tags(mp3_path, title, artist, album, final_thumb)
    try:
        embed_tags(dl_mp3_path, title, artist, album, dl_final_thumb)
    except Exception:
        pass

    duration = get_duration_str(mp3_path)
    print(f"   Duration: {duration}")

    print(f"\nUpdating database...")
    update_database(title, duration, mp3_path, final_thumb, artist, album,
                    dl_mp3_path, dl_final_thumb)

    print(f"\nDone!")
    print(f"   allSongs  -> {mp3_path}")
    print(f"   Downloads -> {dl_mp3_path}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    query = " ".join(sys.argv[1:])
    download(query)
