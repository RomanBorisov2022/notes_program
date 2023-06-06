
from NotesClass import Note


def add_note(notes):
    id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите содержание заметки: ")
    note = Note(id, title, body)
    notes.append(note)
    print("Новая заметка успешно добавлена!")