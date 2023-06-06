

def edit_note_by_id(notes, id):
    note = next((note for note in notes if note.id == id), None)
    if note:
        new_title = input("Введите новый заголовок заметки: ")
        new_body = input("Введите новое содержание заметки: ")
        note.update(new_title, new_body)
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка с указанным ID не найдена")