from AddNote import add_note
from ChangeNote import edit_note_by_id
from DeleteNote import delete_note_by_id
from ReadFile import load_notes
from SaveFile import save_notes
from SearchNoteByDate import get_notes_by_date
from View import print_notes


def main():
    NOTES_FILENAME = "notes.json"
    try:
        notes = load_notes(NOTES_FILENAME)
    except:
        notes = []

    while True:
        print("=" * 30)
        print("Выберите действие:")
        print("1. Просмотреть все заметки")
        print("2. Просмотреть заметки по дате")
        print("3. Добавить заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")
        choice = input("Введите номер действия: ")
        print("=" * 30)

        if choice == "1":
            if len(notes) == 0:
                print("Нет ни одной заметки")
            else:
                print_notes(notes)

        elif choice == "2":
            date_str = input("Введите дату в формате YYYY-MM-DD: ")
            selected_notes = get_notes_by_date(notes, date_str)
            if len(selected_notes) == 0:
                print("Нет заметок по указанной дате")
            else:
                print_notes(selected_notes)

        elif choice == "3":
            add_note(notes)

        elif choice == "4":
            id = int(input("Введите ID заметки для редактирования: "))
            edit_note_by_id(notes, id)

        elif choice == "5":
            id = int(input("Введите ID заметки для удаления: "))
            delete_note_by_id(notes, id)

        elif choice == "6":
            save_notes(notes, NOTES_FILENAME)
            print("До свидания!")
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")
