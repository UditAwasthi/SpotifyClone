# 🎵 Spotify Clone — Local Music Player

A fully offline, Spotify-inspired desktop music player built with Python. Stream your local MP3 library, browse artist pages, manage playlists, and download songs directly from YouTube — all with a sleek dark UI.

---

## ✨ Features

- 🎨 **Spotify-like dark UI** built with CustomTkinter
- 🎵 **Local music playback** with play / pause / next / previous controls
- 📁 **Auto-scan library** — drop MP3s into `allSongs/` and they appear instantly
- 🎤 **Artist pages** — dedicated pages per artist with cover art and song list
- 📋 **Playlists** — create, manage, and add songs to custom playlists
- 🕓 **History** — automatically tracks recently played songs
- 📥 **Downloads page** — songs downloaded from YouTube appear here
- 🔍 **Search** — search your local library or find songs online via YouTube
- ⬇️ **YouTube downloader** — download any song or full artist playlist as MP3
- 🖼️ **Thumbnails** — auto-extracts album art from MP3 ID3 tags or downloads from YouTube
- 💾 **SQLite database** — no MySQL required, everything stored locally

---

## 📁 Project Structure

```
Spotify/
│
├── main.py                  # Main application
├── downloader_script.py     # Download individual songs from YouTube
├── download_artist.py       # Download full artist playlists from YouTube
├── ffmpeg.exe               # Required for audio conversion
├── ffprobe.exe              # Required for audio conversion
├── Spotify.db               # SQLite database (auto-created)
│
├── allSongs/                # All songs library (MP3 + thumbnail .jpg)
│   ├── Shape of You.mp3
│   └── Shape of You.jpg
│
├── Downloads/               # Songs downloaded via downloader (shown on Downloads page)
│   ├── Blinding Lights.mp3
│   └── Blinding Lights.jpg
│
├── artists/                 # Per-artist folders
│   ├── Ed_Sheeran/
│   │   ├── cover.jpg        # Artist tile image (auto-downloaded)
│   │   ├── Perfect.mp3
│   │   └── Perfect.jpg
│   └── Arijit_Singh/
│       ├── cover.jpg
│       └── Tum Hi Ho.mp3
│
├── imgs/                    # UI icons and assets
│   ├── covers/              # Cached thumbnails for player UI
│   └── notifi.png           # Fallback thumbnail
│
└── playlist_images/         # User-created playlist cover images
```

---

## 🚀 Setup

### 1. Install Python dependencies

```bash
pip install customtkinter pygame mutagen Pillow requests yt-dlp ytmusicapi pywinstyles
```

### 2. Install FFmpeg

Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and place **`ffmpeg.exe`** and **`ffprobe.exe`** in your project folder (same directory as `main.py`).

### 3. Add your music

Place MP3 files into the appropriate folders:

```
allSongs/          ← general library
artists/Ed_Sheeran/   ← artist-specific songs
```

### 4. Run the app

```bash
python main.py
```

The app will automatically scan your folders, extract metadata, and populate the database on startup.

---

## ⬇️ Downloading Songs from YouTube

### Download a single song

```bash
# By search query
python downloader_script.py Shape of You Ed Sheeran

# By URL
python downloader_script.py https://www.youtube.com/watch?v=JGwWNGJdvx8
```

This will:
- Download the song as a **192kbps MP3** into `allSongs/` and `Downloads/`
- Download the **thumbnail** and embed it as cover art in the MP3
- Add the song to the database — it appears in the app immediately

### Download a full artist playlist

```bash
python download_artist.py "Ed Sheeran"    https://www.youtube.com/@EdSheeranVEVO
python download_artist.py "Arijit Singh"  https://www.youtube.com/playlist?list=PLxxx
python download_artist.py "Taylor Swift"  https://music.youtube.com/channel/UCxxx
```

This will:
- Create `artists/Ed_Sheeran/` folder automatically
- Download the **channel avatar** as `cover.jpg` (shown as artist tile on home page)
- Download all songs with thumbnails and embedded ID3 tags
- Register songs in both the artist table and the main library
- **Skip already-downloaded songs** — safe to re-run if interrupted

---

## 🗃️ Database Schema

The app uses a local **SQLite** database (`Spotify.db`) with these tables:

| Table | Columns | Description |
|---|---|---|
| `all_songs_data` | Name, DURATION, FILE_PATH, IMG_PATH, Artist, Album | Main song library |
| `Downloads` | Name, DURATION, FILE_PATH, IMG_PATH, Artist | Downloaded songs page |
| `History` | Name, DURATION, FILE_PATH, IMG_PATH, Artist, TIME | Recently played |
| `Playlists_data` | Name, Description, IMG_Path | Playlist metadata |
| `[playlist_name]` | Name, DURATION, FILE_PATH, IMG_PATH, Artist, Album | Per-playlist songs |
| `[Artist_Name]` | Name, DURATION, FILE_PATH, IMG_PATH, Artist, Album | Per-artist songs |

---

## 🎮 Controls

| Action | How |
|---|---|
| Play / Pause | Click the play button or song tile |
| Next / Previous | Arrow buttons in the player bar |
| Seek | Drag the progress slider |
| Volume | Drag the volume slider |
| Add to playlist | Click ➕ icon on any song row |
| Delete song | Click 🗑️ icon on any song row |
| Search offline | Search tab → Offline |
| Search YouTube | Search tab → Online |

---

## 🛠️ Troubleshooting

**`no such table: ArtistName`**
The artist table hasn't been created yet. Run `download_artist.py` for that artist first, or add MP3s to `artists/ArtistName/` and restart the app.

**`ffprobe and ffmpeg not found`**
Place `ffmpeg.exe` and `ffprobe.exe` in the same folder as `downloader_script.py`.

**Song doesn't appear after download**
Restart the app — it rescans the database on launch. Or check that the song was added to `all_songs_data` in `Spotify.db`.

**Thumbnail not showing**
The MP3 may not have embedded cover art. Re-download via `downloader_script.py` which embeds the thumbnail automatically.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `customtkinter` | UI framework |
| `pygame` | Audio playback |
| `mutagen` | MP3 metadata / ID3 tags |
| `Pillow` | Image processing |
| `yt-dlp` | YouTube audio download |
| `requests` | Thumbnail download |
| `ytmusicapi` | YouTube Music search |
| `pywinstyles` | Windows UI styling |
| `ffmpeg` | Audio format conversion |

---

## 👨‍💻 Credits

Built by **Udit Awasthi**

