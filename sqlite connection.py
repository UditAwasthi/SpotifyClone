import os
from customtkinter import *
import pygame
import math

# Initialize Pygame mixer
pygame.mixer.init()

# Dictionary to store song titles and duratons


import sqlite3 as sq
mycon = sq.connect('Spotify.db')
cur = mycon.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS all_songs_data (Name TEXT, DURATION TEXT, FILE_PATH TEXT, IMG_PATH TEXT, Artist TEXT)")


def files_data_insert(directory,Table_Name,artist):
    songs_data = []


    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        seconds %= 60
        global tdur
        tdur = f"{math.ceil(minutes)}:{math.ceil(seconds)}"
        if int(f"{math.ceil(minutes)}") < 10:
            a = "0" + f"{math.ceil(minutes)}"
        else:
            a = f"{math.ceil(minutes)}"
        if int(f"{math.ceil(seconds)}") < 10:
            b = "0" + f"{math.ceil(seconds)}"
        else:
            b = f"{math.ceil(seconds)}"
        return f"{a}:{b}"

    # Iterate over files in the directory
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            # Get the full path to the file
            song_path = os.path.join(directory, file)

            # Get the song title (without the file extension)
            song_title = os.path.splitext(file)[0]

            # Get the duration of the song
            sound = pygame.mixer.Sound(song_path)
            duration = sound.get_length()

            # Store the song title and duration in the dictionary
            songs_data.append((song_title, seconds_to_minutes(duration), song_path, song_path.rstrip(".mp3") + ".jpg",artist))

    print(songs_data)
    # Create a table with parameterized query
    # Create a table with parameterized query
    cur.execute(
        f"CREATE TABLE IF NOT EXISTS {Table_Name} (Name TEXT, DURATION TEXT, FILE_PATH TEXT, IMG_PATH TEXT, Artist TEXT)")

    # Commit the changes
    mycon.commit()
    for i in songs_data:
        print(i)
        cur.execute(f"INSERT INTO {Table_Name} VALUES{i}")
        cur.execute(f"INSERT INTO all_songs_data VALUES{i}")
        mycon.commit()

# Path to the directory containing MP3 files
def insert():
    files_data_insert("All resources\\Justin Bieber","JustinBieber","Justin Bieber")
    files_data_insert("All resources\\Alec Benjamin","Alec_Benjamin","Alec Benjamin")
    files_data_insert("All resources\\Anuv Jain","Anuv_Jain","Anuv Jain")
    files_data_insert("All resources\\Arijit Singh","Arijit_Singh","Arijit Singh")
    files_data_insert("All resources\\Billie Eilish","Billie_Eilish","Billie Eilish")
    files_data_insert("All resources\\Duncan Laurence","Duncan_Laurence","Duncan Laurence")
    files_data_insert("All resources\\Ed Sheeran","Ed_Sheeran","Ed Sheeran")
    files_data_insert("All resources\\Imagine Dragons","Imagine_Dragons","Imagine Dragons")
    files_data_insert("All resources\\Taylors Swift","Taylors_Swift","Taylors Swift")
    files_data_insert("All resources\\XXX Tentacion","XXX_Tentacion","XXX Tentacion")

    # Query the database to get all rows
def clear(table_name):
    # Select IMG_PATH from the table
    cur.execute("SELECT IMG_PATH FROM {}".format(table_name))
    rows = cur.fetchall()

    # Check if both files exist for each row
    for row in rows:
        mp3_file = row[0].rstrip(".jpg") + ".mp3"
        if not os.path.exists(row[0]) or not os.path.exists(mp3_file):
            # If either file is missing, delete the row
            cur.execute("DELETE FROM {} WHERE IMG_PATH = ?".format(table_name), (row[0],))
            # Commit the change for each deleted row
            mycon.commit()

def clearAll():
        clear("Alec_Benjamin")
        clear("Anuv_Jain")
        clear("Arijit_Singh")
        clear("Billie_Eilish")
        clear("Duncan_Laurence")
        clear("Ed_Sheeran")
        clear("Imagine_Dragons")
        clear("Taylors_Swift")
        clear("XXX_Tentacion")
        clear("JustinBieber")
        clear("All_Songs_Data")
# Close the connection
app = CTk()
# app.iconbitmap(r"C:\Users\nothing\Downloads\Default_Design_a_logo_for_BeatBlast_a_music_player_and_downloa_1_8f9a8131-cc2c-4171-ac93-c5358f6a4ab7_0.ico")
app.title("Setup - Beat Blast")
app.geometry("800x500")
app.resizable(0,0)
app.mainloop()

