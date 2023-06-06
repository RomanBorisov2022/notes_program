
def print_notes(notes):
    for note in notes:
        print(f"ID: {note.id}")
        print(f"Заголовок: {note.title}")
        print(f"Тело заметки: {note.body}")
        print(f"Дата создания: {note.created_time}")
        print(f"Дата обновления: {note.updated_time}")
        print("")