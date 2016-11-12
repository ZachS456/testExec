from midiutil.MidiFile import MIDIFile
from RanGen import RanGen
import re
import pickle
import argparse
import os
def runner(length, start, fname):
    r2 = pickle.load(open('saver.p', 'rb'))
    lster = r2.walk_mc(start, length, length)
    print (lster)
    tmp = [s.split("(") for s in lster]
    notes = []
    durs = []
    for dur in tmp:
        if len(dur) > 1:
            durs.append(dur[1])
            del dur[1]
        notes.append(dur[0])
    durs = [s.strip(")") for s in durs]
    #print(notes)
    #print(durs)
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 140)

    # add some notes
    channel = 0
    volume = 100
    tmptime = 0
    time = 0
    for nts, dur in zip(notes, durs):
        if nts.count(',') > 0:
            print(nts)
            lst = nts.split(',')
            #print(lst)
            for ln in lst:
                if int(nts) > 0:
                    pitch = int(ln) + 40
            duration = float(dur)
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += float(dur)
        elif nts != 'END':
            if int(nts) > 0:
                pitch = int(nts) + 40
            else:
                tmptime = float(dur)
                continue
            if(tmptime > 0):
                time += tmptime             # start on beat 0
            duration = float(dur)         # 1 beat long
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += float(dur)

    # write it to disk
    fname += '.mid'
    with open(fname, 'wb') as outf:
        mf.writeFile(outf)
    path = os.getcwd()
    path += '/'
    path += fname
    print (path)

def main():
    #print("Hello")
    parser = argparse.ArgumentParser(description="""Make a log of hashes of the #
                                    filesystem files, and check the log file for changes.""") # Sets up all of the parsing for the program takes a mandatory
    parser.add_argument('-l', '-length', action='store', dest='length', type=int, default=6, help='set the jingle length. Defaults to 6') #argument for checking
    parser.add_argument('-s', action='store', dest='start', type=str, default=None, help='User Selected Starting note.')
    parser.add_argument('-fname', action='store', dest='fname', type=str, default='File', help='The temporary filename for the jingle.')
    args = parser.parse_args()
    runner(args.length, args.start, args.fname)

main()
