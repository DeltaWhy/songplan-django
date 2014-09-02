import re

def transpose(original_key, key, chords):
    note_numbers = {'Ab':0, 'A':1, 'A#':2, 'Bb':2, 'B':3, 'C':4,
            'C#':5, 'Db':5, 'D':6, 'D#':7, 'Eb':7, 'E':8, 'F':9,
            'F#':10, 'Gb':10, 'G':11, 'G#':0}
    if key in ['G','D','A','E','B','F#']:
        number_notes = {0:'G#', 1:'A', 2:'A#', 3:'B', 4:'C', 5:'C#',
            6:'D', 7:'D#', 8:'E', 9:'F', 10:'F#', 11:'G'}
    else:
        number_notes = {0:'Ab', 1:'A', 2:'Bb', 3:'B', 4:'C', 5:'Db',
            6:'D', 7:'Eb', 8:'E', 9:'F', 10:'Gb', 11:'G'}
    transpose_factor = note_numbers[key] - note_numbers[original_key]
    new_chords = ""
    for line in chords.splitlines():
        if not(re.search(r'^[\s]*([A-G][\w#+-/]*[\s]*)*$', line)):
            new_chords += line + '\n'
            continue
        if re.search(r'(?i)(chorus|bridge|because|forever)', line):
            new_chords += line + '\n'
            continue
        line = re.sub('(^|[\s]|/|-)([A-G][#b]?)', 
            lambda x: x.group(1) + number_notes[(note_numbers[x.group(2)]+transpose_factor)%12],
            line)
        new_chords += line + '\n'
    return new_chords

def nashville(original_key, chords):
    note_numbers = {'Ab':0, 'A':1, 'A#':2, 'Bb':2, 'B':3, 'C':4,
            'C#':5, 'Db':5, 'D':6, 'D#':7, 'Eb':7, 'E':8, 'F':9,
            'F#':10, 'Gb':10, 'G':11, 'G#':0}
    number_notes = {0:'1', 1:'1#', 2:'2', 3:'2#', 4:'3', 5:'4',
        6:'5b', 7:'5', 8:'6b', 9:'6', 10:'7b', 11:'7'}
    transpose_factor = -note_numbers[original_key]
    new_chords = ""
    for line in chords.splitlines():
        if not(re.search(r'^[\s]*([A-G][\w#+-/]*[\s]*)*$', line)):
            new_chords += line + '\n'
            continue
        if re.search(r'(?i)(chorus|bridge|because|forever)', line):
            new_chords += line + '\n'
            continue
        line = re.sub('(^|[\s]|/|-)([A-G][#b]?)', 
            lambda x: x.group(1) + number_notes[(note_numbers[x.group(2)]+transpose_factor)%12],
            line)
        new_chords += line + '\n'
    return new_chords

def headerlines(chords):
    lines = []
    for i in range(len(chords.splitlines())):
        if re.search(r'(?i)^[\s(\[]*(intro|tag|ending|chorus|verse|bridge|pre[-]?chorus)[\s]*[\d]*[)\]:]*[\s]*(\(.*\))?[\s]*$', chords.splitlines()[i]):
            lines.append(i)
    return lines

def lyrics(chords):
    lyrics = ""
    for line in chords.splitlines():
        if not(re.search(r'^[\s]*([A-G][\w#+-/]*[\s]*)*$', line)):
            lyrics += line.strip() + '\n'
            continue
        if re.search(r'(?i)(chorus|bridge|because|forever)', line):
            lyrics += line.strip() + '\n'
            continue
    return lyrics

def splitlyrics(chords):
    strLyrics = lyrics(chords)
    arrHeaderlines = headerlines(strLyrics)
    lines = strLyrics.splitlines()
    knownStanzas = []
    result = {}
    currentTitle = ""
    currentStanza = ""

    for i in range(len(lines)):
        if i in arrHeaderlines:
            if currentTitle != "" and currentStanza != "":
                result[currentTitle] = currentStanza
                knownStanzas.append(currentTitle)
            currentTitle = re.search(r'(?i)(intro|tag|ending|chorus|verse|bridge|pre[-]?chorus)[\s]*[\d]*', lines[i]).group(0).capitalize()
            currentStanza = ""
        else:
            currentStanza += lines[i] + "\n"
    if currentTitle != "" and currentStanza != "":
        result[currentTitle] = currentStanza
        knownStanzas.append(currentTitle)

    return result
