import funkcje

funkcje.dbconnanddotables()


start = ["0", "1", "2", "3", "4", "q"]
x = "1"
while True:
    funkcje.menu()
    x = input("Wybierz opcję: ")

    if x == "1":
     funkcje.dodajwpis()

    elif x == "2":
     funkcje.odczytwpisu()

    elif x == "3":
     funkcje.edycjawpisu()

    elif x == "q":
     print("Żegnam")
     exit()

    elif x == "add":
        funkcje.addcomment(Name='addname', Surname='addsurname', Comments='addcomments', Email='addemail')

    elif x == "sdb":
        funkcje.showcomments()

    elif x == "rm":
        funkcje.remove()


    else:
     print("Zła opcja, wybierz ponownie: ")
