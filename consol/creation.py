import note


def createNote(numder):
    title = checkLength(input("Введите Название заметки: "), numder)
    text = checkLength(input("Введите Описание заметки: "), numder)
    return note.note(title=title, text=text)


def checkLength(text, n):
    while len(text) <= n:
        print(f"Минимально кол-во символов {n}\n")
        text = input("Текст сюда пиши: ")
    else:
        return text


def writeFile(array, mode):
    file = open("note.csv", mode="w", encoding="utf-8")
    file.seek(0)
    file.close()
    file = open("note.csv", mode=mode, encoding="utf-8")
    for Note in array:
        file.write(note.note.toString(Note))
        file.write("\n")
    file.close


def readFile():
    try:
        array = []
        file = open("note.csv", "r", encoding="utf-8")
        Note = file.read().strip().split("\n")
        for n in Note:
            split_n = n.split(";")
            Notes = note.note(
                id=split_n[0], title=split_n[1], text=split_n[2], date=split_n[3]
            )
            array.append(Notes)
    except Exception:
        print("69")
    finally:
        return array


# кол-во символов
numder = 3


def addnote():
    Note = createNote(numder)
    array = readFile()
    for Notes in array:
        if note.note.getid(Note) == note.note.getid(Notes):
            note.note.setid(Note)
    array.append(Note)
    writeFile(array, "a")
    print("создание")


def show(text):
    log = True
    array = readFile()
    if text == "4":
        date = input("Введите дату в формате 15.08.1096: ")
    for Note in array:
        if text == "1":
            log = False
            print(note.note.mapNote(Note))
        if text == "5":
            log = False
            print("id: " + note.note.getid(Note))
        if text == "4":
            log = False
            if date in note.note.getdate(Note):
                print(note.note.mapNote(Note))
    if log == True:
        print("заметок нет")


def refactor(text):
    id = input("Введите id необходимой заметки: ")
    array = readFile()
    log = True
    for Notes in array:
        if id == note.note.getid(Notes):
            log = False
            if text == "2":
                Note = createNote(numder)
                note.note.settitle(Notes, Note.gettitle())
                note.note.settext(Notes, Note.gettext())
                note.note.setdate(Notes)
                print("Редактирование")
            if text == "3":
                array.remove(Notes)
                print("Удаление")
            if text == "6":
                print(note.note.mapNote(Notes))
    if log == True:
        print("проверь id")
    writeFile(array, "a")
