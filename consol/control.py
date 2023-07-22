import creation as cr 

def run():
    choic = ''
    while True:
        print("\n"
            "Возможные действия: \n"
              "\n"
              "1 - создание заметки\n"
              "2 - просмотр заметок\n"
              "3 - изменение заметок\n"
              "4 - удалить заметку\n"
              "5 - выборка заметок по дате\n"
              "6 - по id\n"
              "7 - выход\n")
        choic = input("Введите действие > ")
        if choic == '1':
            cr.addnote()
        elif choic == '2':
            cr.show('1')
        elif choic == '3':
            cr.show('1')
            cr.refactor('2')
        elif choic == '4':
            cr.show('1')
            cr.refactor('3')
        elif choic == '5':
            cr.show('4')
        elif choic == '6':
            cr.show('5')
            cr.refactor('6')
        else:
            print("dd")
            break
        