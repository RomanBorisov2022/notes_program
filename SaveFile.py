import json

def save_notes(notes, filename):
    with open(filename, 'w') as f:
        notes_dict = []
        for note in notes:
            notes_dict.append(note.to_dict())
        json.dump(notes_dict, f, indent=4)
        print("Заметки сохранены в файл:", filename)