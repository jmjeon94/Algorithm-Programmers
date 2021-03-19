def get_time(start, end):
    h1, m1 = start.split(':')
    h2, m2 = end.split(':')
    if h1==h2:
        return int(m2)-int(m1)
    else:
        return (int(h2)-int(h1))*60 + int(m2)-int(m1)

def convert(song):
    song = song.replace('C#', 'O')
    song = song.replace('D#', 'P')
    song = song.replace('F#', 'Q')
    song = song.replace('G#', 'R')
    song = song.replace('A#', 'S')
    return song

def solution(m, musicinfos):
    answer = '(None)'
    answer_len = 0

    for music in musicinfos:
        start, end, name, song = music.split(',')
        time = get_time(start, end)
        song = convert(song)
        m = convert(m)

        while len(song)<time:
            song += song
        song = song[:time]

        # print(song, m)
        if m in song:
            if answer_len < time:
                answer_len = time
                answer = name

    return answer

print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
