import re
import urllib.request
import csv
from bs4 import BeautifulSoup
 
mood = "happy/"
def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    filename = song_title + " - " + artist + ".txt"
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        f = open("data/" + mood + filename, "w")
        f.write(lyrics)
        f.close()
        return lyrics
    except Exception as e:
        print(filename)
        f = open("data/" + mood + "missing.txt", "a")
        f.write(filename)
        f.close()
        print (str(e))
        return "Exception occurred \n" +str(e)

with open("songs.csv") as f:
    for row in f:
        rows = row.split(",")
        full = rows[0].split("-")
        #print(full)
        song = full[0].strip()
        artist = full[1].strip()
        get_lyrics(artist, song)
        
        
