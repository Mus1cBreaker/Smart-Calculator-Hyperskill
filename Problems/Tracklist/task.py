def tracklist(**artists):
    for artist, albums in artists.items():
        print(artist)
        for album, song in albums.items():
            print("ALBUM: " + album + " TRACK: " + song)