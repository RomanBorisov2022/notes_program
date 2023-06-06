
def delete_note_by_id(notes, id):
    note = next((note for note in notes if note.id == id), None)
    if note:
        notes.remove(note)
        print("Заметка успешно удалена!")
    else:
        print("Заметка с указанным ID не найдена")