import datetime


def get_notes_by_date(notes, date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    return [note for note in notes if note.created_time.date() == date or note.updated_time.date() == date]