from RanGen import RanGen
import pickle

r = RanGen('dataDelim.txt', 'noLines.txt')
r.find_bigrams()
print("\n\n\n\n\n\n\n\n")
r.walk_mc()

pickle.dump(r, open('saver.p', 'wb'))
r = None

r2 = pickle.load(open('saver.p', 'rb'))

r2.find_bigrams()

r2.walk_mc()
