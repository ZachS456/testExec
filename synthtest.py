import subprocess

def to_wav(sf2, filename):
    subprocess.call(['fluidsynth', '-T', 'wav', '-F', filename, '-ni', sf2, 'tester.mid'])

to_wav('Astral Harmonica.sf2', '1-AH.wav')
to_wav('Mournsax.sf2', '2-MS.wav')
to_wav('SGM-V2.01.sf2', '3-PIANO.wav')