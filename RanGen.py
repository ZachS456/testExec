import pykov
import nltk
import random
from nltk.collocations import *
MAXIMUM_RECURRING_TIMES = 1

class RanGen:

    def __init__(self, data, count):
        self.bigram_measures = nltk.collocations.BigramAssocMeasures()
        with open(data, 'r') as dataDelim:
            self.lst = [line.rstrip().split('-') for line in dataDelim]
        with open(count,'r') as noLines:
            self.totallst = noLines.read().split('-')
        self.oChain = pykov.Matrix()

    def find_bigrams(self):
        for song in self.lst:
        	#print "regular: %s" % (song)
        	finder = BigramCollocationFinder.from_words(song)
        	bigrams = finder.nbest(self.bigram_measures.pmi,10)
        	#print "bigrams: %s\n" % (bigrams)
        	for note1,note2 in bigrams:
        		self.oChain[(note1,note2)] += 1

        for (note1,note2) in self.oChain:
        	if not self.oChain.succ(note2):
        			self.oChain[(note2, random.choice(self.totallst).rstrip())] = 1

        #self.oChain['END','END'] = 1
        self.oChain.stochastic()

        #for note1,note2 in self.oChain:
        	#print("Note: %s\n%s\n" % (note1,self.oChain.succ(note1)))

    def walk_mc(self, choice=None, i1=None, i2=None):
        song = pykov.Chain(self.oChain)

        if choice == None or choice == 'RAND':
            choice = random.choice(self.totallst).rstrip()
        if i1 == None:
            i1 = 6
        if i2 == None:
            i2 = 12

        #print("WALK")
        randLength = random.randint(i1,i2)
        song.move(choice)
        output = "['"
        output += choice
        output += "', '"
        reccTimes = 0
        dualReccTimes = 0
        noteList = []
        noteList.append(choice)
        for x in range(0,randLength):
            if x == 0:
                note = song.move(choice)
                noteList.append(note)
                output += note
                #output += "', '"
            else:
                tempNote = song.move(note)

                #handles recurring notes
                if tempNote == noteList[x-1]:
                    #save first note to come into the duplicate note
                    #handling
                    if reccTimes == 0:
                        firstCaughtDuplicate = tempNote

                    #if note that came in as duplicate isn't the original
                    #need to reset the times it has occured and reset
                    #the first caught duplicate
                    if firstCaughtDuplicate != tempNote:
                        reccTimes = 0
                        firstCaughtDuplicate = tempNote

                    #if note has occurred twice in a row, new note needs
                    #to be generated and reocc needs to be reset
                    #else, increment the amount of times the note has recurred
                    if reccTimes >= MAXIMUM_RECURRING_TIMES:
                        while tempNote == note:
                            tempNote = song.move(note)
                        reccTimes = 0
                    else:
                        reccTimes+=1

                #handles recurring dual notes
                if x > 2 and noteList[x-3] == noteList[x-1] and noteList[x-2] == tempNote:
                    #save first note to come into the duplicate note
                    #handling
                    if dualReccTimes == 0:
                        dualNote1 = noteList[x-1]
                        dualNote2 = tempNote

                    #if note that came in as duplicate isn't the original
                    #need to reset the times it has occured and reset
                    #the first caught duplicate
                    if dualNote1 != noteList[x-1] and dualNote2 != tempNote:
                        dualReccTimes = 0
                        dualNote1 = noteList[x-1]
                        dualNote2 = tempNote

                    #if dual note set has occurred twice in a row, new note needs
                    #to be generated and dualRecc needs to be reset
                    #else, increment the amount of times the note has recurred
                    if reccTimes >= MAXIMUM_RECURRING_TIMES:
                        while tempNote == noteList[x-1]:
                            tempNote = song.move(note)
                        dualReccTimes = 0
                    else:
                        dualReccTimes+=1
                note = tempNote
                noteList.append(note)
                output += "', '"
                output += note
            #print ("%d: %s" % (x, note))
        output += "']"
        print (output)
        #print (song.walk_propability(choice))
        #return song.walk(random.randint(i1,i2),choice)
        return noteList
