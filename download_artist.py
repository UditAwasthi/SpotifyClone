"""
Artist Playlist Downloader
===========================
Downloads all songs from a YouTube / YouTube Music artist page, playlist,
or channel — saves MP3s into  artists/[ArtistName]/  and registers them
in the SQLite database so the main player picks them up automatically.

Also downloads the artist's channel avatar and saves it as
artists/[ArtistName]/cover.jpg  (used as the tile image on the home page).

Usage:
    python download_artist.py <Artist Name> <YouTube URL>

URL can be any of:
    • YouTube Music artist page  → https://music.youtube.com/channel/UCxxx
    • YouTube channel            → https://www.youtube.com/@EdSheeran
    • YouTube playlist           → https://www.youtube.com/playlist?list=PLxxx
    • Single video (adds to artist folder) → https://www.youtube.com/watch?v=xxx

Examples:
    python download_artist.py "Ed Sheeran"    https://www.youtube.com/@EdSheeranVEVO
    python download_artist.py "Arijit Singh"  https://www.youtube.com/playlist?list=PLxxx
    python download_artist.py "Alec Benjamin" https://music.youtube.com/channel/UCxxx

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
    print("❌  yt-dlp not found.  Run:  pip install yt-dlp")
    sys.exit(1)

try:
    from mutagen.mp3 import MP3
    from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, ID3NoHeaderError
except ImportError:
    print("❌  mutagen not found.  Run:  pip install mutagen")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("❌  Pillow not found.  Run:  pip install Pillow")
    sys.exit(1)


# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
ARTISTS_ROOT  = "artists"
COVERS_FOLDER = os.path.join("imgs", "covers")
ALL_SONGS_DIR = "allSongs"
DB_PATH       = "Spotify.db"
FALLBACK_IMG  = os.path.join("imgs", "notifi.png")

# ffmpeg location — looks in the same folder as this script first
FFMPEG_DIR = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(os.path.join(FFMPEG_DIR, "ffmpeg.exe")):
    FFMPEG_DIR = ""   # fall back to system PATH

os.makedirs(COVERS_FOLDER, exist_ok=True)
os.makedirs(ALL_SONGS_DIR, exist_ok=True)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def sanitize(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()


def folder_name(artist: str) -> str:
    """Convert 'Ed Sheeran' → 'Ed_Sheeran' for folder & DB table name."""
    return sanitize(artist).replace(" ", "_")


def seconds_fmt(secs: float) -> str:
    m, s = divmod(int(secs), 60)
    return f"{m:02d}:{s:02d}"


def save_thumbnail(url: str, save_path: str, square: bool = True) -> bool:
    """Download image from URL, optionally crop to square, save as JPEG."""
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content)).convert("RGB")
        if square:
            w, h  = img.size
            side  = min(w, h)
            left  = (w - side) // 2
            top   = (h - side) // 2
            img   = img.crop((left, top, left + side, top + side))
            img   = img.resize((500, 500), Image.LANCZOS)
        img.save(save_path, "JPEG", quality=90)
        return True
    except Exception as e:
        print(f"   ⚠️  Thumbnail save failed: {e}")
        return False


def embed_tags(mp3_path: str, title: str, artist: str,
               album: str, thumb_path: str):
    """Embed ID3 tags + cover art into MP3."""
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
    except Exception as e:
        print(f"   ⚠️  Tag embed failed: {e}")


def get_duration(mp3_path: str) -> str:
    try:
        return seconds_fmt(MP3(mp3_path).info.length)
    except Exception:
        return "00:00"


# ─────────────────────────────────────────────
# DATABASE
# ─────────────────────────────────────────────
def get_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    return con, cur


def ensure_artist_table(cur, table: str):
    """Create per-artist table if it doesn't exist."""
    cur.execute(f"""CREATE TABLE IF NOT EXISTS [{table}] (
        Name      VARCHAR(100),
        DURATION  VARCHAR(10),
        FILE_PATH VARCHAR(200),
        IMG_PATH  VARCHAR(200),
        Artist    VARCHAR(100),
        Album     VARCHAR(100)
    )""")


def ensure_all_songs_table(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS all_songs_data (
        Name      VARCHAR(100),
        DURATION  VARCHAR(10),
        FILE_PATH VARCHAR(200),
        IMG_PATH  VARCHAR(200),
        Artist    VARCHAR(100),
        Album     VARCHAR(100)
    )""")
    # Migrate if Album column missing
    cur.execute("PRAGMA table_info(all_songs_data)")
    cols = [r[1] for r in cur.fetchall()]
    if "Album" not in cols:
        cur.execute("ALTER TABLE all_songs_data ADD COLUMN Album VARCHAR(100) DEFAULT ''")


def insert_song(cur, table: str, title: str, duration: str,
                mp3_path: str, thumb_path: str, artist: str, album: str):
    """Insert into both the artist table and all_songs_data (skip duplicates)."""
    row = (title, duration, mp3_path, thumb_path, artist, album)

    # Artist table
    cur.execute(f"SELECT FILE_PATH FROM [{table}] WHERE FILE_PATH = ?", (mp3_path,))
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO [{table}] VALUES (?,?,?,?,?,?)", row)

    # All songs table
    cur.execute("SELECT FILE_PATH FROM all_songs_data WHERE FILE_PATH = ?", (mp3_path,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO all_songs_data VALUES (?,?,?,?,?,?)", row)


# ─────────────────────────────────────────────
# ARTIST COVER
# ─────────────────────────────────────────────
def download_artist_cover(channel_url: str, artist_folder: str):
    """
    Fetch the channel/artist avatar and save as cover.jpg in the artist folder.
    Uses yt-dlp to extract channel info without downloading any video.
    """
    cover_path = os.path.join(artist_folder, "cover.jpg")
    if os.path.exists(cover_path):
        print(f"   🖼  Artist cover already exists, skipping.")
        return cover_path

    print(f"\n🖼  Downloading artist cover art…")
    try:
        opts = {"quiet": True, "extract_flat": True,
                "skip_download": True, "no_warnings": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)

        # Try channel thumbnails first
        thumbs = info.get("thumbnails") or []
        # Also check uploader avatar if present
        avatar_url = info.get("uploader_thumbnail") or info.get("channel_thumbnail")

        chosen_url = avatar_url
        if not chosen_url:
            for t in reversed(thumbs):
                if t.get("url"):
                    chosen_url = t["url"]
                    break

        if chosen_url:
            ok = save_thumbnail(chosen_url, cover_path, square=True)
            if ok:
                print(f"   ✅  Cover saved → {cover_path}")
                return cover_path
    except Exception as e:
        print(f"   ⚠️  Could not fetch artist cover: {e}")

    # Fallback: copy default icon
    try:
        shutil.copy2(FALLBACK_IMG, cover_path)
    except Exception:
        pass
    return cover_path


# ─────────────────────────────────────────────
# CORE – download one song into artist folder
# ─────────────────────────────────────────────
def process_song(entry: dict, artist_name: str, artist_folder: str,
                 table: str, con, cur, total: int, index: int):
    """Download a single song, save thumbnail, embed tags, update DB."""

    raw_title = entry.get("title") or entry.get("id") or "Unknown"
    title     = sanitize(raw_title)
    artist    = sanitize(entry.get("artist") or entry.get("uploader") or artist_name)
    album     = sanitize(entry.get("album") or entry.get("playlist_title") or artist_name)

    mp3_filename   = f"{title}.mp3"
    thumb_filename = f"{title}.jpg"
    mp3_path       = os.path.abspath(os.path.join(artist_folder, mp3_filename))
    thumb_path     = os.path.abspath(os.path.join(artist_folder, thumb_filename))
    cover_copy     = os.path.abspath(os.path.join(COVERS_FOLDER, thumb_filename))
    allsongs_mp3   = os.path.abspath(os.path.join(ALL_SONGS_DIR, mp3_filename))

    print(f"\n  [{index}/{total}]  🎵  {title}")
    print(f"           🎤  {artist}  |  💿  {album}")

    # Skip if already downloaded
    if os.path.exists(mp3_path):
        print(f"           ⏭️   Already downloaded, updating DB only")
        duration = get_duration(mp3_path)
        final_thumb = thumb_path if os.path.exists(thumb_path) else FALLBACK_IMG
        insert_song(cur, table, title, duration, mp3_path, final_thumb, artist, album)
        con.commit()
        return

    # ── Download audio ──
    video_url = entry.get("webpage_url") or entry.get("url") or \
                f"https://www.youtube.com/watch?v={entry.get('id', '')}"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(artist_folder, f"{title}.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "ffmpeg_location": FFMPEG_DIR,
        "quiet": True,
        "no_warnings": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"           ✅  MP3 saved")
    except Exception as e:
        print(f"           ❌  Download failed: {e}")
        return

    if not os.path.exists(mp3_path):
        print(f"           ❌  MP3 not found after download")
        return

    # ── Thumbnail ──
    thumb_ok  = False
    thumb_url = ""
    for t in reversed(entry.get("thumbnails") or []):
        if t.get("url"):
            thumb_url = t["url"]
            break
    if thumb_url:
        thumb_ok = save_thumbnail(thumb_url, thumb_path)
        if thumb_ok:
            try: shutil.copy2(thumb_path, cover_copy)
            except Exception: pass

    final_thumb = thumb_path if thumb_ok else FALLBACK_IMG
    print(f"           🖼  {'Thumbnail saved' if thumb_ok else 'Using fallback thumbnail'}")

    # ── Embed tags ──
    embed_tags(mp3_path, title, artist, album, final_thumb)
    print(f"           🏷  Tags embedded")

    # ── Duration ──
    duration = get_duration(mp3_path)
    print(f"           ⏱  {duration}")

    # ── DB ──
    insert_song(cur, table, title, duration, mp3_path, final_thumb, artist, album)
    con.commit()
    print(f"           💾  Added to database")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def download_artist(artist_name: str, url: str):
    fname  = folder_name(artist_name)
    table  = fname
    artist_folder = os.path.join(ARTISTS_ROOT, fname)
    os.makedirs(artist_folder, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  🎤  Artist : {artist_name}")
    print(f"  📁  Folder : {artist_folder}")
    print(f"  🔗  URL    : {url}")
    print(f"{'='*60}")

    # ── Setup DB ──
    con, cur = get_db()
    ensure_artist_table(cur, table)
    ensure_all_songs_table(cur)
    con.commit()

    # ── Download artist cover ──
    download_artist_cover(url, artist_folder)

    # ── Extract playlist / channel entries ──
    print(f"\n📋  Fetching track list…")
    ydl_info_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",   # get list without downloading
        "skip_download": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_info_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"❌  Failed to fetch info: {e}")
        return

    # Flatten entries
    entries = []
    if "entries" in info:
        for e in info["entries"]:
            if e is None:
                continue
            # Nested playlist (e.g. channel → playlists → videos)
            if "entries" in (e or {}):
                entries.extend([x for x in e["entries"] if x])
            else:
                entries.append(e)
    else:
        entries = [info]  # single video

    total = len(entries)
    print(f"   Found {total} track(s)\n")

    failed = []
    for i, entry in enumerate(entries, 1):
        try:
            # Re-fetch full entry info so we get thumbnails & metadata
            video_id  = entry.get("id") or entry.get("url", "")
            video_url = entry.get("webpage_url") or \
                        (f"https://www.youtube.com/watch?v={video_id}" if video_id else None)
            if not video_url:
                print(f"  [{i}/{total}]  ⚠️  Skipping entry with no URL")
                continue

            full_opts = {"quiet": True, "no_warnings": True, "skip_download": True}
            with yt_dlp.YoutubeDL(full_opts) as ydl:
                full_entry = ydl.extract_info(video_url, download=False)

            process_song(full_entry, artist_name, artist_folder,
                         table, con, cur, total, i)
        except Exception as e:
            print(f"  [{i}/{total}]  ❌  Error: {e}")
            failed.append(entry.get("title", entry.get("id", "unknown")))

    con.close()

    print(f"\n{'='*60}")
    print(f"  ✅  Finished!  {total - len(failed)}/{total} songs downloaded")
    if failed:
        print(f"  ⚠️  Failed ({len(failed)}):")
        for f in failed:
            print(f"      - {f}")
    print(f"  📁  Saved to: {artist_folder}")
    print(f"{'='*60}\n")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(0)

    # argv[1] = artist name (quoted), argv[2] = URL
    artist_arg = sys.argv[1]
    url_arg    = sys.argv[2]

    download_artist(artist_arg, url_arg)
