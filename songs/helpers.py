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
    for line in chords.split('\n'):
        if not(re.search(r'^[\s]*([A-G][\w#+-]*[\s]*)*$', line)):
            new_chords += line + '\n'
            continue
        line = re.sub('(^|[\s])([A-G][#b]?)', 
            lambda x: x.group(1) + number_notes[(note_numbers[x.group(2)]+transpose_factor)%12],
            line)
        new_chords += line + '\n'
    return new_chords
