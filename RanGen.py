import pykov
import nltk
import random
from nltk.collocations import *
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

        for note1,note2 in self.oChain:
        	print("Note: %s\n%s\n" % (note1,self.oChain.succ(note1)))

    def walk_mc(self, choice=None, i1=None, i2=None):
        song = pykov.Chain(self.oChain)

        if choice == None or choice == 'RAND':
            choice = random.choice(self.totallst).rstrip()
        if i1 == None:
            i1 = 6
        if i2 == None:
            i2 = 12

        print("WALK")
        return song.walk(random.randint(i1,i2),choice)
