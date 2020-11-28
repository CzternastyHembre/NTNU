def sec_to_time(sec):
    h = sec//(60*60)
    sec = sec%(60**2)
    m = sec//(60)
    sec = sec%(60)
    s = sec

    if s < 10:
        s = '0'+str(s)
    s = ':'+str(s)
    if 0 < m < 10:
        m = '0'+str(m)
    if h > 0:
        m = str(h)+':'+str(m)
    time = str(m)+str(s)
    return time

#  sec_to_time(11129)

def time_to_sec(str1):
    time = str1.split(':')
    sec = 0
    l = len(time)-1
    for i in range(l+1):
        if time[i].isdigit():
            sec += int(time[i])*60**(l-i)
    return sec

def enter_song():
    while True:
        print('Enter song (Title;Artist;Genre;m:s)')
        song = input('> ')
        song = song.split(';')

        time = song[-1].split(':')

        if len(song) == 4:
            if time[0].isdigit() and time[1].isdigit():
                if 0 <= int(time[0]) <= 60 and 0 <= int(time[1]) <= 60:
                    return song
        print('Ugyldige data! Formatet må være: (Title;Artist;Genre;m:s) ')


def read_file(filename):
    songs = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(';')
            songs.append(line)

    return songs

#  print(read_file('songlist.txt'))

def list_content(filename, choice):
    songs = read_file(filename)
    choices = {
        'title': 0,
        'artist': 1,
        'genre': 2,
    }
    arr = []
    if choice in choices:
        for song in songs:
            arr.append(song[choices[choice]])
    arr = list(set(arr))

    return arr

#   print(list_content('songlist.txt','person'))
#   print(list_content('songlist.txt','artist'))

def list_song_genre(filename):
    songs = read_file(filename)

    genres = list_content(filename, 'genre')
    genre = input('Choose genre ' + str(genres) + ' : ')

    time = 0
    usedSongs = []
    for song in songs:
        if genre in song:
            time += time_to_sec(song[-1])
            usedSongs.append([song[0],song[1],song[3]])

    if time != 0:
        time = sec_to_time(time)
    else:
        time = '0:0'
    return (usedSongs, time)

print(list_song_genre('songlist.txt'))

def pretty_print(filename):
    list_songs_time = list_song_genre(filename)
    print( '\n%-30s%-30s%-10s' % ('Artist','Title','Time'))
    for song in list_songs_time[0]:
        print ('%-30s%-30s%-10s' % (song[1],song[0],song[-1]))

    print('\nTotal time:', list_songs_time[-1])


def add_song(filename):
    newsong = enter_song()

    songs = read_file(filename)

    for song in songs:
        if newsong[0] == song[0] and newsong[1] == song[1]:
            print(song[0], 'Already exist in', filename)
            return

    newsong = ';'.join(newsong)
    print(newsong)
    with open(filename, 'a') as f:

        f.write('\n'+newsong)


#   add_song('songlist.txt')

pretty_print('songlist.txt')


