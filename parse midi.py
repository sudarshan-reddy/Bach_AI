from midiutil.MidiFile import MIDIFile
MyMIDI = MIDIFile(1)
track = 0
time = 0
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time,120)

songdata = [[3, 1, 1, 1, 0], [3, 12, 1, 1, 0], [27, 3, 0, 2, 0], [26, 11, 0, 2, 0], [19, 3, -1, 1, 0], [18, 5, -1, 1, 0], [16, 4, 0, 1, 0], [18, 6, 0, 1, 0], [16, 0, 2, 1, 0], [19, 4, 2, 1, 0], [9, 2, 2, 0, 0], [13, 3, 2, 0, 0], [8, 4, 1, 0, 0], [10, 5, 1, 0, 0], [7, 3, 1, 0, 0], [9, 7, 1, 0, 0], [6, 3, 1, 0, 0], [9, 6, 1, 0, 0], [7, 3, 2, 0, 0], [9, 6, 2, 0, 0], [7, 0, 1, 0, 0], [8, 4, 1, 0, 0], [22, 3, 0, 1, 0], [8, 4, 0, 1, 0], [27, 1, -1, 1, 0], [13, 4, -1, 1, 0], [29, 4, 0, 1, 0], [20, 3, 0, 1, 0], [26, 9, -3, 0, 0], [16, 6, -3, 0, 0], [28, 6, -3, 1, 0], [20, 7, -3, 1, 0], [14, 4, -1, 1, 0], [14, 6, -1, 1, 0], [13, 4, -1, 1, 0], [10, 5, -1, 1, 0], [12, 4, -1, 1, 0], [8, 5, -1, 1, 0], [12, 4, 0, 1, 0], [8, 6, 0, 1, 0], [9, 3, 0, 1, 0], [3, 5, 0, 1, 0], [9, 4, 2, 1, 0], [4, 5, 2, 1, 0], [11, 4, 1, 1, 0], [6, 5, 1, 1, 0], [11, 6, 0, 1, 0], [12, 6, 0, 1, 0], [8, 5, 0, 1, 0], [6, 7, 0, 1, 0], [8, 5, 0, 1, 0], [4, 7, 0, 1, 0], [11, 6, 0, 1, 0], [5, 8, 0, 1, 0], [12, 7, 0, 1, 0], [6, 8, 0, 1, 0], [11, 8, 0, 1, 0], [5, 8, 0, 1, 0], [7, 8, 0, 0, 0], [4, 8, 0, 0, 0], [6, 9, 0, 0, 0], [3, 7, 0, 0, 0], [3, 10, 0, 0, 0], [2, 5, 0, 0, 0], [2, 9, 0, 0, 0], [0, 5, 0, 0, 0], [1, 9, 0, 0, 0], [0, 4, 0, 0, 0], [1, 9, 0, 0, 0], [0, 4, 0, 0, 0], [1, 8, 0, 0, 0], [0, 4, 0, 0, 0], [3, 8, 0, 0, 0], [3, 2, 0, 0, 0], [1, 6, 2, 0, 0], [-1, 3, 2, 0, 0], [4, 3, 1, 0, 0], [0, 3, 1, 0, 0], [5, 6, -1, 1, 0], [-4, 7, -1, 1, 0], [6, 5, -1, 1, 0], [1, 9, -1, 1, 0], [17, 3, -1, 1, 0], [14, 5, -1, 1, 0], [18, 4, -2, 0, 0], [18, 5, -2, 0, 0], [18, 8, -2, 1, 0], [17, 7, -2, 1, 0], [25, 13, -3, 0, 0], [25, 6, -3, 0, 0], [25, 10, -2, 0, 0], [26, 7, -2, 0, 0], [22, 4, 0, 0, 0], [13, 9, 0, 0, 0], [19, 0, 0, 0, 0], [11, 5, 0, 0, 0], [21, 1, 0, 0, 0], [13, 6, 0, 0, 0], [8, 5, 0, 0, 0], [7, 7, 0, 0, 0]]



for note in songdata:
    pitch = note[0] + 60
    if pitch < 60:
        pitch = 60
    if pitch > 84:
        pitch = 80
    duration = (note[1] / 8.0)
    if duration == 0:
        duration = 1
    time += duration
    print time
    MyMIDI.addNote(0,0,pitch,time,duration,100)

binfile = open("song.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()