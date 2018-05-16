from pathlib import Path
import csv
 
def clean_song(song):
    song = song.replace("\n", " ")
    song = song.replace("\t", " ")
    song = song.replace("\"", "")
    song = song.replace("\'", "")
    song = song.replace(",", "")
    song = song.replace(";", "")
    song = song.replace("<i>", "")
    song = song.replace("</i>", "")
    song = song.replace("<b>", "")
    song = song.replace("</b>", "")
    song = song.replace("[Intro]", "")
    song = song.replace("[Chorus]", "")
    song = song.replace("[Bridge]", "")
    song = song.replace("x2", "")
    song = song.replace("x3", "")
    song = song.replace("x4", "")
    song = song.replace("x5", "")
    song = song.replace("x6", "")
    return song

with open('test.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #filewriter.writerow(['Genre', 'Lyrics'])

    pathroot = "data/test/"
    pathlist = Path(pathroot + "happy/").glob('*.txt')
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        song = open(path_in_str, "r")
        song = clean_song(song.read())
        print(path_in_str)
        print("==========================")
        filewriter.writerow(['Happy', song])

    pathlist = Path(pathroot + "sad/").glob('*.txt')
    for path in pathlist:
        path_in_str = str(path)
        song = open(path_in_str, "r")
        song = clean_song(song.read())
        print(path_in_str)
        print("==========================")
        filewriter.writerow(['Sad', song])

    pathlist = Path(pathroot + "angry/").glob('*.txt')
    for path in pathlist:
        path_in_str = str(path)
        song = open(path_in_str, "r")
        song = clean_song(song.read())
        print(path_in_str)
        print("==========================")
        filewriter.writerow(['Angry', song])

