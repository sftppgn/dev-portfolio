import wave
import sys
import random 
import string

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'music\\temp_media\\') 
ACOUSTIC_ROOT = os.path.join(BASE_DIR, 'music\\acoustic_notes\\') 

#from playsound import playsound
defaultNoteTime = 20000
tempfile = (''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
finalFileName= ''.join(MEDIA_ROOT+tempfile+".wav")
outfile = wave.open(finalFileName, 'w')
#outfile = wave.open("outfile.wav", 'w')
content={
'filename':finalFileName,
} 
print (MEDIA_ROOT)

#set required params on outfile
#print ("test")
baseline = wave.open(ACOUSTIC_ROOT+"baseline.wav", 'r')
outfile.setparams(baseline.getparams())
baseline.close()

#if documentation is unclear after first if statement, you'll likely need to review guitar/music scales 

def write(note,time=defaultNoteTime):
    #if we've passed in 0en (first octave e natural), referencing "0" octave, "e" note, "n" for natural (vs "s" for sharp)
    if "0en" in note:
        #set the note to the e0 wav file (E string, open)
        note = wave.open(ACOUSTIC_ROOT+"e0.wav", 'r')

    elif "0fn" in note:
        note = wave.open(ACOUSTIC_ROOT+"e1.wav", 'r')

    elif "0fs" in note:
        note = wave.open("./music/acoustic_notes/e2.wav", 'r')

    elif "0gn" in note:
        note = wave.open("./music/acoustic_notes/e3.wav", 'r')

    elif "0gs" in note:
        note = wave.open("./music/acoustic_notes/e4.wav", 'r')

    elif "0an" in note:
        note = wave.open("./music/acoustic_notes/a0.wav", 'r')

    elif "0as" in note:
        note = wave.open("./music/acoustic_notes/a1.wav", 'r')

    elif "0bn" in note:
        note = wave.open("./music/acoustic_notes/a2.wav", 'r')

    elif "0cn" in note:
        note = wave.open("./music/acoustic_notes/a3.wav", 'r')

    elif "0cs" in note:
        note = wave.open("./music/acoustic_notes/a4.wav", 'r')

    elif "0dn" in note:
        note = wave.open("./music/acoustic_notes/d0.wav", 'r')

    elif "0ds" in note:
        note = wave.open("./music/acoustic_notes/d1.wav", 'r')

    elif "1en" in note:
        note = wave.open("./music/acoustic_notes/d2.wav", 'r')

    elif "1fn" in note:
        note = wave.open("./music/acoustic_notes/d3.wav", 'r')

    elif "1fs" in note:
        note = wave.open("./music/acoustic_notes/d4.wav", 'r')

    elif "1gn" in note:
        note = wave.open("./music/acoustic_notes/g0.wav", 'r')

    elif "1gs" in note:
        note = wave.open("./music/acoustic_notes/g1.wav", 'r')

    elif "1an" in note:
        note = wave.open("./music/acoustic_notes/g2.wav", 'r')

    elif "1as" in note:
        note = wave.open("./music/acoustic_notes/g3.wav", 'r')

    elif "1bn" in note:
        note = wave.open("./music/acoustic_notes/g4.wav", 'r')

    elif "1bn" in note:
        note = wave.open("./music/acoustic_notes/b0.wav", 'r')

    elif "1cn" in note:
        note = wave.open("./music/acoustic_notes/b1.wav", 'r')

    elif "1cs" in note:
        note = wave.open("./music/acoustic_notes/b2.wav", 'r')

    elif "1dn" in note:
        note = wave.open("./music/acoustic_notes/b3.wav", 'r')

    elif "1ds" in note:
        note = wave.open("./music/acoustic_notes/b4.wav", 'r')

    elif "2en" in note:
        note = wave.open("./music/acoustic_notes/ehi1.wav", 'r')

    elif "2fn" in note:
        note = wave.open("./music/acoustic_notes/ehi2.wav", 'r')

    elif "2fs" in note:
        note = wave.open("./music/acoustic_notes/ehi3.wav", 'r')

    elif "2gn" in note:
        note = wave.open("./music/acoustic_notes/ehi4.wav", 'r')

    elif "2gs" in note:
        note = wave.open("./music/acoustic_notes/ehi5.wav", 'r')

    elif "2an" in note:
        note = wave.open("./music/acoustic_notes/ehi6.wav", 'r')

    elif "2as" in note:
        note = wave.open("./music/acoustic_notes/ehi7.wav", 'r')

    elif "2bn" in note:
        note = wave.open("./music/acoustic_notes/ehi8.wav", 'r')

    elif "2cn" in note:
        note = wave.open("./music/acoustic_notes/ehi9.wav", 'r')

    elif "2cs" in note:
        note = wave.open("./music/acoustic_notes/ehi10.wav", 'r')

    elif "2dn" in note:
        note = wave.open("./music/acoustic_notes/ehi11.wav", 'r')

    elif "2ds" in note:
        note = wave.open("./music/acoustic_notes/ehi12.wav", 'r')

    elif "3en" in note:
        note = wave.open("./music/acoustic_notes/ehi13.wav", 'r')

    elif "3fn" in note:
        note = wave.open("./music/acoustic_notes/ehi14.wav", 'r')

    elif "3fs" in note:
        note = wave.open("./music/acoustic_notes/ehi15.wav", 'r')

    elif "3gn" in note:
        note = wave.open("./music/acoustic_notes/ehi16.wav", 'r')

    elif "3gs" in note:
        note = wave.open("./music/acoustic_notes/ehi17.wav", 'r')

    elif "3an" in note:
        note = wave.open("./music/acoustic_notes/ehi18.wav", 'r')

    elif "3as" in note:
        note = wave.open("./music/acoustic_notes/ehi19.wav", 'r')

    elif "3bn" in note:
        note = wave.open("./music/acoustic_notes/ehi20.wav", 'r')

    elif "rst" in note:
        note = wave.open("./music/acoustic_notes/rest.wav", 'r')
    else:
        print("You've passed in an invalid note.  Review the documentation.")

    outfile.writeframes(note.readframes(time))
    print ("wrote ", note, " to ", outfile)
    note.close()
    
    return (content)

def closeFile():
    #print ("closing ", outfile)
    outfile.close()

def getTempFilename():
    return(content['filename'])
def getTempDict():
    return(content)