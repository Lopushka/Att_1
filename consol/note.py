from datetime import datetime
import uuid


class note:
    def __init__(
        self,
        id=str(uuid.uuid1())[0:3],
        title="текст",
        text="текст",
        date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")),
    ):
        self.id = id
        self.title = title
        self.text = text
        self.date = date

    def getid(note):
        return note.id

    def gettitle(note):
        return note.title

    def gettext(note):
        return note.text

    def getdate(note):
        return note.date

    def setid(note):
        note.id = str(uuid.uuid1())[0:3]

    def settitle(note, title):
        note.title = title

    def settext(note, text):
        note.text = text

    def setdate(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def toString(note):
        return note.id + ";" + note.title + ";" + note.text + ";" + note.date

    def mapNote(note):
        return (
            "\nId: "
            + note.id
            + "\n"
            + "Название: "
            + note.title
            + "\n"
            + "Описание: "
            + note.text
            + "\n"
            + "Дата создания: "
            + note.date
        )
