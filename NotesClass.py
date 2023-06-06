import datetime


class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_time = datetime.datetime.now()
        self.updated_time = self.created_time

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_time = datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_time": str(self.created_time),
            "updated_time": str(self.updated_time)
        }
    
