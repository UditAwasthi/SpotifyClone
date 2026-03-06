import time
import webbrowser
from datetime import datetime
import pywinstyles
from customtkinter import *
import threading
# from moviepy.editor import *
from ytmusicapi import YTMusic
from pytube import Playlist,YouTube
# from youtubesearchpython import *
import urllib.request
import sqlite3 as sq
from PIL import Image,ImageFilter, ImageTk,ImageDraw
import math
from pygame import mixer
global playlist_but1,playlist_but2
playlist_but1=[]
playlist_but2=[]
def open_insta():
    url = r"https://www.instagram.com/udit_awasthi_/"
    webbrowser.open(url)
def open_Youtube():
    url2 = r"https://youtube.com/@udit-tj2oy?si=tlD56g7dVoJVUCLx"
    webbrowser.open(url2)
def convert_minutes_to_seconds(time_str):
    try:
        minutes, seconds = map(int, time_str.split(':'))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    except :
        pass
set_appearance_mode("dark")
name="Alec_Benjamin"
mycon = sq.connect('Spotify.db')
cur = mycon.cursor()
def delete_row_from_all_tables(row_id,parent):

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Iterate over each table and delete the row with the specified ID
    for table in tables:
        table_name = table[0]
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE Name = ?", (row_id[0],))
            mycon.commit()
            parent.destroy()

        except:
            pass
def delete_row_from_playlist(row_id,parent,tableee):
    try:
        cur.execute(f"DELETE FROM {tableee} WHERE Name = ?", (row_id[0],))
        mycon.commit()
        parent.destroy()

    except:
        pass

home_im = CTkImage(light_image=Image.open("imgs\\Home.png"),dark_image=Image.open("imgs\\Home.png"),size=(27,27))
home_om = CTkImage(light_image=Image.open("imgs\\HomeUn.png"),dark_image=Image.open("imgs\\HomeUn.png"),size=(27,27))
searchw_im = CTkImage(light_image=Image.open("imgs\\searchw.png"),dark_image=Image.open("imgs\\searchw.png"),size=(27,27))
searchw_om = CTkImage(light_image=Image.open("imgs\\search69.png"),dark_image=Image.open("imgs\\search69.png"),size=(27,27))
library1 = CTkImage(light_image=Image.open("imgs\\library1.png"),dark_image=Image.open("imgs\\library1.png"),size=(27,27))
library2 = CTkImage(light_image=Image.open("imgs\\Library.png"),dark_image=Image.open("imgs\\Library.png"),size=(27,27))
backdis = CTkImage(light_image=Image.open("imgs\\backd.png"),dark_image=Image.open("imgs\\backd.png"),size=(32,32))
note = CTkImage(light_image=Image.open("imgs\\notifi.png"),dark_image=Image.open("imgs\\notifi.png"),size=(35,35))
noteon = CTkImage(light_image=Image.open("imgs\\notifihi.png"),dark_image=Image.open("imgs\\notifihi.png"),size=(35,35))
backen = CTkImage(light_image=Image.open("imgs\\back.png"),dark_image=Image.open("imgs\\back.png"),size=(32,32))
fordis = CTkImage(light_image=Image.open("imgs\\frontd.png"),dark_image=Image.open("imgs\\frontd.png"),size=(32,32))
foren = CTkImage(light_image=Image.open("imgs\\forward.png"),dark_image=Image.open("imgs\\forward.png"),size=(32,32))
down = CTkImage(light_image=Image.open("imgs\\down.png"),dark_image=Image.open("imgs\\down.png"),size=(20,20))
hover_image = CTkImage(light_image=Image.open("imgs\\hover_image.png"),dark_image=Image.open("imgs\\hover_image.png"),size=(70,70))
t1 = CTkImage(light_image=Image.open("imgs\\tsg.jpg"),dark_image=Image.open("imgs\\tsg.jpg"),size=(170,170))
t2 = CTkImage(light_image=Image.open("imgs\\tsi.jpg"),dark_image=Image.open("imgs\\tsi.jpg"),size=(170,170))
t3 = CTkImage(light_image=Image.open("imgs\\t50ind.jpg"),dark_image=Image.open("imgs\\t50ind.jpg"),size=(170,170))
t4 = CTkImage(light_image=Image.open("imgs\\t50glob.jpg"),dark_image=Image.open("imgs\\t50glob.jpg"),size=(170,170))
t5 = CTkImage(light_image=Image.open("imgs\\t50vglob.jpg"),dark_image=Image.open("imgs\\t50vglob.jpg"),size=(170,170))
soep1 = CTkImage(light_image=Image.open("imgs\\joerogan.jpg"),dark_image=Image.open("imgs\\joerogan.jpg"),size=(170,170))
soep2 = CTkImage(light_image=Image.open("imgs\\beerbicep.jpg"),dark_image=Image.open("imgs\\beerbicep.jpg"),size=(170,170))
soep3 = CTkImage(light_image=Image.open("imgs\\horr.jpg"),dark_image=Image.open("imgs\\horr.jpg"),size=(170,170))
soep4 = CTkImage(light_image=Image.open("imgs\\krishle.jpg"),dark_image=Image.open("imgs\\krishle.jpg"),size=(170,170))
soep5 = CTkImage(light_image=Image.open("imgs\\gtp.jpg"),dark_image=Image.open("imgs\\gtp.jpg"),size=(170,170))
play1 = CTkImage(light_image=Image.open("imgs\\play.png"),dark_image=Image.open("imgs\\play.png"),size=(40,40))
pause1 = CTkImage(light_image=Image.open("imgs\\pause.png"),dark_image=Image.open("imgs\\pause.png"),size=(40,40))
next1 = CTkImage(light_image=Image.open("imgs\\nextun.png"),dark_image=Image.open("imgs\\nextun.png"),size=(20,20))
previous1 = CTkImage(light_image=Image.open("imgs\\previousun.png"),dark_image=Image.open("imgs\\previousun.png"),size=(20,20))
next2 = CTkImage(light_image=Image.open("imgs\\next.png"),dark_image=Image.open("imgs\\next.png"),size=(20,20))
previous2 = CTkImage(light_image=Image.open("imgs\\previous.png"),dark_image=Image.open("imgs\\previous.png"),size=(20,20))
alb1 = CTkImage(light_image=Image.open("imgs\\1.png"),dark_image=Image.open("imgs\\1.png"),size=(170,170))
alb2 = CTkImage(light_image=Image.open("imgs\\2.png"),dark_image=Image.open("imgs\\2.png"),size=(170,170))
alb3 = CTkImage(light_image=Image.open("imgs\\3.png"),dark_image=Image.open("imgs\\3.png"),size=(170,170))
alb4 = CTkImage(light_image=Image.open("imgs\\4.png"),dark_image=Image.open("imgs\\4.png"),size=(170,170))
alb5 = CTkImage(light_image=Image.open("imgs\\5.png"),dark_image=Image.open("imgs\\5.png"),size=(170,170))
alb6 = CTkImage(light_image=Image.open("imgs\\6.png"),dark_image=Image.open("imgs\\6.png"),size=(170,170))
alb7 = CTkImage(light_image=Image.open("imgs\\7.png"),dark_image=Image.open("imgs\\7.png"),size=(170,170))
alb8 = CTkImage(light_image=Image.open("imgs\\8.png"),dark_image=Image.open("imgs\\8.png"),size=(170,170))
alb9 = CTkImage(light_image=Image.open("imgs\\9.png"),dark_image=Image.open("imgs\\9.png"),size=(170,170))
alb10 = CTkImage(light_image=Image.open("imgs\\10.png"),dark_image=Image.open("imgs\\10.png"),size=(170,170))
add = CTkImage(light_image=Image.open("imgs\\add.png"),dark_image=Image.open("imgs\\add.png"),size=(20,20))
adde = CTkImage(light_image=Image.open("imgs\\adde.png"),dark_image=Image.open("imgs\\adde.png"),size=(20,20))

app = CTk()
app.geometry("800x800")
app.configure(fg_color="#000000",font=('CircularSp',25))

class HoverButton(CTkButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        if self._text == "Home":
            self.configure(text="Home", compound=LEFT, anchor='w', image=home_om, font=("CircularSp", 16, "bold"), text_color="white")
        elif self._text == "Search":
            self.configure(text="Search", compound=LEFT, anchor='w', image=searchw_im, font=("CircularSp", 16, "bold"), text_color="white")
        elif self._text == "Your Library":
            self.configure(text="Your Library", compound=LEFT, anchor='w', image=library2, font=("CircularSp", 16, "bold"), text_color="white")
            global a
            a=CTkLabel(app, text="Collapse Your Library", text_color="white",fg_color="#282828",bg_color="#121212",font=("CircularSp", 15, "bold"),width=180,corner_radius=5,height=30)
            a.place(x=10, y=100)
        elif self._text == "➕":
            self.configure(text="➕", compound=LEFT, anchor='w', font=("CircularSp", 20, "bold"), text_color="white")
            global bd
            bd=CTkLabel(app, text="Create Playlist or Folder", text_color="white",fg_color="#282828",bg_color="#121212",font=("CircularSp", 16, "bold"),width=180,corner_radius=5,height=30)
            bd.place(x=250, y=100)
        elif self._text == "➔":
            self.configure(text="➔", compound=LEFT, anchor='w', font=("CircularSp", 27, "bold"), text_color="white")
            global bdc
            bdc=CTkLabel(app, text="Show More", text_color="white",fg_color="#282828",bg_color="#121212",font=("CircularSp", 16, "bold"),width=100,corner_radius=5,height=30)
            bdc.place(x=350, y=100)
        elif self._text == "Create playlist":
            self.configure(width=128,height=33,font=("CircularSp", 13.5,"bold"))
            self.place(x=18,y=85)
        elif self._text == "Browse Podcasts":
            self.configure(width=145,height=33,font=("CircularSp", 13.5,"bold"))
            self.place(x=18,y=85)
        elif self._text == "MY Instagram":
            self.configure(width=135, height=35, font=("CircularSp", 15, "bold"))
        elif self._text == "MY YouTube":
            self.configure(width=145, height=38, font=("CircularSp", 15, "bold"))
        elif self._text == " ":
            self.configure(image=noteon)
        elif self._text == "Try something else":
            self.configure(font = ("CircularSp", 25, "bold", "underline"))
        elif self._text == "Downloads":
            self.configure(font = ("CircularSp", 25, "bold", "underline"))
        elif self._text == "Show All":
            self.configure(font=("CircularSp", 15,"bold", "underline"))
        elif self._text == "Recently Played":
            self.configure(font=("CircularSp", 25,"bold", "underline"))
        elif self._text == "Featured Charts":
            self.configure(font=("CircularSp", 25,"bold", "underline"))
        elif self._text == "Spotify Podcasts":
            self.configure(font=("CircularSp", 25,"bold", "underline"))
        elif self._text == "":
            self.configure(image=add)
        elif self._text == "  ":
            self.configure(image=searchw_im)


    def on_leave(self, event):
        if self._text == "Home":
            self.configure(text="Home", compound=LEFT, anchor='w', image=home_im, font=("CircularSp", 16, "bold"), text_color="#696969")
        elif self._text == "Search":
            self.configure(text="Search", compound=LEFT, anchor='w', image=searchw_om, font=("YCircularSp", 16, "bold"), text_color="#696969")
        elif self._text == "Your Library":
            self.configure(text="Your Library", compound=LEFT, anchor='w', image=library1, font=("CircularSp", 16, "bold"), text_color="#696969")
            a.destroy()
        elif self._text == "➕":
            self.configure(text="➕", compound=LEFT, anchor='w',  font=("CircularSp", 18), text_color="#696969")
            bd.destroy()
        elif self._text == "➔":
            self.configure(text="➔", compound=LEFT, anchor='w',  font=("CircularSp", 25), text_color="#696969")
            bdc.destroy()
        elif self._text == "Create playlist":
            self.configure(width=125,height=32,font=("CircularSp", 13,"bold"))
            self.place(x=20,y=85)
        elif self._text == "Browse Podcasts":
            self.configure(width=125,height=32,font=("CircularSp", 13,"bold"))
            self.place(x=20,y=85)
        elif self._text == "MY Instagram":
            self.configure(width=125, height=32, font=("CircularSp", 13, "bold"))
        elif self._text == "MY YouTube":
            self.configure(width=125, height=32, font=("CircularSp", 13, "bold"))
        elif self._text == " ":
            self.configure(image=note)
        elif self._text == "Try something else":
            self.configure(font=("CircularSp", 25,"bold"))
        elif self._text == "Downloads":
            self.configure(font = ("CircularSp", 25, "bold"))
        elif self._text == "Show All":
            self.configure(font=("CircularSp", 15,"bold"))
        elif self._text == "Recently Played":
            self.configure(font=("CircularSp", 25,"bold"))
        elif self._text == "Featured Charts":
            self.configure(font=("CircularSp", 25,"bold"))
        elif self._text == "Spotify Podcasts":
            self.configure(font=("CircularSp", 25,"bold"))
        elif self._text == "":
            self.configure(image=adde)
        elif self._text == "  ":
            self.configure(image=searchw_om)

def hero():
    global app1
    FULL_frame()
    try:
        tabview.place(x=2000,y=12333)
    except:
        pass
    global k
    k = CTkButton(ltop,text="Home",compound=LEFT,anchor='w',image=home_om,text_color="white",fg_color="#121212",font=("CircularSp", 16, "bold"),hover_color="#121212",width = 331,height = 35)
    k.place(x=12,y=12)

    try:
        k1.destroy()
    except:
        pass
def hero1():
    se_ar_ch()
    Search_but1.configure(image=searchw_im)
    Search_but1.configure(command=FULL_frame)
    global k1
    k1 = CTkButton(ltop,text="Search",compound=LEFT,anchor='w',image=searchw_im,text_color="white",fg_color="#121212",font=("CircularSp", 16, "bold"),hover_color="#121212",width = 331,height = 35)
    k1.place(x=12,y=60)

    try:
        k.destroy()
    except:
        pass

ltop = CTkFrame(app,width=320,height=112,fg_color='#121212')
ltop.place(x=5,y=5)
home_but = HoverButton(ltop,text="Home",compound=LEFT,anchor='w',image=home_im,text_color="gray",fg_color="#121212",font=("CircularSp", 16, "bold"),hover_color="#121212",width = 300,height = 35,command=hero)
home_but.place(x=12,y=12)
def se_ar_ch():
    global tabview
    collapse()
    short_frame()
    home_but_s.configure(command=hero)
    Search_but1.configure(command=hero)
    tabview = CTkTabview(master=app,height=700,width=1435,fg_color="#111111")
    tabview.place(x=100,y=0)

    tabview.add("Offline")  # add tab at the end
    tabview.add("Online")  # add tab at the end
    app1 = CTkFrame(tabview.tab("Offline"),fg_color="black", width=1420, height=600)
    app1.place(x=0,y=10)
    cur.execute("SELECT * FROM all_songs_data")
    data = cur.fetchall()
    global search_results,SearchFrame
    def find_matching_songs():
        j = 0
        k = 0
        search_keyword = entry.get().strip()
        global search_results
        search_results.destroy()
        search_results = CTkScrollableFrame(app1, fg_color="#000000",scrollbar_button_color="white", width=1420, height=600)
        search_results.place(x=5, y=110)
        for song_tuple in data:

            if search_keyword.title() in song_tuple[0] or search_keyword.lower() in song_tuple[0] or search_keyword.upper() in song_tuple[0]:
                if j==7:
                    j=0
                    k+=1
                create_song_label(song_tuple, j,k)
                j += 1

    search_image = CTkImage(light_image=Image.open(r"imgs\search69.png"), dark_image=Image.open(r"imgs\search69.png"),
                            size=(20, 20))
    search_image1 = CTkImage(light_image=Image.open(r"imgs\searchw.png"), dark_image=Image.open(r"imgs\searchw.png"),
                             size=(20, 20))

    SearchFrame = CTkFrame(app1, width=1400, height=300)
    SearchFrame.place(x=5, y=5)

    search_widgets = CTkEntry(SearchFrame, fg_color="#121212", width=1400, height=100, text_color="#121212")
    search_widgets.pack()

    def on_focus_in(event):
        entry.configure(border_color="white")
        search.configure(text="", image=search_image1)

    def on_focus_out(event):
        entry.configure(border_color="#242424")
        search.configure(entry, text="", image=search_image)

    entry = CTkEntry(search_widgets, placeholder_text="   What do you want to play?", font=("Circular Sp", 14),
                     fg_color="#242424", border_color="#242424", corner_radius=1250, width=800, height=50)
    entry.place(x=110, y=20)

    search = CTkButton(entry, text="", width=20, fg_color="#242424", hover_color="#242424", image=search_image,
                       command=find_matching_songs)
    search.place(x=730, y=10)
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    search_results = CTkScrollableFrame(app1,width=1400, height=600)
    search_results.place(x=0, y=110)
    def create_song_label(song_tuple, j,k):

        tile = CTkButton(search_results, text=song_tuple[0][0:20]+"\n ~"+song_tuple[4],
                         image=CTkImage(light_image=Image.open(song_tuple[3]), dark_image=Image.open(song_tuple[3]),
                                        size=(100, 100)), compound="top",
                         anchor='n', height=180, border_spacing=0, font=("CircularSp", 15, "bold"), border_width=0,
                         fg_color="#000000", corner_radius=12, hover_color="#1a1a1a")

        tile.grid(row=k, column=j)

        tile.configure(command=lambda path=song_tuple: replace_extension(path))

    def on():
        app2 = CTkFrame(tabview.tab("Online"), fg_color="black", width=1420, height=700)
        app2.place(x=0, y=10)
        ytmusic = YTMusic()

        def move_label_left(l1, l2, l3, m):
            l1.place(x=1600, y=0)
            l2.place(x=1600, y=0)
            l3.place(x=1600, y=0)
            m.place(x=0, y=0)

        def move_label_right(l1, l2, l3, mainframe):
            l1.place(x=1600, y=0)
            l2.place(x=1600, y=0)
            l3.place(x=1600, y=0)
            mainframe.place(x=0, y=0)

        def search(search_type, root):
            root1 = CTkScrollableFrame(root, width=1350, height=480, fg_color="#121212", scrollbar_fg_color="#121212",
                                       scrollbar_button_hover_color="#121212", scrollbar_button_color="#121212",
                                       border_color="#111111", corner_radius=0)
            root1.place(x=40, y=110)
            global results
            # Perform the search based on the selected type
            if search_type == "Artist":
                results = ytmusic.search(search_entry.get(), filter="artists")

                def a():
                    nb = 0
                    i, x = 0, 0
                    for index, result in list(enumerate(results)):
                        try:
                            index -= nb
                            thumbnail_url = result['thumbnails'][1]['url']
                            thumbnail_path = f"temp.jpg"
                            urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                            # Open the image and get its dimensions
                            img = Image.open(thumbnail_path)
                            width, height = img.size

                            # Crop the image to make it square
                            new_width = min(width, height)
                            left = (width - new_width) // 2
                            right = width - (width - new_width) // 2
                            img = img.crop((left, 0, right, new_width))

                            # Resize the image to 140x140 pixels
                            img = img.resize((120, 120))

                            # Convert the image to ImageTk format
                            img = ImageTk.PhotoImage(img)
                            tile1 = CTkButton(root1, text=result['artist'][0:20], image=img, compound="left",
                                              anchor='w', height=125,
                                              width=320,
                                              border_spacing=0, font=("CircularSp", 18, "bold"), border_width=0,
                                              fg_color="#282828",
                                              corner_radius=0, hover_color="#222222", text_color="white",
                                              command=lambda r=result, r1=root, r2=root1: show_id(r['browseId'], r1,
                                                                                                  r2))
                            tile1.grid(row=x, column=i, padx=5, pady=5)

                            i += 1
                            if i == 4:
                                i = 0
                                x += 1

                        except:
                            nb += 1

                t1 = threading.Thread(target=a, args=())
                t1.start()
            elif search_type == "Playlist":
                results = ytmusic.search(search_entry1.get(), filter="playlists")

                def a():
                    nb = 0
                    i, x = 0, 0
                    for index, result in list(enumerate(results)):
                        try:
                            index -= nb
                            thumbnail_url = result['thumbnails'][-1]['url']
                            thumbnail_path = f"temp.jpg"
                            urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                            # Open the image and get its dimensions
                            img = Image.open(thumbnail_path)
                            # Convert the image to ImageTk format
                            img = CTkImage(light_image=img, dark_image=img, size=(180, 180))
                            tile1 = CTkButton(root1,
                                              text=result['title'][0:20] + "\n" + result['author'][0:20] + "\n" + result[
                                                  'itemCount'], image=img, compound="top", height=220,width=200, border_spacing=0,
                                              font=("CircularSp", 12, "bold"), border_width=0, fg_color="#242424",
                                              corner_radius=12, hover_color="#222222",
                                              command=lambda r=result, r1=root, r2=root1: show_id1(
                                                  'https://www.youtube.com/playlist?list=' + r['browseId'].lstrip("VL"),
                                                  r1, r2))
                            tile1.grid(row=x, column=i, padx=5, pady=5)

                            i += 1
                            if i == 6:
                                i = 0
                                x += 1
                        except:
                            nb += 1

                t1 = threading.Thread(target=a, args=())
                t1.start()
            elif search_type == "Album":
                results = ytmusic.search(search_entry2.get(), filter="albums")

                def a():
                    nb = 0
                    i, x = 0, 0
                    for index, result in list(enumerate(results)):
                        try:
                            index -= nb
                            thumbnail_url = result['thumbnails'][-1]['url']
                            thumbnail_path = f"temp.jpg"
                            urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                            # Open the image and get its dimensions
                            img = Image.open(thumbnail_path)
                            # Convert the image to ImageTk format
                            img = CTkImage(light_image=img, dark_image=img, size=(180, 180))
                            k = ''
                            for index1,j in enumerate(result['artists']):
                                k += j['name'][0:20] + "\n"

                            tile1 = CTkButton(root1, text=result['title'][0:20] + "\n" + k, image=img, compound="top",
                                              height=250,width=200, border_spacing=0, font=("CircularSp", 15, "bold"),
                                              border_width=0, fg_color="#242424", corner_radius=12,
                                              hover_color="#222222",
                                              command=lambda r=result, r1=root, r2=root1: show_id3(r['browseId'], r1,
                                                                                                   r2))
                            tile1.grid(row=x, column=i, padx=5, pady=5)

                            i += 1
                            if i == 6:
                                i = 0
                                x += 1
                        except:
                            nb += 1

                t1 = threading.Thread(target=a, args=())
                t1.start()
            elif search_type == "Song":
                results = ytmusic.search(search_entry3.get(), filter="songs")

                def a():
                    nb = 0
                    i, x = 0, 0
                    for index, result in list(enumerate(results)):

                        try:
                            index -= nb
                            thumbnail_url = result['thumbnails'][0]['url']
                            thumbnail_path = f"temp.jpg"
                            urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                            # Open the image and get its dimensions
                            img = Image.open(thumbnail_path)
                            width, height = img.size

                            # Crop the image to make it square
                            new_width = min(width, height)
                            left = (width - new_width) // 2
                            right = width - (width - new_width) // 2
                            img = img.crop((left, 0, right, new_width))

                            # Resize the image to 140x140 pixels
                            img = img.resize((120, 120))

                            # Convert the image to ImageTk format
                            img = ImageTk.PhotoImage(img)
                            tile1 = CTkButton(root1, text=result['title'][0:20], image=img, compound="left", anchor='w',
                                              height=125, width=320,
                                              border_spacing=0, font=("CircularSp", 15, "bold"), border_width=0,
                                              fg_color="#282828",
                                              corner_radius=0, hover_color="#222222", text_color="white",
                                              command=lambda
                                                  x="https://www.youtube.com/watch?v=" + result[
                                                      'videoId']: download_song(x))
                            tile1.grid(row=x, column=i, padx=5, pady=5)

                            i += 1
                            if i == 4:
                                i = 0
                                x += 1
                        except:
                            nb += 1
                            pass

                t1 = threading.Thread(target=a, args=())
                t1.start()

        def download_song(yt1):
            def run():
                os.system(f"python downloader_script.py {yt1}")



            t = threading.Thread(target=run, args=())
            t.start()


        def show_id3(video_id, root, r2):
            root2 = CTkScrollableFrame(root, width=1350, height=480, fg_color="#121212", scrollbar_fg_color="#121212",
                                       scrollbar_button_hover_color="#ffffff", scrollbar_button_color="#ffffff",
                                       border_color="#111111", corner_radius=0)
            root2.place(x=30, y=110)

            def root_des():
                root2.place(x=5000, y=5000)

                def r2_dis():
                    r2.place(x=5000, y=5000)

                but.configure(command=r2_dis)

            but = CTkButton(root, text="close", command=root_des)
            but.place(x=0, y=0)
            playlist = ytmusic.get_album(video_id)

            def a(x, y):
                nb = 0
                for index, i in enumerate(playlist['tracks'][x:y]):
                    try:
                        index -= nb
                        yt = YouTube("https://www.youtube.com/watch?v=" + i['videoId'])

                        thumbnail_url = yt.thumbnail_url
                        thumbnail_path = f"temp.jpg"
                        urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                        # Open the image and get its dimensions
                        img = Image.open(thumbnail_path)
                        width, height = img.size

                        # Crop the image to make it square
                        new_width = min(width, height)
                        left = (width - new_width) // 2
                        right = width - (width - new_width) // 2
                        img = img.crop((left, 0, right, new_width))

                        # Resize the image to 140x140 pixels
                        img = img.resize((120, 120))

                        # Convert the image to ImageTk format
                        img = ImageTk.PhotoImage(img)
                        jkl = yt.title[0:20] + "\n" + yt.title[21:37]
                        if len(yt.title) >= 40:
                            jkl += "..."
                        tile1 = CTkButton(root2, text=jkl, image=img,
                                          compound="left", anchor='w', width=320, height=125, border_spacing=0,
                                          font=("CircularSp", 18, "bold"), border_width=0, fg_color="#121212",
                                          corner_radius=0,
                                          hover_color="#1a1a1a")
                        tile1.grid(row=x, column=index, padx=5, pady=5)

                        tile1.configure(
                            command=lambda x="https://www.youtube.com/watch?v=" + i['videoId']: download_song(x))

                    except:
                        nb += 1

                        pass

            t1 = threading.Thread(target=a, args=(0, 4))
            t2 = threading.Thread(target=a, args=(4, 8))
            t3 = threading.Thread(target=a, args=(8, 12))
            t4 = threading.Thread(target=a, args=(12, 16))
            t5 = threading.Thread(target=a, args=(20, 24))
            t6 = threading.Thread(target=a, args=(28, 32))
            t7 = threading.Thread(target=a, args=(36, 40))
            t8 = threading.Thread(target=a, args=(44, 48))
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()

        def show_id(video_id, root, r2):
            root2 = CTkScrollableFrame(root, width=1350, height=480, fg_color="#121212", scrollbar_fg_color="#121212",
                                       scrollbar_button_hover_color="#ffffff", scrollbar_button_color="#ffffff",
                                       border_color="#111111", corner_radius=0)
            root2.place(x=30, y=110)

            def root_des():
                root2.place(x=5000, y=5000)
                r2.place(x=5000, y=5000)

            but = CTkButton(root, text="close", command=root_des)
            but.place(x=0, y=0)
            # playlist = Playlist(playlist_from_channel_id(video_id))
            playlist = Playlist(video_id);

            def a(x, y):
                for index, i in enumerate(playlist.videos[x:y]):
                    try:
                        yt = YouTube("https://www.youtube.com/watch?v=" + i['id'])

                        thumbnail_url = i['thumbnails'][-1]['url']
                        thumbnail_path = f"temp.jpg"
                        urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                        # Open the image and get its dimensions
                        img = Image.open(thumbnail_path)
                        width, height = img.size

                        # Crop the image to make it square
                        new_width = min(width, height)
                        left = (width - new_width) // 2
                        right = width - (width - new_width) // 2
                        img = img.crop((left, 0, right, new_width))

                        # Resize the image to 140x140 pixels
                        img = img.resize((120, 120))

                        # Convert the image to ImageTk format
                        img = ImageTk.PhotoImage(img)
                        jkl = yt.title[0:20] + "\n" + yt.title[21:37]
                        if len(yt.title) >= 40:
                            jkl += "..."
                        tile1 = CTkButton(root2, text=jkl, image=img, compound="left", anchor='w', width=320,
                                          height=125, border_spacing=0,
                                          font=("CircularSp", 15, "bold"), border_width=0, fg_color="#121212",
                                          corner_radius=0,
                                          hover_color="#1a1a1a")
                        tile1.grid(row=x, column=index, padx=5, pady=5)

                        tile1.configure(command=lambda x="https://www.youtube.com/watch?v=" + i['id']: download_song(x))

                    except:
                        pass

            t1 = threading.Thread(target=a, args=(0, 4))
            t2 = threading.Thread(target=a, args=(4, 8))
            t3 = threading.Thread(target=a, args=(8, 12))
            t4 = threading.Thread(target=a, args=(12, 16))
            t5 = threading.Thread(target=a, args=(20, 24))
            t6 = threading.Thread(target=a, args=(28, 32))
            t7 = threading.Thread(target=a, args=(36, 40))
            t8 = threading.Thread(target=a, args=(44, 48))
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()

        def show_id1(video_id, root, r2):
            root2 = CTkScrollableFrame(root, width=1350, height=480, fg_color="#121212", scrollbar_fg_color="#121212",
                                       scrollbar_button_hover_color="#ffffff", scrollbar_button_color="#ffffff",
                                       border_color="#111111", corner_radius=0)
            root2.place(x=30, y=110)
            playlist = Playlist(video_id)

            def root_des():
                root2.place(x=5000, y=5000)
                r2.place(x=5000, y=5000)

            but = CTkButton(root, text="close", command=root_des)
            but.place(x=0, y=0)

            def a(x, y):
                for index, i in enumerate(playlist.videos[x:y]):
                    try:
                        yt = YouTube("https://www.youtube.com/watch?v=" + i['id'])

                        thumbnail_url = i['thumbnails'][-1]['url']
                        thumbnail_path = f"temp.jpg"
                        urllib.request.urlretrieve(thumbnail_url, thumbnail_path)
                        # Open the image and get its dimensions
                        img = Image.open(thumbnail_path)
                        width, height = img.size

                        # Crop the image to make it square
                        new_width = min(width, height)
                        left = (width - new_width) // 2
                        right = width - (width - new_width) // 2
                        img = img.crop((left, 0, right, new_width))

                        # Resize the image to 140x140 pixels
                        img = img.resize((120, 120))

                        # Convert the image to ImageTk format
                        img = ImageTk.PhotoImage(img)
                        tile1 = CTkButton(root2, text=yt.title[0:20], image=img, compound="left", anchor='w', width=320,
                                          height=125, border_spacing=0,
                                          font=("CircularSp", 18, "bold"), border_width=0, fg_color="#121212",
                                          corner_radius=0,
                                          hover_color="#1a1a1a")
                        tile1.grid(row=x, column=index, padx=5, pady=5)
                        tile1.configure(command=lambda x="https://www.youtube.com/watch?v=" + i['id']: download_song(x))

                    except:
                        pass

            t1 = threading.Thread(target=a, args=(0, 4))
            t2 = threading.Thread(target=a, args=(4, 8))
            t3 = threading.Thread(target=a, args=(8, 12))
            t4 = threading.Thread(target=a, args=(12, 16))
            t5 = threading.Thread(target=a, args=(20, 24))
            t6 = threading.Thread(target=a, args=(28, 32))
            t7 = threading.Thread(target=a, args=(36, 40))
            t8 = threading.Thread(target=a, args=(44, 48))
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()

        label1 = CTkFrame(app2, width=1420, height=600, fg_color="#111111")
        label1.place(x=0, y=0)
        CTkButton(label1, text="", corner_radius=50, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=70, border_width=1).place(x=10, y=5)
        CTkButton(label1, text="", corner_radius=15, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=500, border_width=1).place(x=10, y=100)

        search_entry3 = CTkEntry(label1, font=("CircularSp", 16, "bold"), placeholder_text="Search Songs",
                                 fg_color="#121212", bg_color="#121212", width=1360, height=50, corner_radius=50)
        search_entry3.place(x=30, y=15)
        enter = CTkButton(label1, text="Search", text_color="white", fg_color="#242424", hover_color="#282827",
                          bg_color="#121212", width=198, font=("CircularSp", 16, "bold"), height=42, corner_radius=50,
                          command=lambda r=label1, x="Song": search(x, r))
        enter.place(x=1185, y=18)

        label2 = CTkFrame(app2, width=1420, height=600, fg_color="#111111")
        label2.place(x=1600, y=50)
        CTkButton(label2, text="", corner_radius=50, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=70, border_width=1).place(x=10, y=5)
        CTkButton(label2, text="", corner_radius=15, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=500, border_width=1).place(x=10, y=100)

        search_entry = CTkEntry(label2, font=("CircularSp", 16, "bold"), placeholder_text="Search Artists",
                                fg_color="#121212", bg_color="#121212", width=1360, height=50, corner_radius=50)
        search_entry.place(x=30, y=15)
        enter = CTkButton(label2, text="Search", text_color="white", fg_color="#242424", hover_color="#282827",
                          bg_color="#121212", width=198, font=("CircularSp", 16, "bold"), height=42, corner_radius=50,
                          command=lambda r=label2, x="Artist": search(x, r))
        enter.place(x=1185, y=18)

        label3 = CTkFrame(app2, width=1420, height=600, fg_color="#111111")
        label3.place(x=3150, y=700)
        CTkButton(label3, text="", corner_radius=50, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=70, border_width=1).place(x=10, y=5)
        CTkButton(label3, text="", corner_radius=15, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=500, border_width=1).place(x=10, y=100)

        search_entry1 = CTkEntry(label3, font=("CircularSp", 16, "bold"), placeholder_text="Search Playlists",
                                 fg_color="#121212", bg_color="#121212", width=1360, height=50, corner_radius=50)
        search_entry1.place(x=30, y=15)
        ente1 = CTkButton(label3, text="Search", text_color="white", fg_color="#242424", hover_color="#282827",
                          bg_color="#121212", width=198, font=("CircularSp", 16, "bold"), height=42, corner_radius=50,
                          command=lambda r=label3, x="Playlist": search(x, r))
        ente1.place(x=1185, y=18)

        label4 = CTkFrame(app2, width=1420, height=600, fg_color="#111111")
        label4.place(x=4700, y=700)

        CTkButton(label4, text="", corner_radius=50, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=70, border_width=1).place(x=10, y=5)
        CTkButton(label4, text="", corner_radius=15, border_color="white", bg_color="#121212", fg_color="#121212",
                  hover_color="#121212", width=1400, height=500, border_width=1).place(x=10, y=100)

        search_entry2 = CTkEntry(label4, font=("CircularSp", 16, "bold"), placeholder_text="Search Albums",
                                 fg_color="#121212", bg_color="#121212", width=1360, height=50, corner_radius=50)
        search_entry2.place(x=30, y=15)
        ente1 = CTkButton(label4, text="Search", text_color="white", fg_color="#242424", hover_color="#282827",
                          bg_color="#121212", width=198, font=("CircularSp", 16, "bold"), height=42, corner_radius=50,
                          command=lambda r=label4, x="Album": search(x, r))
        ente1.place(x=1185, y=18)

        def segmented_button_callback(value):
            global pre
            l1 = label1
            l2 = label2
            l3 = label3
            l4 = label4
            if value == pre:
                pass
            elif pre == "Song" and value == "Artist":
                pre = value
                move_label_right(l1, l4, l3, l2)
                button2.configure(text="⚫Artist")
                button3.configure(text="◯Playlist")
                button4.configure(text="◯Album")
                button1.configure(text="◯Song")
            elif pre == "Song" and value == "Album":
                pre = value
                move_label_right(l1, l2, l3, l4)
                button4.configure(text="⚫Album")
                button2.configure(text="◯Artist")
                button3.configure(text="◯Playlist")
                button1.configure(text="◯Song")
            elif pre == "Song" and value == "Playlist":
                pre = value
                move_label_right(l1, l2, l4, l3)
                button3.configure(text="⚫Playlist")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
                button1.configure(text="◯Song")
            elif pre == "Artist" and value == "Song":
                pre = value
                move_label_left(l2, l4, l3, l1)
                button1.configure(text="⚫Song")
                button3.configure(text="◯Playlist")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
            elif pre == "Artist" and value == "Album":
                pre = value
                move_label_right(l1, l2, l3, l4)
                button4.configure(text="⚫Album")
                button3.configure(text="◯Playlist")
                button2.configure(text="◯Artist")
                button1.configure(text="◯Song")
            elif pre == "Artist" and value == "Playlist":
                pre = value
                move_label_right(l1, l2, l4, l3)
                button3.configure(text="⚫Playlist")
                button1.configure(text="◯Song")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
            elif pre == "Playlist" and value == "Song":
                pre = value
                move_label_left(l2, l4, l3, l1)
                button1.configure(text="⚫Song")
                button3.configure(text="◯Playlist")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
            elif pre == "Playlist" and value == "Artist":
                pre = value
                move_label_left(l1, l4, l3, l2)
                button2.configure(text="⚫Artist")
                button3.configure(text="◯Playlist")
                button1.configure(text="◯Song")
                button4.configure(text="◯Album")
            elif pre == "Playlist" and value == "Album":
                pre = value
                move_label_right(l1, l2, l3, l4)
                button4.configure(text="⚫Album")
                button3.configure(text="◯Playlist")
                button2.configure(text="◯Artist")
                button1.configure(text="◯Song")
            elif pre == "Album" and value == "Song":
                pre = value
                move_label_left(l2, l4, l3, l1)
                button1.configure(text="⚫Song")
                button3.configure(text="◯Playlist")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
            elif pre == "Album" and value == "Artist":
                pre = value
                move_label_left(l1, l4, l3, l2)
                button2.configure(text="⚫Artist")
                button1.configure(text="◯Song")
                button3.configure(text="◯Playlist")
                button4.configure(text="◯Album")
            elif pre == "Album" and value == "Playlist":
                pre = value
                move_label_left(l1, l2, l4, l3)
                button3.configure(text="⚫Playlist")
                button1.configure(text="◯Song")
                button2.configure(text="◯Artist")
                button4.configure(text="◯Album")
        global pre
        pre = "Song"

        buttons = ["Song", "Artist", "Playlist", "Album"]

        button1 = CTkButton(app2, fg_color="#111111", hover_color="#111111", text='⚫Song',
                            font=("CircularSp", 16, "bold"), width=0,
                            command=lambda name=buttons[0]: segmented_button_callback(name))
        button1.place(x=500, y=600)  # Place the buttons at appropriate positions
        button2 = CTkButton(app2, fg_color="#111111", hover_color="#111111", text='◯Artist',
                            font=("CircularSp", 16, "bold"), width=0,
                            command=lambda name=buttons[1]: segmented_button_callback(name))
        button2.place(x=600, y=600)  # Place the buttons at appropriate positions
        button3 = CTkButton(app2, fg_color="#111111", hover_color="#111111", text='◯Playlist',
                            font=("CircularSp", 16, "bold"), width=0,
                            command=lambda name=buttons[2]: segmented_button_callback(name))
        button3.place(x=700, y=600)  # Place the buttons at appropriate positions
        button4 = CTkButton(app2, fg_color="#111111", hover_color="#111111", text='◯Album',
                            font=("CircularSp", 16, "bold"), width=0,
                            command=lambda name=buttons[3]: segmented_button_callback(name))
        button4.place(x=800, y=600)
    on()

Search_but=HoverButton(ltop,text="Search",compound=LEFT,anchor='w',image=searchw_om,text_color="gray",fg_color="#121212",font=("CircularSp", 16, "bold"),hover_color="#121212",width = 300,height = 35,command=hero1)
Search_but.place(x=12,y=60)

def cr_pl():
    import threading
    from tkinter import filedialog, messagebox
    def asdasd():
        cur.execute("use spotify")
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS Playlists_data (Name VARCHAR(100), DESCRIPTION VARCHAR(200),IMG_PATH VARCHAR(1000))"
        )

        window = CTkFrame(app,width=1600,height=900,fg_color="black")
        window.place(x=0,y=0)
        pywinstyles.set_opacity(window, 0.5)
        playlist_create_window = CTkFrame(app,fg_color="#222222",height=400,width=520)
        playlist_create_window.place(x=600,y=100)
        def destroy1():
            window.destroy()
            playlist_create_window.destroy()
        close_but =CTkButton(playlist_create_window,text="×",fg_color="#222222",font=("CircularSp", 40),hover_color="#222222",corner_radius=0,width=40,command=destroy1)
        close_but.place(x=480,y=0)
        close_but.bind("<Enter>", lambda e, button=close_but: button.configure(text_color="red"))
        close_but.bind("<Leave>", lambda e, button=close_but: button.configure(text_color="white"))
        def button_click_event():

            global ima
            file_path = filedialog.askopenfilename(title="Select a file", filetypes=(
            ("Image files", "*.jpg"), ("Image files", "*.png"), ("All files", "*.*")))
            ima = Image.open(file_path)

            button = CTkButton(playlist_create_window, text="",
                               image=CTkImage(light_image=ima, dark_image=ima, size=(178, 178)), fg_color="#000000",
                               height=180, width=180,
                               command=button_click_event, font=("CircularSp", 18), hover_color="black", border_width=0,
                               corner_radius=0)
            button.place(x=25, y=70)

            # ima.save(f"playlist_images\\{playlist_name}.png")


        name_entry = CTkEntry(playlist_create_window, width=280, fg_color="grey", height=50,
                              placeholder_text="Name your Playlisst", placeholder_text_color="#000000",
                              font=("CircularSp", 18))
        name_entry.place(x=220, y=70)
        afs = "Add Description(optional*)"
        desc_entry = CTkEntry(playlist_create_window, width=280, fg_color="grey", height=120, placeholder_text=afs,
                              placeholder_text_color="#000000", font=("CircularSp", 18))
        desc_entry.place(x=220, y=130)

        def submit():
            name = name_entry.get().strip().replace(' ','_')
            desc = desc_entry.get().strip().replace(' ','_')
            try:
                # Check if the table already exists
                cur.execute(
                    f"SELECT Name FROM Playlists_data"
                )
                result = cur.fetchall()
                # Extract table names from the result tuples
                existing_tables = [row[0] for row in result]
                if name in existing_tables:
                    messagebox.showerror("DB ERROR", "Playlist already exists")
                else:
                    # Create the new playlist table
                    cur.execute(
                        "CREATE TABLE IF NOT EXISTS `{}` (Name VARCHAR(100), DURATION VARCHAR(10), FILE_PATH VARCHAR(200), IMG_PATH VARCHAR(200), Artist VARCHAR(100))".format(
                            name)
                    )
                    mycon.commit()
                    new_path = f"playlist_images/{name}.png"
                    ima.save(new_path)
                    # Insert the playlist data into Playlists_data table
                    cur.execute(
                        "INSERT INTO Playlists_data (Name, Description, IMG_Path) VALUES ('{}','{}','{}')".format(
                            name, desc, new_path))
                    mycon.commit()
                    kl()
                    cur.execute("USE SPOTIFY")
                    cur.execute("SELECT * FROM playlists_data")
                    da = cur.fetchall()
                    if len(da) == 0:
                        pass
                    else:
                        playlist_scroll_frame = CTkScrollableFrame(lmiddle1, fg_color="#121212",width=80, height=500)
                        playlist_scroll_frame.place(x=0, y=100)

                        for i in da:
                            im = CTkButton(playlist_scroll_frame, fg_color="#121212",hover_color="#FFFFFF",text="",image=CTkImage(light_image=Image.open(i[2]),dark_image=Image.open(i[2]),size=(60, 60)), anchor='w', compound=LEFT, width=80,height=50)
                            im.pack(pady=5)

            except :
                pass

        button = CTkButton(playlist_create_window, text="Select Image", fg_color="grey", height=180, width=180,
                           command=button_click_event, font=("CircularSp", 18))
        button.place(x=25, y=70)
        button1 = CTkButton(playlist_create_window, text="Create", fg_color="#FFFFFF", height=40, width=80,
                            corner_radius=500, command=submit, text_color="black", font=("CircularSp", 18))
        button1.place(x=400, y=260)

        def enter(event):
            button1.configure(width=100, height=45, font=("CircularSp", 20))
            button1.place(x=395, y=260)

        def leave(event):
            button1.configure(width=80, height=40, font=("CircularSp", 18))
            button1.place(x=400, y=260)

        button1.bind("<Enter>", enter)
        button1.bind("<Leave>", leave)
        CTkLabel(playlist_create_window,
                 text="By proceeding, you agree to give us access to the image you choose to upload.\n Please make sure you have the right to upload the image.\nAny Image provided is encrypted and no one else can access it except you.",
                 font=("CircularSp", 12, 'bold'), text_color="red").place(x=40, y=320)

    t = threading.Thread(target=asdasd,args=())
    t.start()

lmiddle = CTkFrame(app,width=320,height=570,fg_color='#121212')
lmiddle.place(x=5,y=125)
library = HoverButton(lmiddle,text="Your Library",compound=LEFT,anchor='w',image=library1,text_color="gray",fg_color="#121212",font=("CircularSp", 16, "bold"),hover_color="#121212",width = 100,height = 35)
library.place(x=15,y=10)
CTkLabel(lmiddle,text="",width=50,fg_color="#121212").place(x=210,y=5)
addp = HoverButton(lmiddle,text="➕",compound=LEFT,anchor='w',text_color="gray",fg_color="#121212",font=("CircularSp", 18),hover_color="#121000",width=40,corner_radius=200,command=cr_pl)
addp.place(x=220,y=13.5)
qe = HoverButton(lmiddle,text="➔",compound=LEFT,anchor='w',text_color="gray",fg_color="#121212",font=("CircularSp", 25),hover_color="#121000",width=40,corner_radius=200)
qe.place(x=270,y=10)

#create playlist:


# Add a label inside the frame
#create playlist:

def kl():
    try:
        cur.execute("USE SPOTIFY")
        cur.execute("SELECT * FROM playlists_data")
        da = cur.fetchall()
        if len(da)==0:
            create_playlist = CTkFrame(lmiddle, width=300, height=135, fg_color="#242424")
            create_playlist.place(x=5, y=65)
            info = CTkLabel(create_playlist, text="Create your first playlist", fg_color="#242424", text_color="white",
                            font=("CircularSp-Cyrl", 16, "bold"))
            info.place(x=20, y=13)
            info1 = CTkLabel(create_playlist, text="It's easy, we'll help you", fg_color="#242424", text_color="white",
                             font=("CircularSp-Cyrl", 13, "bold"))
            info1.place(x=22, y=41)
            cpb = HoverButton(create_playlist, text_color="Black", fg_color="white", text="Create playlist", width=125,
                              height=32, corner_radius=50, font=("CircularSp", 13, "bold"), command=cr_pl)
            cpb.place(x=20, y=85)
        else:
            playlist_scroll_frame = CTkScrollableFrame(lmiddle, width=300,fg_color="#121212", height=480)
            playlist_scroll_frame.place(x=5, y=70)

            def goback1(parent):
                ltop.place(x=5, y=5)
                lmiddle.place(x=5, y=125)

                opt.place(x=330, y=5)
                parent.place(x=5000, y=5000)
                global lmiddle1, ltop1
                FULL_frame()
                frontbut.configure(image=foren)

            def show_all_playlist(j):
                h = CTkFrame(app, width=1500, height=700, fg_color="#000000")

                create_image_frames2(h, j[0])
                collapse()
                short_frame()
                h.place(x=95, y=5)

                def gofor():
                    collapse()
                    short_frame()
                    h.place(x=95, y=5)

                home_but_s.configure(command=lambda: goback1(h))
                frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212",
                                     hover_color="#121212",
                                     command=gofor)
                frontbut.place(x=40, y=10)

            def delete_pla(play_name, l):
                menu = CTkLabel(app, text="", fg_color="#484848")
                menu.place(x=150, y=300)
                asd = CTkButton(menu, text="open", width=200, height=50, fg_color="Black", text_color="#FFFFFF",
                                command=lambda x=i: show_all_playlist(x))
                asd.grid(row=0, column=0)

                asd1 = CTkButton(menu, text=f"Delete {play_name[0]} ", width=200, height=50, fg_color="Black",
                                 text_color="#FFFFFF",
                                 command=lambda x=i: delete_row_from_playlist(x, l, 'playlists_data'))
                asd1.grid(row=1, column=0)

                def close(event):
                    menu.destroy()
                def close1(event):
                    menu.destroy()
                asd2 = CTkButton(menu, text="Close", width=200, height=50, fg_color="Black", text_color="#FFFFFF",
                                 )
                asd2.grid(row=3, column=0)
                asd2.bind("<Button-1>", close)
                asd.bind("<Button-1>", close)
                asd1.bind("<Button-1>", close1)
            for i in da:
                im = CTkButton(playlist_scroll_frame,text=i[0],fg_color="#121212",text_color="grey",command=lambda x=i:show_all_playlist(x),image=CTkImage(light_image=Image.open(i[2]),dark_image=Image.open(i[2]),size=(60,60)),anchor='w',compound=LEFT,width=300,height=50,font=("CircularSp", 18,"bold"))
                im.pack(pady=2)
                playlist_but1.append(im)
                # Use lambda to capture the current value of 'im'
                im.bind("<Enter>", lambda e, button=im: button.configure(fg_color="#FFFFFF",text_color="Black"))
                im.bind("<Leave>", lambda e, button=im: button.configure(fg_color="#121212",text_color="grey"))
                im.bind("<Button-3>", lambda event, arg=i, button=im: delete_pla(arg, button))



    except:
        create_playlist = CTkFrame(lmiddle, width=300, height=135, fg_color="#242424")
        create_playlist.place(x=5, y=65)
        info = CTkLabel(create_playlist, text="Create your first playlist", fg_color="#242424", text_color="white",
                        font=("CircularSp-Cyrl", 16, "bold"))
        info.place(x=20, y=13)
        info1 = CTkLabel(create_playlist, text="It's easy, we'll help you", fg_color="#242424", text_color="white",
                         font=("CircularSp-Cyrl", 13, "bold"))
        info1.place(x=22, y=41)
        cpb = HoverButton(create_playlist, text_color="Black", fg_color="white", text="Create playlist", width=125,
                          height=32, corner_radius=50, font=("CircularSp", 13, "bold"), command=cr_pl)
        cpb.place(x=20, y=85)
        podcasts1 = CTkFrame(lmiddle, width=300, height=135, fg_color="#242424")
        podcasts1.place(x=5, y=222)
        CTkLabel(podcasts1, text="Let's find some podcasts to follow", fg_color="#242424", text_color="white",
                 font=("CircularSp-Cyrl", 16, "bold")).place(x=20, y=13)
        CTkLabel(podcasts1, text="We we'll keep you updated on new episodes", fg_color="#242424", text_color="white",
                 font=("CircularSp-Cyrl", 13, "bold")).place(x=22, y=41)
        cpb1 = HoverButton(podcasts1, text_color="Black", fg_color="white", text="Browse Podcasts", width=125, height=32,
                           corner_radius=50, font=("CircularSp", 13, "bold"), )
        cpb1.place(x=20, y=85)
kl()
#options menu

opt = CTkFrame(app,width=1300,height=112,fg_color='#121212',corner_radius=0)
opt.place(x=330,y=5)



backbut = CTkButton(opt,image=backdis,compound=LEFT,anchor='w',text="",width=30,fg_color="#121212",hover_color="#121212")
backbut.place(x=0,y=10)
frontbut= CTkButton(opt,image=fordis,text="",width=30,fg_color="#121212",hover_color="#121212")
frontbut.place(x=40,y=10)
Prem = HoverButton(opt,text_color="Black",fg_color="white",text="MY Instagram",width=125,height=32,corner_radius=50,font=("CircularSp", 13,"bold"),command=open_insta)
Prem.place(x=750,y=10)
Prem = HoverButton(opt,text_color="white",image=down,fg_color="black",text="MY YouTube",width=125,height=32,corner_radius=50,font=("CircularSp", 13.5,"bold"),command=open_Youtube)
Prem.place(x=930,y=10)
notbut = HoverButton(opt,image=note,compound=TOP,anchor='s',text=" ",text_color="black",width=10,fg_color="#121212",hover_color="#121212")
notbut.place(x=1100,y=6)
'''
def selll():
    all.configure(text_color="black",hover_color="white",fg_color="white")
    music.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
    podcasts.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
def selll1():
    music.configure(text_color="black",hover_color="white",fg_color="white")
    all.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
    podcasts.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
def selll2():
    podcasts.configure(text_color="black",hover_color="white",fg_color="white")
    music.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
    all.configure(text_color="white", hover_color="#3a3a3a", fg_color="#2a2a2a")
all = CTkButton(opt,command=selll,text_color="black",hover_color="white",fg_color="white",text="All",height=35,width=20,corner_radius=50,font=("CircularSp", 15,"bold"),)
all.place(x=10,y=60)
music = CTkButton(opt,command=selll1,text_color="white",hover_color="#3a3a3a",fg_color="#2a2a2a",text="Music",height=35,width=20,corner_radius=50,font=("CircularSp", 15,"bold"),)
music.place(x=80,y=60)
podcasts = CTkButton(opt,command=selll2,text_color="white",hover_color="#3a3a3a",fg_color="#2a2a2a",text="Podcasts",height=35,width=20,corner_radius=50,font=("CircularSp", 15,"bold"),)
podcasts.place(x=175,y=60)


'''



#SAMLL FARAMA



def hero4():
    global k1
    se_ar_ch()
    k1 = CTkButton(ltop, text="", compound=LEFT, anchor='w', image=searchw_im, text_color="white",
                   fg_color="#121212", font=("CircularSp", 16, "bold"), hover_color="#121212", width=331,
                   height=35)
    k1.place(x=12, y=60)

    try:
        k.destroy()
    except:
        pass


global ltop1, lmiddle1
ltop1 = CTkFrame(app, width=80, height=112, fg_color='#121212')
ltop1.place(x=5, y=5000)
lmiddle1 = CTkFrame(app, width=80, height=570, fg_color='#121212')
lmiddle1.place(x=5, y=12500)


def on_hover_enter(event):
    home_but_s.configure(image=home_om)
def on_hover_leave(event):
    home_but_s.configure(image=home_im)
def on_hover_enter1(event):
    Search_but.configure(image=searchw_im)
def on_hover_leave1(event):
    Search_but.configure(image=searchw_om)
def collapse():
    ltop.place(x=5000, y=0)
    lmiddle.place(x=5000, y=7)
    opt.place(x=8100, y=2)
def short_frame():
    lmiddle1.place(x=5, y=125)
    ltop1.place(x=5, y=5)
def FULL_frame():
    ltop.place(x=5, y=5)
    lmiddle.place(x=5, y=125)
    lmiddle1.place(x=5, y=12500)
    ltop1.place(x=5, y=50000)
    opt.place(x=330, y=5)

home_but_s = HoverButton(ltop1, text="", compound=LEFT, anchor='w', image=home_im, text_color="gray",
                       fg_color="#121212", font=("CircularSp", 16, "bold"), hover_color="#121212", width=300,
                       height=35,command=FULL_frame)
home_but_s.place(x=12, y=12)
home_but_s.bind("<Enter>", on_hover_enter)
home_but_s.bind("<Leave>", on_hover_leave)

Search_but1 = HoverButton(ltop1, text="  ", compound=LEFT, anchor='w', image=searchw_om, text_color="gray",
                         fg_color="#121212", font=("CircularSp", 16, "bold"), hover_color="#121212", width=300,
                         height=35, command=hero4)
Search_but1.place(x=12, y=60)
Search_but1.bind("<Enter>", on_hover_enter1)
Search_but1.bind("<Leave>", on_hover_leave1)


def on_hover_enter12(event):
    library.configure(image=library2)


def on_hover_leave12(event):
    library.configure(image=library1)


library = HoverButton(lmiddle1, text="", compound=LEFT, anchor='w', image=library1,
                      text_color="gray", fg_color="#121212", font=("CircularSp", 16, "bold"),
                      hover_color="#121212", width=100, height=35)
library.place(x=15, y=10)
library.bind("<Enter>", on_hover_enter12)
library.bind("<Leave>", on_hover_leave12)
addp = HoverButton(lmiddle1, text="➕", compound=LEFT, anchor='w', text_color="gray", fg_color="#121212",
                   font=("CircularSp", 18), hover_color="#121000", width=40, corner_radius=200,command=cr_pl)
addp.place(x=5, y=60.5)
try:
    cur.execute("USE SPOTIFY")
    cur.execute("SELECT * FROM playlists_data")
    da = cur.fetchall()
    if len(da)==0:
        pass
    else:
        playlist_scroll_frame = CTkScrollableFrame(lmiddle1,fg_color="#121212",corner_radius=0, width=75, height=470)
        playlist_scroll_frame.place(x=0, y=100)


        def goback1(parent):
            ltop.place(x=5, y=5)
            lmiddle.place(x=5, y=125)

            opt.place(x=330, y=5)
            parent.place(x=5000, y=5000)
            global lmiddle1, ltop1
            FULL_frame()
            frontbut.configure(image=foren)


        def show_all_playlist(j):
            h = CTkFrame(app, width=1500, height=700, fg_color="#000000")

            create_image_frames2(h, j[0])
            collapse()
            short_frame()
            h.place(x=95, y=5)

            def gofor():
                collapse()
                short_frame()
                h.place(x=95, y=5)

            home_but_s.configure(command=lambda: goback1(h))
            frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212",
                                 hover_color="#121212",
                                 command=gofor)
            frontbut.place(x=40, y=10)
        def delete_pla(play_name,l):
            menu = CTkLabel(app,text="",fg_color="#484848")
            menu.place(x=100,y=300)
            asd = CTkButton(menu,text="open",width=200,height=50,fg_color="Black",text_color="#FFFFFF",command=lambda x=i:show_all_playlist(x))
            asd.grid(row=0,column=0)
            asd1 = CTkButton(menu, text=f"Delete {play_name[0]} ",width=200,height=50,fg_color="Black",text_color="#FFFFFF", command=lambda x=i: delete_row_from_playlist(x,l,'playlists_data'))
            asd1.grid(row=1,column=0)
            def close(event):
                menu.destroy()
            def close1(event):
                menu.destroy()
                fg=playlist_but2.index(l)
                playlist_but1[fg].destroy()
            asd2 = CTkButton(menu, text="Close", width=200,height=50,fg_color="Black",text_color="#FFFFFF")
            asd2.grid(row=3,column=0)
            asd2.bind("<Button-1>", close)
            asd.bind("<Button-1>", close)
            asd1.bind("<Button-1>", close1)

        for i in da:
            im = CTkButton(playlist_scroll_frame, text="", command=lambda x=i: show_all_playlist(x),
                           image=CTkImage(light_image=Image.open(i[2]), dark_image=Image.open(i[2]), size=(60, 60)),
                           fg_color="#121212", hover_color="#FFFFFF", anchor='w', compound=LEFT, width=50, height=50)
            im.pack(pady=5)
            playlist_but2.append(im)
            im.bind("<Button-3>", lambda event, arg=i, button=im: delete_pla(arg, button))
except:
    pass

#main frame
def artS():
    global firstrow
    firstrow = CTkScrollableFrame(app,width=1190,height=575,fg_color="#121212",corner_radius=0)
    firstrow.place(x=330,y=117)

    #firstrow = CTkFrame(mainF,width=1080,height=300,fg_color="#121212")
    #firstrow.pack()
    def goback1(parent):
        ltop.place(x=5, y=5)
        lmiddle.place(x=5, y=125)
        opt.place(x=330, y=5)
        parent.place(x=5000, y=5000)
        global lmiddle1, ltop1
        FULL_frame()
        frontbut.configure(image=foren)
    global but_list
    but_list=[]
    def d():
        global f5
        f5 = CTkFrame(firstrow, width=1200, fg_color="#121212", height=350)
        f5.pack()
        h = CTkFrame(app, width=1500, height=700, fg_color="#000000")

        def show_all_downloads():
            create_image_frames3(h, 'Downloads')
            collapse()
            short_frame()
            h.place(x=95, y=5)

            def gofor():
                collapse()
                short_frame()
                h.place(x=95, y=5)

            home_but_s.configure(command=lambda: goback1(h))
            frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                                 command=gofor)
            frontbut.place(x=40, y=10)
            did("Downloads")
            next()


        def show_downloads(k, l, i):

            alb1 = CTkImage(light_image=Image.open(i[3]), dark_image=Image.open(i[3]), size=(170, 170))
            tile = HoverButton(f5, text=i[0][0:20] + '\n~' + i[4], image=alb1, compound=TOP, height=280,
                               border_spacing=0,
                               font=("CircularSp", 17, "bold"), border_width=0, fg_color="#121212", corner_radius=15,
                               hover_color="#1a1a1a")
            tile.place(x=k, y=l)
            tile.configure(command=lambda path=i: replace_extension(path))
            but_list.append(tile)

        try:
            cur.execute("SELECT * FROM Downloads")
            data1 = cur.fetchall()
            data=[]
            for i in data1:
                data.append(i)

            for index, i in enumerate(data[-1:-6:-1]):
                k = 10 + int(index * 230)
                show_downloads(k, 50, i)
        except:
            pass
        textbutton = HoverButton(f5, text="Downloads", font=("CircularSp", 25, "bold"), fg_color="#121212",
                                 hover_color="#121212")
        textbutton.place(x=15, y=10)
        show_button1 = HoverButton(f5, text="Show All", text_color="grey", font=("CircularSp", 15, "bold"), anchor='e',
                                   fg_color="#121212", hover_color="#121212", command=show_all_downloads)
        show_button1.place(x=1050, y=10)
    try:
        d()
    except:
        pass
    f1 = CTkFrame(firstrow,width=1200,fg_color="#121212",height=350)
    f1.pack()
    def showall():
        def collasd():
            f1.configure(height=350)
            show_button.configure(text="Show All",command=showall)
        show_button.configure(text="Show Less",command=collasd)
        f1.configure(height=700)
    textbutton = HoverButton(f1,text="Try something else",font=("CircularSp", 25,"bold"),fg_color="#121212",hover_color="#121212")
    textbutton.place(x=15,y=10)
    show_button = HoverButton(f1,text="Show All",text_color="grey",font=("CircularSp", 15,"bold"),anchor='e',fg_color="#121212",hover_color="#121212",command=showall)
    show_button.place(x=1050,y=10)
    def p():
        f()
        # Path to the directory containing images
        image_dir = "Duncan_Laurence"
        global opt0
        opt0.place(x=95, y=5)
        def gofor():
            collapse()
            short_frame()
            opt0.place(x=95, y=5)
        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        did(image_dir)
        next()
    def p1():
        f11()
        # Path to the directory containing images
        image_dir = r"Alec_Benjamin"
        name = image_dir
        global opt1
        collapse()
        short_frame()


        opt1.place(x=95, y=5)
        home_but_s.configure(goback1)
        def gofor():
            collapse()
            short_frame()
            opt1.place(x=95, y=5)


        home_but_s.configure(command=lambda: goback1(opt1))
        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        did(image_dir)
        next()
    def p2():
        f22()
        # Path to the directory containing images
        image_dir = r"Billie_Eilish"
        name = image_dir
        global opt2
        collapse()
        short_frame()
        opt2.place(x=95, y=5)
        def gofor():
            collapse()
            short_frame()
            opt2.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt2))
        did(image_dir)
        next()
    def p3():
        f33()
        # Path to the directory containing images
        image_dir = r"JustinBieber"
        name = image_dir
        global opt3
        collapse()
        short_frame()
        opt3.place(x=95, y=5)
        def gofor():
            collapse()
            short_frame()
            opt3.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt3))
        did(image_dir)
        next()
    def p4():
        f44()
        # Path to the directory containing images
        image_dir = r"XXX_Tentacion"
        name = image_dir
        global opt4
        collapse()
        short_frame()
        opt4.place(x=95, y=5)
        def gofor():
            collapse()
            short_frame()
            opt4.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt4))
        did(image_dir)
        next()
    def p6():
        f66()
        # Path to the directory containing images
        image_dir = r"Ed_Sheeran"
        name = image_dir
        global opt6
        collapse()
        short_frame()
        opt6.place(x=95, y=5)

        def gofor():
            collapse()
            short_frame()
            opt6.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt6))
        did(image_dir)
        next()
    def p7():
        f77()
        # Path to the directory containing images
        image_dir = r"Arijit_Singh"
        name = image_dir
        global opt7
        collapse()

        short_frame()
        opt7.place(x=95, y=5)

        def gofor():
            collapse()
            short_frame()
            opt7.place(x=95, y=5)
        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt7))
        did(image_dir)
        next()
    def p8():
        f88()
        image_dir = r"Imagine_Dragons"
        name = image_dir
        # Path to the directory containing images

        global opt8
        collapse()
        short_frame()
        opt8.place(x=95, y=5)
        def gofor():
            collapse()
            short_frame()
            opt8.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt8))
        did(image_dir)
        next()
    def p9():
        f99()
        # Path to the directory containing images
        image_dir = r"Anuv_Jain"
        name = image_dir
        global opt9
        collapse()
        short_frame()
        opt9.place(x=95, y=5)

        def gofor():
            collapse()
            short_frame()
            opt9.place(x=95, y=5)

        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        home_but_s.configure(command=lambda: goback1(opt9))
        did(image_dir)
        next()
    def p10():
        f10()
        # Path to the directory containing images

        image_dir = r"Taylors_Swift"
        name = image_dir
        global opt10
        collapse()
        short_frame()
        opt10.place(x=95, y=5)

        def gofor():
            collapse()
            short_frame()
            opt10.place(x=95, y=5)


        home_but_s.configure(command=lambda: goback1(opt10))
        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)
        did(image_dir)
        next()
    teee = "Duncan Laurence"
    tile = HoverButton(f1,text=(teee[0:17]+"..." if len(teee) > 18 else teee ),image=alb1,compound="top",anchor='n',height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=12,hover_color="#1a1a1a",command=p)
    teee = "Alec Benjamin"
    tile1 = HoverButton(f1,text=(teee[0:17]+"..." if len(teee) > 18 else teee ),image=alb2,compound="top",anchor='n',height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a",command=p1)
    teee = "Billie Eilish"
    tile2 = HoverButton(f1,text=(teee[0:17]+"..." if len(teee) > 18 else teee ),image=alb3,compound="top",anchor='n',height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a",command=p2)
    teee = "Justin Beiber"
    tile3 = HoverButton(f1,text=(teee[0:17]+"..." if len(teee) > 18 else teee ),image=alb4,compound="top",anchor='n',height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a",command=p3)
    teee = "XXX Tentacion"
    tile4 = HoverButton(f1,text=(teee[0:17]+"..." if len(teee) > 18 else teee ),image=alb5,compound="top",anchor='n',height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a",command=p4)
    tile.place(x=10,y=50)
    tile1.place(x=240,y=50)
    tile2.place(x =470,y=50)
    tile3.place(x=700,y=50)
    tile4.place(x=930,y=50)



    teee = "Ed Sheeran"
    tile = HoverButton(f1, text=(teee[0:17] + "..." if len(teee) > 18 else teee), image=alb6, compound="top",
                       anchor='n', height=280, border_spacing=0, font=("CircularSp", 17, "bold"), border_width=0,
                       fg_color="#121212", corner_radius=12, hover_color="#1a1a1a", command=p6)
    teee = "Arijit Singh"
    tile1 = HoverButton(f1, text=(teee[0:17] + "..." if len(teee) > 18 else teee), image=alb9, compound="top",
                        anchor='n', height=280, border_spacing=0, font=("CircularSp", 17, "bold"), border_width=0,
                        fg_color="#121212", corner_radius=15, hover_color="#1a1a1a", command=p7)
    teee = "Imagine Dragons"
    tile2 = HoverButton(f1, text=(teee[0:17] + "..." if len(teee) > 18 else teee), image=alb8, compound="top",
                        anchor='n', height=280, border_spacing=0, font=("CircularSp", 17, "bold"), border_width=0,
                        fg_color="#121212", corner_radius=15, hover_color="#1a1a1a", command=p8)
    teee = "Anuv Jain"
    tile3 = HoverButton(f1, text=(teee[0:17] + "..." if len(teee) > 18 else teee), image=alb7, compound="top",
                        anchor='n', height=280, border_spacing=0, font=("CircularSp", 17, "bold"), border_width=0,
                        fg_color="#121212", corner_radius=15, hover_color="#1a1a1a", command=p9)
    teee = "Taylor Swift"
    tile4 = HoverButton(f1, text=(teee[0:17] + "..." if len(teee) > 18 else teee), image=alb10, compound="top",
                        anchor='n', height=280, border_spacing=0, font=("CircularSp", 17, "bold"), border_width=0,
                        fg_color="#121212", corner_radius=15, hover_color="#1a1a1a", command=p10)

    tile.place(x=10, y=380)
    tile1.place(x=240, y=380)
    tile2.place(x=470, y=380)
    tile3.place(x=700, y=380)
    tile4.place(x=930, y=380)



    global f2
    f2 = CTkFrame(firstrow,width=1200,fg_color="#121212",height=350)
    f2.pack()
    h = CTkFrame(app,width=1500,height=700,fg_color="#000000")

    def show_all_history():
        create_image_frames1(h,'History')
        collapse()
        short_frame()
        h.place(x=95, y=5)

        def gofor():
            collapse()
            short_frame()
            h.place(x=95, y=5)

        home_but_s.configure(command=lambda: goback1(h))
        frontbut = CTkButton(opt, image=fordis, text="", width=30, fg_color="#121212", hover_color="#121212",
                             command=gofor)
        frontbut.place(x=40, y=10)

    def show_history(k,l,i):
        image_dir = i[4]
        alb1=CTkImage(light_image=Image.open(i[3]),dark_image=Image.open(i[3]),size=(170,170))
        tile = HoverButton(f2, text=i[0][0:20]+'\n~'+image_dir[0:20], image=alb1, compound=TOP, height=280, border_spacing=0,
                           font=("CircularSp", 17, "bold"), border_width=0, fg_color="#121212", corner_radius=15,
                           hover_color="#1a1a1a")
        tile.place(x=k, y=l)

        tile.configure(command=lambda path=i: replace_extension(path))


    try:
        cur.execute("SELECT DISTINCT* FROM History ORDER BY TIME DESC LIMIT 5;")
        history = cur.fetchall()
        for index, i in enumerate(history):
            k=10+int(index*230)
            show_history(k,50,i)

    except:
        pass
    textbutton = HoverButton(f2,text="Recently Played",font=("CircularSp", 25,"bold"),fg_color="#121212",hover_color="#121212")
    textbutton.place(x=15,y=10)
    show_button1 = HoverButton(f2,text="Show All",text_color="grey",font=("CircularSp", 15,"bold"),anchor='e',fg_color="#121212",hover_color="#121212",command=show_all_history)
    show_button1.place(x=1050,y=10)
    """
    f3 = CTkFrame(firstrow,width=1200,fg_color="#121212",height=350)
    f3.pack()

    textbutton = HoverButton(f3,text="Featured Charts",font=("CircularSp", 25,"bold"),fg_color="#121212",hover_color="#121212")
    textbutton.place(x=15,y=10)
    textbutton = HoverButton(f3,text="Show All",text_color="grey",font=("CircularSp", 15,"bold"),anchor='e',fg_color="#121212",hover_color="#121212")
    textbutton.place(x=905,y=10)

    tile = HoverButton(f3,text="Album1\nalbum1\n\n",image=t1,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
    tile1 = HoverButton(f3,text="Album2\nalbum2\n\n",image=t2,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")

    tile2 = HoverButton(f3,text="Album3\nalbum3\n\n",image=t3,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")

    tile3 = HoverButton(f3,text="Album4\nalbum4\n\n",image=t4,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")

    tile4 = HoverButton(f3,text="Album5\nalbum5\n\n",image=t5,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
    tile.place(x=10, y=50)
    tile1.place(x=240, y=50)
    tile2.place(x=470, y=50)
    tile3.place(x=700, y=50)
    tile4.place(x=930, y=50)


    
    global more
    def create_more_items1():
        global more
        more.destroy()
        f4 = CTkLabel(firstrow,width=1200,fg_color="#121212",height=350)
        f4.pack()
        textbutton = HoverButton(f4,text="Spotify Podcasts",font=("CircularSp", 25,"bold"),fg_color="#121212",hover_color="#121212")
        textbutton.place(x=15,y=10)
        textbutton = HoverButton(f4,text="Show All",text_color="grey",font=("CircularSp", 15,"bold"),anchor='e',fg_color="#121212",hover_color="#121212")
        textbutton.place(x=905,y=10)

        tile = HoverButton(f4,text="Album1\nalbum1\n\n",image=soep1,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
        tile1 = HoverButton(f4,text="Album2\nalbum2\n\n",image=soep2,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
        tile2 = HoverButton(f4,text="Album3\nalbum3\n\n",image=soep3,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
        tile3 = HoverButton(f4,text="Album4\nalbum4\n\n",image=soep4,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
        tile4 = HoverButton(f4,text="Album5\nalbum5\n\n",image=soep5,compound=TOP,height=280,border_spacing=0,font=("CircularSp", 17,"bold"),border_width=0,fg_color="#121212",corner_radius=15,hover_color="#1a1a1a")
        tile.place(x=10, y=50)
        tile1.place(x=240, y=50)
        tile2.place(x=470, y=50)
        tile3.place(x=700, y=50)
        tile4.place(x=930, y=50)
        more = CTkButton(firstrow, text="SHOW MORE", height=40, width=200, font=("CircularSp", 17, "bold"),
                         command=create_more_items1)
        more.pack()
    more = CTkButton(firstrow,text="SHOW MORE",height=40,width=200,font=("CircularSp", 17,"bold"),command=create_more_items1)
    more.pack()
    """
artS()

global length_,curson, img_list, current_position_ms, music_paused, slider_manually_changed, update_loop_running,frames
frames=0
length_=0
slider_manually_changed = False
current_position_ms = 0
curson = 0
directory = dir
global files_list
files_list = []

def did(directory):
    global files_list, img_list
    files_list = []
    mixer.init()
    mixer.music.pause()
    cur.execute(f"select * from {directory}")
    data = cur.fetchall()

    for fil in data:
        files_list.append(fil)
    mixer.music.unpause()
    # Starting the mixer
_directory_="all_songs_data"
did(_directory_)

main = CTkLabel(app, text="0:0", font=("CircularSp", 15), text_color="#A7A7A7")
main.place(x=450, y=755)

file_path = files_list[curson][2]

# Loading the song
mixer.music.load(file_path)
music_paused = True

def seconds_to_minutes(seconds):
    minutes = seconds // 60
    seconds %= 60
    global tdur
    tdur = f"{math.ceil(minutes)}:{math.ceil(seconds)}"
    if int(f"{math.ceil(minutes)}") <10:
        a="0"+f"{math.ceil(minutes)}"
    else:
        a=f"{math.ceil(minutes)}"
    if int(f"{math.ceil(seconds)}") <10:
        b="0"+f"{math.ceil(seconds)}"
    else:
        b=f"{math.ceil(seconds)}"
    return f"{a}:{b}"

def songss():
    mixer.music.set_volume(0.7)
    tduration = CTkLabel(app, text=files_list[curson][1], font=("CircularSp", 15), text_color="#A7A7A7")
    tduration.place(x=1020, y=755)
    mixer.music.play()
    mixer.music.pause()
def next():
    global curson, update_loop_running
    # Stop the existing update loop
    update_loop_running = False
    curson += 1
    if curson != len(files_list):
        pass
    else:
        curson = 0
    file_path = files_list[curson][2]
    try:
        create_history(files_list[curson])
    except:
        pass
    mixer.music.load(file_path)
    try:
        global ui1, ui2, ui3, ui4, ui5, main_title_
        ui1.configure(image_path=files_list[curson - 2][3])
        ui2.configure(image_path=files_list[curson - 1][3])
        ui3.configure(image_path=files_list[curson][3])
        ui4.configure(image_path=files_list[curson + 1][3])
        ui5.configure(image_path=files_list[curson + 2][3])
        main_title_.configure(text=files_list[curson][0])
    except:
        pass
    tduration = CTkLabel(app, text=files_list[curson][1], font=("CircularSp", 15), text_color="#A7A7A7")
    tduration.place(x=1020, y=755)
    progress_slider.configure(from_=0, to=int(convert_minutes_to_seconds(files_list[curson][1])),
                              number_of_steps=int(convert_minutes_to_seconds(files_list[curson][1])))
    global length_
    length_=int(math.ceil(mixer.Sound(file_path).get_length()))
    progress_slider.set(0)
    titlename.configure(text=files_list[curson][0])
    title.configure(text="",
                    image=CTkImage(light_image=Image.open(files_list[curson][3]),
                                   dark_image=Image.open(files_list[curson][3]), size=(70, 70)), compound=LEFT,
                    anchor='e')
    artist.configure(text=files_list[curson][4])
    mixer.music.play()
    playbutton.destroy()
    global music_paused
    music_paused = False
    pausebutton = CTkButton(app, text="", image=pause1,hover_color="black", command=pause, fg_color="black", width=5)
    pausebutton.place(x=720, y=700)
    global current_position_ms
    current_position_ms = 0

def previous():
    global curson
    curson -= 1
    if curson != -len(files_list):
        pass
    else:
        curson = 0
    file_path = files_list[curson][2]
    mixer.music.load(file_path)
    try:
        create_history(files_list[curson])
    except:
        pass
    try:
        global ui1, ui2, ui3, ui4, ui5, main_title_
        ui1.configure(image_path=files_list[curson - 2][3])
        ui2.configure(image_path=files_list[curson - 1][3])
        ui3.configure(image_path=files_list[curson][3])
        ui4.configure(image_path=files_list[curson + 1][3])
        ui5.configure(image_path=files_list[curson + 2][3])
        main_title_.configure(text=files_list[curson][0])
    except:
        pass
    tduration = CTkLabel(app, text=files_list[curson][1], font=("CircularSp", 15), text_color="#A7A7A7")
    tduration.place(x=1020, y=755)
    progress_slider.configure(from_=0, to=int(convert_minutes_to_seconds(files_list[curson][1])),
                              number_of_steps=int(convert_minutes_to_seconds(files_list[curson][1])))
    progress_slider.set(0)
    global length_
    length_ = int(math.ceil(mixer.Sound(file_path).get_length()))
    titlename.configure(text=files_list[curson][0])
    title.configure(text="",
                    image=CTkImage(light_image=Image.open(files_list[curson][3]),
                                   dark_image=Image.open(files_list[curson][3]), size=(70, 70)), compound=LEFT,
                    anchor='e')
    artist.configure(text=files_list[curson][4])
    mixer.music.play()
    playbutton.destroy()
    global music_paused
    music_paused = False
    pausebutton = CTkButton(app, text="", image=pause1, command=pause, fg_color="black", width=5, hover_color="black")
    pausebutton.place(x=720, y=700)

    global current_position_ms
    current_position_ms = 0

def progress1(value):
    global slider_manually_changed
    global current_position_ms
    slider_manually_changed = True
    current_position_ms = value
    mixer.music.set_pos(current_position_ms)
    main.configure(text=seconds_to_minutes(current_position_ms))
    return value

def update_slider_position(event=None):
    # Get the current slider value
    current_position = progress_slider.get()
    # Update the music playback position (in seconds)
    mixer.music.set_pos(current_position)
    main.configure(text=seconds_to_minutes(current_position))
    # Reset the flag indicating that the slider position was updated manually
    global slider_manually_changed
    slider_manually_changed = False
    return False
    # Start the update loop

def update():
    global current_position_ms
    global slider_manually_changed,frames
    if slider_manually_changed and not music_paused:
        if length_==current_position_ms:
            next()
        current_position_ms = current_position_ms
        main.configure(text=seconds_to_minutes(current_position_ms))
        progress_slider.set(current_position_ms)

    if not slider_manually_changed and not music_paused:
        if length_==current_position_ms:
            next()
        current_position_ms += 1
        progress_slider.set(current_position_ms)
        main.configure(text=seconds_to_minutes(current_position_ms))

    app.after(1000, update)

update()
def progress(value):
    a = value
    mixer.music.set_volume(a)

  # Variable to store the current position of the music playback in milliseconds



def pause():
    global music_paused
    music_paused = True
    mixer.music.pause()

    pausebutton.destroy()
    playbutton = CTkButton(app, text="", fg_color="black",hover_color="#000000", image=play1, command=play,width=5)
    playbutton.place(x=720, y=700)

def play():
    global music_paused
    music_paused = False
    mixer.music.unpause()
    playbutton.destroy()
    pausebutton = CTkButton(app, text="", fg_color="black",hover_color="#000000", image=pause1, command=pause,width=5)
    pausebutton.place(x=720, y=700)


class ReflectionImage(CTkLabel):
    def __init__(self, master=None, image_path=None, **kwargs):
        super().__init__(master, **kwargs)
        self.image_path = image_path
        self.load_image()

    def load_image(self):
        if self.image_path:
            # Load the original image
            original_image = Image.open(self.image_path)

            # Create a blurred copy of the image
            blurred_image = original_image.copy()
            blurred_image = blurred_image.filter(
                ImageFilter.GaussianBlur(radius=10))  # Adjust the radius for the blur effect

            # Create a mask with a gradient opacity from the sides
            mask = Image.new('L', blurred_image.size, 0)
            draw = ImageDraw.Draw(mask)
            width, height = blurred_image.size
            gradient_width = 100  # Width of the gradient
            for x in range(gradient_width):
                opacity = int(255 * (x / gradient_width))
                draw.line([(x, 0), (x, height)], fill=opacity)
                draw.line([(width - x - 1, 0), (width - x - 1, height)], fill=opacity)

            # Apply the mask to the blurred image
            blurred_image.putalpha(mask)

            # Make the image corners round
            round_corners = Image.new('L', blurred_image.size, 0)
            draw = ImageDraw.Draw(round_corners)
            radius = 40  # Adjust the radius for the roundness of the corners
            draw.pieslice([(0, 0), (2 * radius, 2 * radius)], 180, 270, fill=255)
            draw.pieslice([(0, height - 2 * radius), (2 * radius, height)], 90, 180, fill=255)
            draw.pieslice([(width - 2 * radius, 0), (width, 2 * radius)], 270, 360, fill=255)
            draw.pieslice([(width - 2 * radius, height - 2 * radius), (width, height)], 0, 90, fill=255)
            blurred_image.putalpha(round_corners)

            # Create a shine effect around the corners at the top, left, and right sides
            shine_effect = Image.new('L', blurred_image.size, 0)
            draw = ImageDraw.Draw(shine_effect)
            draw.polygon([(0, 0), (width, 0), (width, 2 * radius), (0, 2 * radius)], fill=255)
            draw.polygon([(0, 0), (2 * radius, 0), (2 * radius, height), (0, height)], fill=255)
            draw.polygon([(width - 2 * radius, 0), (width, 0), (width, height), (width - 2 * radius, height)], fill=255)
            blurred_image.putalpha(shine_effect)

            # Create a reflection of the image
            reflection = blurred_image.copy().transpose(Image.FLIP_TOP_BOTTOM)
            # Crop the reflection to decrease its height
            reflection = reflection.crop((0, 0, reflection.size[0], reflection.size[1] // 2))
            # Create a gradient mask for the reflection with varying opacity
            reflection_mask = Image.new('L', reflection.size, 0)
            draw = ImageDraw.Draw(reflection_mask)
            for y in range(reflection.size[1]):  # Iterate over reflection height
                opacity = int(255 * ((reflection.size[1] - y) / reflection.size[1]) * 0.8)  # Varying opacity
                draw.line([(0, y), (reflection.size[0], y)], fill=opacity)

            # Apply the mask to the reflection
            reflection.putalpha(reflection_mask)

            # Create a blank image to composite the original image, reflection, and shadow
            composite_image = Image.new('RGBA', (width, height * 2), (255, 255, 255, 0))

            # Paste the original image onto the composite image
            composite_image.paste(original_image, (0, 0))

            # Paste the reflection below the original image
            composite_image.paste(reflection, (0, height))

            # Convert the composite image to a format compatible with Tkinter
            composite_image_tk = CTkImage(light_image=composite_image, dark_image=composite_image, size=(250, 600))

            # Display the composite image in the button
            self.configure(image=composite_image_tk)
            self.image = composite_image_tk

    def configure(self, image_path=None, **kwargs):
        if image_path:
            self.image_path = image_path
            self.load_image()
        super().configure(**kwargs)


next_button = CTkButton(app, text="", image=next2, fg_color="black",hover_color="black", command=next,width=5)
next_button.place(x=790, y=710)
previous_button = CTkButton(app, text="", image=previous2, fg_color="black",hover_color="black", command=previous,width=5)
previous_button.place(x=670, y=710)

volume_slider = CTkSlider(app, from_=0, to=1, command=progress,progress_color="white",button_hover_color="#ffffff",
                            button_color="white",corner_radius=1000,border_width=5.5)
volume_slider.place(x=1150, y=745)
volume_slider.set(0.7)
vf=CTkLabel(app,text="",image=CTkImage(light_image=Image.open("imgs/volume.png"),dark_image=Image.open("imgs/volume.png"),size=(40,40)))
vf.place(x=1100,y=730)

playbutton = CTkButton(app, text="", image=play1, fg_color="black", hover_color="black",command=play,width=5)

pausebutton = CTkButton(app, text="", image=pause1, fg_color="black",hover_color="black", command=pause,width=5)
playbutton.place(x=720, y=700)
progress_slider = CTkSlider(app,width=500, from_=0, to=int(math.ceil(mixer.Sound(file_path).get_length())),
                            number_of_steps=int(math.ceil(mixer.Sound(file_path).get_length())), command=progress1,progress_color="white",button_hover_color="#ffffff",
                            button_color="white",corner_radius=1000,border_width=5.5)
progress_slider.place(x=500, y=760)
length_=int(math.ceil(mixer.Sound(file_path).get_length()))
def on_enter(event):
    progress_slider.configure(progress_color="#FFFFFF")
def on_enterr(event):
    volume_slider.configure(progress_color="#FFFFFF")
    vf.configure(image=CTkImage(light_image=Image.open("imgs/volumeUp.png"), dark_image=Image.open("imgs/volumeUp.png"),
                                size=(40, 40)))
def on_leave(event):
    progress_slider.configure(progress_color="white")

def on_leavee(event):
    volume_slider.configure(progress_color="white")
    vf.configure(image=CTkImage(light_image=Image.open("imgs/volume.png"), dark_image=Image.open("imgs/volume.png"),
                                size=(40, 40)))

progress_slider.bind("<Enter>", on_enter)
progress_slider.bind("<Leave>", on_leave)

volume_slider.bind("<Button-1>", on_enterr)
volume_slider.bind("<ButtonRelease-1>", on_leavee)

progress_slider.set(0)
progress_slider.bind("<ButtonRelease-1>", update_slider_position)
title = CTkLabel(app, text=files_list[curson][0])

titlename = CTkButton(app,fg_color="#000000",font=("CircularSp", 17,"bold"),anchor="w",hover_color="#000000",text_color="#ffffff",corner_radius=0,border_color="#121212",text=files_list[curson][0])
titlename.place(x=100,y=720)
title.configure(text="", image=CTkImage(light_image=Image.open(files_list[curson][3]),
                    dark_image=Image.open(files_list[curson][3]), size=(70, 70)), compound=LEFT, anchor='e')
title.place(x=10, y=710)
artist = CTkButton(app, text=files_list[curson][4],hover_color="#000000", fg_color="#000000",font=("CircularSp", 14,"bold"),anchor="w",text_color="#A7A7A7",corner_radius=0,border_color="#121212")
artist.place(x=100, y=750)
artist.configure(text=files_list[curson][4])
def on_enter(event):
    title.configure(font=("CircularSp", 16, "bold", "underline"))
def on_leave(event):
    title.configure(font=("CircularSp",16, "bold"))

title.bind("<Enter>", on_enter)
title.bind("<Leave>", on_leave)
def on_enter1(event):
    artist.configure(font=("CircularSp", 14, "bold", "underline"))

def on_leave2(event):
    artist.configure(font=("CircularSp",14, "bold"))

artist.bind("<Enter>", on_enter1)
artist.bind("<Leave>", on_leave2)
def on_enter11(event):
    titlename.configure(font=("CircularSp", 17, "bold", "underline"))

def on_leave22(event):
    titlename.configure(font=("CircularSp",17, "bold"))

titlename.bind("<Enter>", on_enter11)
titlename.bind("<Leave>", on_leave22)

songss()



# Start the update loop
def newsongss(path):
    global frames
    global curson
    frames+=1
    for index,i in enumerate(files_list):
        if i==path:
            global curson
            curson=index
            break

    mixer.music.load(path[2])
    try:
        create_history(files_list[curson])
    except:
        pass
    try:
        global ui1, ui2, ui3, ui4, ui5, main_title_

        ui1.configure(image_path=files_list[curson - 2][3])
        ui2.configure(image_path=files_list[curson - 1][3])
        ui3.configure(image_path=files_list[curson][3])
        ui4.configure(image_path=files_list[curson + 1][3])
        ui5.configure(image_path=files_list[curson + 2][3])
        main_title_.configure(text=files_list[curson][0])
    except:
        pass
    tduration = CTkLabel(app, text=path[1], font=("CircularSp", 15), text_color="#A7A7A7")
    tduration.place(x=1020, y=755)
    global music_paused
    music_paused = False
    mixer.music.play()
    playbutton.destroy()
    main.configure(text="00:00")
    progress_slider.configure(from_=0,to=convert_minutes_to_seconds(path[1]),number_of_steps=convert_minutes_to_seconds(path[1]))
    global length_
    length_ = int(math.ceil(convert_minutes_to_seconds(path[1])))
    progress_slider.set(0)
    pausebutton = CTkButton(app, text="", image=pause1, command=pause, fg_color="black", width=5, hover_color="black")
    pausebutton.place(x=720, y=700)
    global current_position_ms
    current_position_ms = 0

def replace_extension(path):
    ima1 = CTkImage(light_image=Image.open(f"{path[3]}"), dark_image=Image.open(f"{path[3]}"),
                    size=(70, 70))

    titlename.configure(text=path[0])
    title.configure(text="",
                    image=ima1, compound=LEFT,
                    anchor='w')
    artist.configure(text=path[4])

    newsongss(path)
    return path


global create_image_frames
def create_image_frames(parent, image_dir):
    cur.execute(f"select * from {image_dir}")
    data = cur.fetchall()

    scrollable_frame = CTkScrollableFrame(parent, width=520, height=580, fg_color='#000000',bg_color="#000000",scrollbar_fg_color="#000000",border_color="#000000",scrollbar_button_color="#000000",scrollbar_button_hover_color="white")
    scrollable_frame.place(x=900, y=80)

    #pywinstyles.set_opacity(scrollable_frame,0.5)
    def goback():
        ltop.place(x=5, y=5)
        lmiddle.place(x=5, y=125)
        FULL_frame()
        opt.place(x=330, y=5)
        parent.place(x=5000,y=5000)
        global lmiddle1,ltop1
        frontbut.configure(image=foren)

    class HoverButton1(CTkButton):

        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.default_text = kwargs.get("text", "")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.default_text = self.cget("text")
            self.configure(text="▶️",width=5)

        def on_leave(self, event):
            self.configure(text=self.default_text)

    global curson
    curson = 0

    # Iterate over image paths and create frames

    # Dictionary to store child widgets for each HoverButton2 instanc

    # Update HoverButton2 class to use the child_widgets dictionary
    class HoverButton2(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.child_widgets = []

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):

            for widget in self.child_widgets:
                widget.configure(fg_color="#282828",bg_color = "#282828")


        def on_leave(self, event):
            for widget in self.child_widgets:
                widget.configure(fg_color="#000000",bg_color = "#000000")


    optk = CTkFrame(parent, width=1500, height=80, fg_color="#000000", corner_radius=0)
    Prem = HoverButton(parent, text_color="Black", fg_color="white", text="MY Instagram", width=125,bg_color="black",
                       height=32, corner_radius=50, font=("CircularSp", 13, "bold"), command=open_insta)
    backbut = CTkButton(parent, image=backen, compound=LEFT, corner_radius=50,anchor='w',hover_color="#000000", text="", width=5, fg_color="#000000",command=goback)
    Prem1 = HoverButton(parent, text_color="white", image=down, fg_color="black", text="MY YouTube", width=125,bg_color="#000000",
                        height=32, corner_radius=50, font=("CircularSp", 13.5, "bold"),command=open_Youtube )

    notbut = HoverButton(parent, image=note, text=" ", text_color="black",height=0, width=10,bg_color="#000000",
                         fg_color="#000000", hover_color="#000000")
    notbut.configure(fg_color="#000000", bg_color="#000000", hover_color="#000000")
    backbut.place(x=0, y=10)
    Prem.place(x=950, y=10)
    Prem1.place(x=1150, y=10)
    notbut.place(x=1350, y=10)

    class HoverButton3(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold,"underline"))


        def on_leave(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp",font_size , fbold))

    nb = 0
    global ui1,ui2,ui3,ui4,ui5,main_title_
    ui1 = ReflectionImage(parent,image_path=data[-2][3],text="")
    ui5 = ReflectionImage(parent, image_path=data[2][3],text="")
    ui2 = ReflectionImage(parent, image_path=data[-1][3],text="")
    ui4 = ReflectionImage(parent, image_path=data[1][3],text="")
    ui3 = ReflectionImage(parent, image_path=data[0][3],text="")
    main_title_=CTkLabel(parent,width=880,fg_color="#000000",text=data[0][0],font=("CircularSp", 30, "bold"))
    ui1.place(x=50,y=50)
    ui5.place(x=650, y=50)
    ui2.place(x=200,y=100)
    ui4.place(x=500,y=100)
    ui3.place(x=350,y=200)
    main_title_.place(x=20,y=650)

    def enter_playlist(song_tuple):
        bh = CTkFrame(app,fg_color="#000000",width=1600,height=900)
        bh.place(x=0,y=0)
        ask = CTkFrame(app)
        ask.place(x=900,y=200)
        pywinstyles.set_opacity(bh,0.5)
        cur.execute("SELECT NAME FROM playlists_data")
        option_list=[]
        choices = cur.fetchall()
        for h in choices:
            option_list.append(h[0].replace("_"," "))

        global choice
        def optionmenu_callback(choice):

            global table
            table=choice.replace(" ","_")

        optionmenu = CTkOptionMenu(ask, values=option_list,
                                                 command=optionmenu_callback)
        optionmenu.pack()
        def vbn():
            global table

            cur.execute("INSERT INTO {} VALUES {}".format(table, song_tuple))

            mycon.commit()

            bh.destroy()
            ask.destroy()
        select_vut = CTkButton(ask,text="Select",command=vbn)
        select_vut.pack()
    # Iterate over image paths and create frames
    for index,i in enumerate(data):
        try:
            index-=nb
            ine = HoverButton2(scrollable_frame, text="", fg_color="#000000", hover_color="#282828", width=1420, height=80)
            title_button = HoverButton3(ine, text=i[0][0:40],
                                     font=("CircularSp", 20,"normal"),anchor="w",
                                     fg_color="#000000",corner_radius=0,border_color="#000000",hover_color="#000000")
            button1 = HoverButton3(ine, text=i[4],hover_color="#000000", fg_color="#000000",font=("CircularSp", 14,"bold"),anchor="w",text_color="#FFFFFF",corner_radius=10,border_color="#000000")

            button2 = HoverButton1(ine, text=str(index + 1), width=5, height=20,corner_radius=10, border_width=0,border_spacing=0,hover_color="#000000", fg_color="#000000",
                                   font=("CircularSp", 16, "bold"),border_color="#000000")
            button3 = HoverButton(ine, text="",image=adde,width=20, height=20,corner_radius=10,border_width=0,border_spacing=0, hover_color="#000000", fg_color="#000000",
                                   font=("CircularSp", 16, "bold"),border_color="#000000",command=lambda x=i: enter_playlist(x))
            label = HoverButton3(ine, text=i[1],font=("CircularSp", 16, "bold"), fg_color="#000000",corner_radius=0,hover_color="#000000")
            button4 = HoverButton(ine, text="🗑️", width=20, height=20, corner_radius=10, border_width=0,
                                  border_spacing=0, hover_color="#000000", fg_color="#000000",
                                  font=("CircularSp", 16, "bold"), border_color="#000000",
                                  command=lambda x=i, y=ine: delete_row_from_all_tables(x, y))
            ine.child_widgets.append(button4)
            button4.place(x=350,
                          y=40)
            # Store child widgets in the dictionary
            ine.child_widgets.append(label),ine.child_widgets.append(title_button),ine.child_widgets.append(button2),ine.child_widgets.append(button3),ine.child_widgets.append(button1)
            ine.pack()
            title_button.place(x=50, y=10),button1.place(x=50, y=40),button2.place(x=0, y=25),button3.place(x=400, y=40),label.place(x=400, y=10)

            title_button.configure(command=lambda path=i: replace_extension(path))
            button2.configure(command=lambda path=i: replace_extension(path))
        except:
            nb+=1
            pass


def create_image_frames1(parent, image_dir):
    cur.execute(f"SELECT * FROM {image_dir} ORDER BY TIME DESC")
    data = cur.fetchall()
    ine = CTkLabel(parent,font=("CircularSp", 30, "bold"), text=f"{image_dir}",
                    fg_color="#111111", text_color="#777777",width=420,
                   height=40)
    ine.place(x=300, y=20)
    ine = CTkLabel(parent, text="",image=CTkImage(light_image=Image.open('imgs/#.png'),dark_image=Image.open('imgs/#.png'),size=(1420,80)), fg_color="#FFFFFF", width=1420,
                   height=40)
    ine.place(x=10, y=60)

    scrollable_frame = CTkScrollableFrame(parent, width=1400, height=580, fg_color='#111111', bg_color="#111111",
                                        border_color="#111111",
                                          scrollbar_button_color="#FFFFFF", scrollbar_button_hover_color="white")
    scrollable_frame.place(x=10, y=120)

    # pywinstyles.set_opacity(scrollable_frame,0.5)
    def goback():
        ltop.place(x=5, y=5)
        lmiddle.place(x=5, y=125)
        FULL_frame()
        opt.place(x=330, y=5)
        parent.place(x=5000, y=5000)
        global lmiddle1, ltop1
        frontbut.configure(image=foren)

    class HoverButton1(CTkButton):

        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.default_text = kwargs.get("text", "")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.default_text = self.cget("text")
            self.configure(text="▶️", width=5)

        def on_leave(self, event):
            self.configure(text=self.default_text)

    global curson
    curson = 0

    # Iterate over image paths and create frames

    # Dictionary to store child widgets for each HoverButton2 instanc

    # Update HoverButton2 class to use the child_widgets dictionary
    class HoverButton2(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.child_widgets = []

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):

            for widget in self.child_widgets:
                widget.configure(fg_color="#282828", bg_color="#282828")

        def on_leave(self, event):
            for widget in self.child_widgets:
                widget.configure(fg_color="#111111", bg_color="#111111")

    optk = CTkFrame(parent, width=1500, height=80, fg_color="#111111", corner_radius=0)
    Prem = HoverButton(parent, text_color="Black", fg_color="white", text="MY Instagram", width=125,
                       bg_color="#111111",
                       height=32, corner_radius=50, font=("CircularSp", 13, "bold"), command=open_insta)
    backbut = CTkButton(parent, image=backen, compound=LEFT, corner_radius=50, anchor='w', hover_color="#111111",
                        text="", width=5, fg_color="#111111", command=goback)
    Prem1 = HoverButton(parent, text_color="white", image=down, fg_color="black", text="MY YouTube", width=125,
                        bg_color="#111111",
                        height=32, corner_radius=50, font=("CircularSp", 13.5, "bold"),command=open_Youtube )

    notbut = HoverButton(parent, image=note, text=" ", text_color="black", height=0, width=10, bg_color="#111111",
                         fg_color="#111111", hover_color="#111111")
    backbut.place(x=0, y=10)
    Prem.place(x=950, y=10)
    Prem1.place(x=1150, y=10)
    notbut.place(x=1350, y=10)

    class HoverButton3(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold, "underline"))

        def on_leave(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold))

    nb = 0

    # Iterate over image paths and create frames
    for index, i in enumerate(data):
        try:
            index -= nb
            ine = HoverButton2(scrollable_frame, text="", fg_color="#111111", hover_color="#282828", width=1420,
                               height=80)

            title_button = HoverButton3(ine, text=i[0],
                                        font=("CircularSp", 20, "normal"), anchor="w",
                                        fg_color="#111111", corner_radius=0, border_color="#111111",
                                        hover_color="#111111",text_color="#A5C9FF")
            artist_name = HoverButton3(ine, text=i[4], hover_color="#111111",
                                   fg_color="#111111", font=("CircularSp", 14, "bold"), anchor="w",
                                   text_color="#A5FFC9", corner_radius=10, border_color="#111111")

            button2 = HoverButton1(ine, text=str(index + 1), width=5, height=20, corner_radius=10, border_width=0,
                                   border_spacing=0, hover_color="#111111", fg_color="#111111",
                                   font=("CircularSp", 16, "bold"), border_color="#000000")
            button3 = HoverButton(ine, text="", image=adde, width=20, height=20, corner_radius=10, border_width=0,
                                  border_spacing=0, hover_color="#111111", fg_color="#111111",
                                  font=("CircularSp", 16, "bold"), border_color="#111111")
            label = HoverButton3(ine, text=i[1], font=("CircularSp", 16, "bold"), fg_color="#111111", corner_radius=0,
                                 hover_color="#111111")
            label2 = HoverButton3(ine, text=i[5], font=("CircularSp", 16, "bold"), fg_color="#111111", corner_radius=0,
                                 hover_color="#111111")

            # Store child widgets in the dictionary
            ine.child_widgets.append(label), ine.child_widgets.append(title_button), ine.child_widgets.append(
                button2), ine.child_widgets.append(button3), ine.child_widgets.append(artist_name),ine.child_widgets.append(label2)
            ine.pack()
            title_button.place(x=150, y=10), artist_name.place(x=150, y=40), button2.place(x=20, y=25),  label.place(
                x=810, y=10),label2.place(x=1190,y=10),button3.place(x=890,y=10)


            title_button.configure(command=lambda path=i: replace_extension(path))
            button2.configure(command=lambda path=i: replace_extension(path))
        except:
            nb += 1
            pass
def create_image_frames2(parent, image_dir):
    cur.execute(f"SELECT * FROM {image_dir} ")
    data1=[]

    data = cur.fetchall()

    for i in data:
        if i not in data1:
            data1.append(i)
    data=data1
    ine = CTkLabel(parent,font=("CircularSp", 30, "bold"), text=f"{image_dir}",
                    fg_color="#000000", text_color="#FFFFFF",width=420,
                   height=40)
    ine.place(x=300, y=20)
    ine = CTkLabel(parent, text="",image=CTkImage(light_image=Image.open('imgs/#.png'),dark_image=Image.open('imgs/#.png'),size=(1820,80)), fg_color="#FFFFFF", width=1420,
                   height=40)
    ine.place(x=10, y=60)

    scrollable_frame = CTkScrollableFrame(parent, width=1400, height=580, fg_color='#000000', bg_color="#000000",
                                        border_color="#000000",
                                          scrollbar_button_color="#FFFFFF", scrollbar_button_hover_color="white")
    scrollable_frame.place(x=10, y=120)

    # pywinstyles.set_opacity(scrollable_frame,0.5)
    def goback():
        ltop.place(x=5, y=5)
        lmiddle.place(x=5, y=125)
        FULL_frame()
        opt.place(x=330, y=5)
        parent.place(x=5000, y=5000)
        global lmiddle1, ltop1
        frontbut.configure(image=foren)

    class HoverButton1(CTkButton):

        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.default_text = kwargs.get("text", "")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.default_text = self.cget("text")
            self.configure(text="▶️", width=5)

        def on_leave(self, event):
            self.configure(text=self.default_text)

    global curson
    curson = 0

    # Iterate over image paths and create frames

    # Dictionary to store child widgets for each HoverButton2 instanc

    # Update HoverButton2 class to use the child_widgets dictionary
    class HoverButton2(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.child_widgets = []

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):

            for widget in self.child_widgets:
                widget.configure(fg_color="#282828", bg_color="#282828")

        def on_leave(self, event):
            for widget in self.child_widgets:
                widget.configure(fg_color="#000000", bg_color="#000000")

    optk = CTkFrame(parent, width=1500, height=80, fg_color="#000000", corner_radius=0)
    Prem = HoverButton(parent, text_color="Black", fg_color="white", text="MY Instagram", width=125,
                       bg_color="black",
                       height=32, corner_radius=50, font=("CircularSp", 13, "bold"),command=open_insta )
    backbut = CTkButton(parent, image=backen, compound=LEFT, corner_radius=50, anchor='w', hover_color="#000000",
                        text="", width=5, fg_color="#000000", command=goback)
    Prem1 = HoverButton(parent, text_color="white", image=down, fg_color="black", text="MY YouTube", width=125,
                        bg_color="#000000",
                        height=32, corner_radius=50, font=("CircularSp", 13.5, "bold"),command=open_Youtube )

    notbut = HoverButton(parent, image=note, text=" ", text_color="black", height=0, width=10, bg_color="#000000",
                         fg_color="#000000", hover_color="#000000")
    notbut.configure(fg_color="#000000", bg_color="#000000", hover_color="#000000")
    backbut.place(x=0, y=10)
    Prem.place(x=950, y=10)
    Prem1.place(x=1150, y=10)
    notbut.place(x=1350, y=10)

    class HoverButton3(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold, "underline"))

        def on_leave(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold))

    nb = 0

    # Iterate over image paths and create frames
    for index, i in enumerate(data):
        try:
            index -= nb
            ine = HoverButton2(scrollable_frame, text="", fg_color="#000000", hover_color="#282828", width=1420,
                               height=80)
            title_button = HoverButton3(ine, text=i[0],
                                        font=("CircularSp", 20, "normal"), anchor="w",
                                        fg_color="#000000", corner_radius=0, border_color="#000000",
                                        hover_color="#000000")
            artist_name = HoverButton3(ine, text=i[4], hover_color="#000000",
                                   fg_color="#000000", font=("CircularSp", 14, "bold"), anchor="w",
                                   text_color="#FFFFFF", corner_radius=10, border_color="#000000")

            button2 = HoverButton1(ine, text=str(index + 1), width=5, height=20, corner_radius=10, border_width=0,
                                   border_spacing=0, hover_color="#000000", fg_color="#000000",
                                   font=("CircularSp", 16, "bold"), border_color="#000000")

            label = HoverButton3(ine, text=i[1], font=("CircularSp", 16, "bold"), fg_color="#000000", corner_radius=0,
                                 hover_color="#000000")

            # Store child widgets in the dictionary
            ine.child_widgets.append(label), ine.child_widgets.append(title_button), ine.child_widgets.append(
                button2), ine.child_widgets.append(artist_name)
            ine.pack()
            title_button.place(x=180, y=10), artist_name.place(x=180, y=40), button2.place(x=20, y=25),  label.place(
                x=1050, y=10)


            title_button.configure(command=lambda path=i: replace_extension(path))
            button2.configure(command=lambda path=i: replace_extension(path))
        except:
            nb += 1
            pass
def create_image_frames3(parent, image_dir):
    cur.execute(f"select * from {image_dir}")
    data = cur.fetchall()

    scrollable_frame = CTkScrollableFrame(parent, width=520, height=580, fg_color='#000000', bg_color="#000000",
                                          scrollbar_fg_color="#000000", border_color="#000000",
                                          scrollbar_button_color="#000000", scrollbar_button_hover_color="white")
    scrollable_frame.place(x=900, y=80)

    # pywinstyles.set_opacity(scrollable_frame,0.5)
    def goback():
        ltop.place(x=5, y=5)
        lmiddle.place(x=5, y=125)
        FULL_frame()
        opt.place(x=330, y=5)
        parent.place(x=5000, y=5000)
        global lmiddle1, ltop1
        frontbut.configure(image=foren)

    class HoverButton1(CTkButton):

        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.default_text = kwargs.get("text", "")
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            self.default_text = self.cget("text")
            self.configure(text="▶️", width=5)

        def on_leave(self, event):
            self.configure(text=self.default_text)

    global curson
    curson = 0

    # Iterate over image paths and create frames

    # Dictionary to store child widgets for each HoverButton2 instanc

    # Update HoverButton2 class to use the child_widgets dictionary
    class HoverButton2(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)
            self.child_widgets = []

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):

            for widget in self.child_widgets:
                widget.configure(fg_color="#282828", bg_color="#282828")

        def on_leave(self, event):
            for widget in self.child_widgets:
                widget.configure(fg_color="#000000", bg_color="#000000")

    optk = CTkFrame(parent, width=1500, height=80, fg_color="#000000", corner_radius=0)
    Prem = HoverButton(parent, text_color="Black", fg_color="white", text="MY Instagram", width=125,
                       bg_color="black",
                       height=32, corner_radius=50, font=("CircularSp", 13, "bold"),command=open_insta )
    backbut = CTkButton(parent, image=backen, compound=LEFT, corner_radius=50, anchor='w', hover_color="#000000",
                        text="", width=5, fg_color="#000000", command=goback)
    Prem1 = HoverButton(parent, text_color="white", image=down, fg_color="black", text="MY YouTube", width=125,
                        bg_color="#000000",
                        height=32, corner_radius=50, font=("CircularSp", 13.5, "bold"), command=open_Youtube)

    notbut = HoverButton(parent, image=note, text=" ", text_color="black", height=0, width=10, bg_color="#000000",
                         fg_color="#000000", hover_color="#000000")
    notbut.configure(fg_color="#000000", bg_color="#000000", hover_color="#000000")
    backbut.place(x=0, y=10)
    Prem.place(x=950, y=10)
    Prem1.place(x=1150, y=10)
    notbut.place(x=1350, y=10)

    class HoverButton3(CTkButton):
        def __init__(self, master=None, **kwargs):
            CTkButton.__init__(self, master, **kwargs)

            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold, "underline"))

        def on_leave(self, event):
            font_size = self.cget("font")[1]
            fbold = self.cget("font")[2]
            self.configure(font=("CircularSp", font_size, fbold))

    nb = 0
    global ui1, ui2, ui3, ui4, ui5, main_title_
    ui1 = ReflectionImage(parent, image_path=data[-2][3], text="")
    ui5 = ReflectionImage(parent, image_path=data[2][3], text="")
    ui2 = ReflectionImage(parent, image_path=data[-1][3], text="")
    ui4 = ReflectionImage(parent, image_path=data[1][3], text="")
    ui3 = ReflectionImage(parent, image_path=data[0][3], text="")
    main_title_ = CTkLabel(parent, width=880, fg_color="#000000", text=data[0][0], font=("CircularSp", 30, "bold"))
    ui1.place(x=50, y=50)
    ui5.place(x=650, y=50)
    ui2.place(x=200, y=100)
    ui4.place(x=500, y=100)
    ui3.place(x=350, y=200)
    main_title_.place(x=20, y=650)

    def enter_playlist(song_tuple):
        bh = CTkFrame(app, fg_color="#000000", width=1600, height=900)
        bh.place(x=0, y=0)
        ask = CTkFrame(app)
        ask.place(x=900, y=200)
        pywinstyles.set_opacity(bh, 0.5)
        cur.execute("SELECT NAME FROM playlists_data")
        option_list = []
        choices = cur.fetchall()
        for h in choices:
            option_list.append(h[0].replace("_", " "))

        global choice

        def optionmenu_callback(choice):

            global table
            table = choice.replace(" ", "_")

        optionmenu = CTkOptionMenu(ask, values=option_list,
                                   command=optionmenu_callback)
        optionmenu.pack()

        def vbn():
            global table

            cur.execute("INSERT INTO {} VALUES {}".format(table, song_tuple))

            mycon.commit()

            bh.destroy()
            ask.destroy()

        select_vut = CTkButton(ask, text="Select", command=vbn)
        select_vut.pack()

    # Iterate over image paths and create frames
    for index, i in enumerate(data):
        try:
            index -= nb
            ine = HoverButton2(scrollable_frame, text="", fg_color="#000000", hover_color="#282828", width=1420,
                               height=80)
            title_button = HoverButton3(ine, text=i[0][0:40],
                                        font=("CircularSp", 20, "normal"), anchor="w",
                                        fg_color="#000000", corner_radius=0, border_color="#000000",
                                        hover_color="#000000")
            button1 = HoverButton3(ine, text=i[4][0:20], hover_color="#000000", fg_color="#000000",
                                   font=("CircularSp", 14, "bold"), anchor="w", text_color="#FFFFFF", corner_radius=10,
                                   border_color="#000000")

            button2 = HoverButton1(ine, text=str(index + 1), width=5, height=20, corner_radius=10, border_width=0,
                                   border_spacing=0, hover_color="#000000", fg_color="#000000",
                                   font=("CircularSp", 16, "bold"), border_color="#000000")
            button3 = HoverButton(ine, text="", image=adde, width=20, height=20, corner_radius=10, border_width=0,
                                  border_spacing=0, hover_color="#000000", fg_color="#000000",
                                  font=("CircularSp", 16, "bold"), border_color="#000000",
                                  command=lambda x=i: enter_playlist(x))
            label = HoverButton3(ine, text=i[1], font=("CircularSp", 16, "bold"), fg_color="#000000", corner_radius=0,
                                 hover_color="#000000")
            button4 = HoverButton(ine, text="🗑️",  width=20, height=20, corner_radius=10, border_width=0,
                                  border_spacing=0, hover_color="#000000", fg_color="#000000",
                                  font=("CircularSp", 16, "bold"), border_color="#000000",
                                  command=lambda x=i,y=ine: delete_row_from_all_tables(x,y))

            # Store child widgets in the dictionary
            ine.child_widgets.append(label), ine.child_widgets.append(title_button), ine.child_widgets.append(
                button2), ine.child_widgets.append(button3),ine.child_widgets.append(button4), ine.child_widgets.append(button1)
            ine.pack()
            title_button.place(x=50, y=10), button1.place(x=50, y=40), button2.place(x=0, y=25), button3.place(x=400,y=40), button4.place(x=350,
                                                                                                               y=40), label.place(
                x=400, y=10)


            title_button.configure(command=lambda path=i: replace_extension(path))
            button2.configure(command=lambda path=i: replace_extension(path))
        except:
            nb += 1
            pass
def f11():
    # Path to the directory containing images
    global opt1
    opt1= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt1.place(x=3330, y=122)

    create_image_frames(opt1,'Alec_Benjamin')

def f():
    # Path to the directory containing images
    global opt0
    opt0= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt0.place(x=3330, y=122)

    create_image_frames(opt0,'Duncan_Laurence')
def f22():
    # Path to the directory containing images
    global opt2

    opt2= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt2.place(x=3330, y=122)

    create_image_frames(opt2,'Billie_Eilish')
def f33():
    # Path to the directory containing images
    global opt3
    opt3= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt3.place(x=3330, y=122)

    create_image_frames(opt3,'JustinBieber')
def f44():
    # Path to the directory containing images
    global opt4
    opt4= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt4.place(x=3330, y=122)

    create_image_frames(opt4,'XXX_Tentacion')
def f66():
    # Path to the directory containing images
    global opt6

    opt6= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt6.place(x=3330, y=122)
    create_image_frames(opt6,"Ed_Sheeran")
def f77():
    # Path to the directory containing images
    global opt7

    opt7= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt7.place(x=3330, y=122)

    create_image_frames(opt7,"Arijit_Singh")
def f88():
    # Path to the directory containing images
    global opt8

    opt8= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt8.place(x=3330, y=122)

    create_image_frames(opt8,"Imagine_Dragons")
def f99():
    # Path to the directory containing images
    global opt9
    opt9= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt9.place(x=3330, y=122)

    create_image_frames(opt9,"Anuv_Jain")
def f10():
    # Path to the directory containing images
    global opt10
    opt10= CTkFrame(app,width=1500,height=700,fg_color="#000000")
    opt10.place(x=3330, y=122)

    create_image_frames(opt10,"Taylors_Swift")
import random
def move_label(label):
    x, y = label.place_info()['x'], label.place_info()['y']

    if int(x) < 400:  # Change 400 to the desired end point
        label.place(x=int(x)+50, y=y)  # Move the label 5 pixels to the right
        label.after(10, lambda: move_label(label))  # Call move_label again after 50 milliseconds



def show_history(k, l, i):
    image_dir = i[4]
    alb1 = CTkImage(light_image=Image.open(i[3]), dark_image=Image.open(i[3]), size=(170, 170))
    tile = HoverButton(f2, text=i[0][0:20] + '\n~' + image_dir[0:20], image=alb1, compound=TOP, height=280, border_spacing=0,
                       font=("CircularSp", 17, "bold"), border_width=0, fg_color="#121212", corner_radius=15,
                       hover_color="#1a1a1a")
    tile.place(x=k, y=l)

    tile.configure(command=lambda path=i: replace_extension(path))

def create_history(song_tuple):
    cur.execute("USE SPOTIFY")
    current_time = datetime.now().strftime("%D %H:%M:%S")
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS History(Name VARCHAR(100), DURATION VARCHAR(10), FILE_PATH VARCHAR(200), IMG_PATH VARCHAR(200),Artist VARCHAR(100), TIME VARCHAR(30))"
    )
    cur.execute("select FILE_PATH from History")
    data_his = cur.fetchall()
    if (song_tuple[2],) in data_his:
        cur.execute(f"UPDATE History SET TIME = '{current_time}' WHERE Name = '{song_tuple[0]}'")
        mycon.commit()
    else:
        cur.execute(f"INSERT INTO History VALUES {song_tuple + (current_time,)}")

    try:
        cur.execute("SELECT * FROM History ORDER BY TIME DESC LIMIT 5;")
        history = cur.fetchall()
        for index, i in enumerate(history):
            k = 10 + int(index * 230)
            show_history(k, 50, i)
    except:
        pass


def fgh():
    try:
        cur.execute("SELECT * FROM Downloads ;")
        data1 = cur.fetchall()
        data = []
        for i in data1:
            data.append(i)
        global but_list
        lengt = len(but_list)
        if lengt <5:
            for j in but_list:
                j.destroy()

            for index, i in enumerate(data[-1:-6:-1]):
                k = 10 + int(index * 230)
                show_downloads(k, 50, i)
        else:
            for index, i in enumerate(data[-1:-6:-1]):
                alb1 = CTkImage(light_image=Image.open(i[3]), dark_image=Image.open(i[3]), size=(170, 170))
                but_list[index].configure(text=i[0][0:20] + '\n~' + i[4][0:20], image=alb1, compound=TOP, height=280,
                                   border_spacing=0,
                                   font=("CircularSp", 17, "bold"), border_width=0, fg_color="#121212",
                                   corner_radius=15,
                                   hover_color="#1a1a1a")
                but_list[index].configure(command=lambda path=i: replace_extension(path))

    except:
        pass
    f5.after(1000, fgh)
T =threading.Thread(target=fgh,args=())
T.start()



def show_downloads(k, l, i):
    alb1 = CTkImage(light_image=Image.open(i[3]), dark_image=Image.open(i[3]), size=(170, 170))
    tile = HoverButton(f5, text=i[0][0:20] + '\n~' + i[4][0:20], image=alb1, compound=TOP, height=280,
                       border_spacing=0,
                       font=("CircularSp", 17, "bold"), border_width=0, fg_color="#121212",
                       corner_radius=15,
                       hover_color="#1a1a1a")
    tile.place(x=k, y=l)
    tile.configure(command=lambda path=i: replace_extension(path))
    but_list.append(tile)
h = CTkFrame(app, width=1500, height=700, fg_color="#000000")
app.mainloop()
