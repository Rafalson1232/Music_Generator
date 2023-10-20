from music import (Phrase, Note, Play)

Major = [0, 2, 4, 5, 7, 9, 11, 12]
Minor = [0, 2, 3, 5, 7, 8, 10, 12]
Strong = [1, 0, 0, 1, 1, 1, 0, 1]

def wordToList(word):
    list = []
    for i in word:
        list.append(ord(i))
    return list

def listToLastRootScale(list, scaleType, scaleRoot):
    list = []
    step = ord(list[len(list)-1])%7
    for i in list:
        list.append(scaleRoot + scaleType[(i - step)%7])
    return list

def wordToLastRootScale(word, scaleType, scaleRoot):
    listIn = wordToList(word)
    step = listIn[len(listIn)-1]%7
    listOut = []
    for i in listIn:
        listOut.append(scaleRoot + scaleType[(i - step)%7])
    return listOut
    
def wordToRythm(word):
    StrAndWeak = [1, 0.5, 0.5, 1, 1, 1, 0.5, 1]
    rythm = []
    list = wordToLastRootScale(word, Minor, 58)
    i = 0
    for j in list:
        if StrAndWeak[j%7] == 1:
            rythm.append(StrAndWeak[j%7])
        else:
            rythm.append(StrAndWeak[j%7])
            if i>0:
                rythm[i-1] = 0.5
        i += 1
    return rythm
mPhrase = Phrase()
word = "love you very much"
word = "zabierz mnie na kregle"
mPhrase.addNoteList(wordToLastRootScale(word, Minor, 58), wordToRythm(word))

Play.midi(mPhrase)
