import datetime
import json

from NotesClass import Note

def load_notes(filename):
    try:
        with open(filename, 'r') as f:
            notes_dict = json.load(f)
            notes = []
            for note_dict in notes_dict:
                note = Note(note_dict['id'], note_dict['title'], note_dict['body'])
                note.created_time = datetime.datetime.strptime(note_dict['created_time'], '%Y-%m-%d %H:%M:%S.%f')
                note.updated_time = datetime.datetime.strptime(note_dict['updated_time'], '%Y-%m-%d %H:%M:%S.%f')
                notes.append(note)
            print("Заметки загружены из файла:", filename)
            return notes
    except FileNotFoundError:
        print("Файл не найден")