import datetime
import mysql.connector as mariadb
data = datetime.datetime.now()
print (data)

#   Połączenie i tworzenie tabel
def dbconnanddotables():

    db = mariadb.connect(host="juchnicki.pl",  # your host, usually localhost
                         user="python",  # your username
                         passwd="testpy",  # your password
                         db="python")  # name of the data base

    cursor = db.cursor()

#    cursor.execute(""
 #                   "DROP TABLE IF EXISTS baza;"
  #                 "")
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS baza
            (
                    NrID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    Name varchar(255),
                    Surname varchar(255),
                    Comments varchar (255),
                    Email varchar(255)
            )

                    """)

    # disconnect from server
    db.close()

#   dodawanie wpisow do tabeli
def addcomment(Name, Surname, Comments, Email):
    Name = input("Podaj imie: ")
    Surname = input("Podaj Nazwisko: ")
    Comments = input("Wytaź swoją opinię: ")
    Email = input("Podaj e-mail: ")


    db = mariadb.connect(host="juchnicki.pl",  # your host, usually localhost
                         user="python",  # your username
                         passwd="testpy",  # your password
                         db="python")  # name of the data base

    cursor = db.cursor()

    sql = "INSERT INTO baza(Name, Surname, Comments, Email) \
           VALUES ('%s', '%s', '%s', '%s' )" % \
          (
            Name,
            Surname,
            Comments,
            Email
           )
    try:

        cursor.execute(sql)
        # tu dodaje
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def remove():
    db = mariadb.connect(host="juchnicki.pl",  # your host, usually localhost
                         user="python",  # your username
                         passwd="testpy",  # your password
                         db="python")  # name of the data base
    cursor = db.cursor()
    sql = "SELECT * FROM baza"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            NrID = row[0]
            Name = row[1]
            Surname = row[2]
            Comments = row[3]
            Email = row[4]
            # pokaz dane z bazy
            print("Pozycja na liście: %d" % (NrID))
 #           print(NrID)
            print("Name: %s | Surname: %s | Email: %s " % (Name, Surname, Email ))
            print("Comments: %s" % (Comments))
            print("  ")


    except:
            print("(t)ErRoR22222")

    PosID = results
    for IDposition in PosID:
       # print(IDposition[0])
        IDposOK = IDposition[0]
        print(IDposOK)


    nrid = str(input('Podaj numer z numerem wpisu do usunięcia: '))
    sql = 'DELETE FROM baza WHERE NrID='+ nrid
    try:
        if nrid in IDposOK:
         print("Wpis o numerze: " + nrid, "został usunięty"),
         cursor.execute(sql)
         db.commit()
    except:
         print("(T)ErRoR")
    db.close()

#   pokaz komentarze
def showcomments():
    db = mariadb.connect(host="juchnicki.pl",  # your host, usually localhost
                         user="python",  # your username
                         passwd="testpy",  # your password
                         db="python")  # name of the data base


    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM baza"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            NrID = row[0]
            Name = row[1]
            Surname = row[2]
            Comments = row[3]
            Email = row[4]
            # pokaz dane z bazy
            print("Pozycja na liście: %d" % (NrID))
            #           print(NrID)
            print("Name: %s | Surname: %s | Email: %s " % (Name, Surname, Email))
            print("Comments: %s" % (Comments))
    except:
            print("Nie tyra")

    # disconnect from server
    db.close()

#   MENU
def menu():
    print("Co chcesz zrobić?")
    print("Jeśli dodać wpis do księgi, wpisz - add")
    print("Jeśli chcesz odczytać wpisy, wpisz - sdb")
    print("Jeśli chcesz edytować lub usunąć wpis, wpisz - rm")
#    print("Wyświetl menu - 0")
    print("Jeśli chcesz Wyjść, wpisz - q")


#   NOWY WPIS
def dodajwpis():
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj Nazwisko: ")
    uwagi = input("Wytaź swoją opinię: ")
    email = input("Podaj e-mail: ")
    print("Dziękuje", imie, nazwisko, "za dodanie wpisu w dniu:", (data))
    print("Bye")
    daneimie = ["Imię: ", imie, '\n']
    danenazwisko = ["Nazwisko: ", nazwisko, '\n']
    daneuwagi = ["Uwagi: ", uwagi, '\n']
    daneemail = ["E-mail: ", email, '\n']

    print(imie)
#   danedaty = [data]
    print(data)
    plikzdanymi = open('plikzdanymi.txt', 'a+')
    plikzdanymi.writelines(daneimie)
    plikzdanymi.writelines(danenazwisko)
    plikzdanymi.writelines(daneuwagi)
    plikzdanymi.writelines(daneemail)
    with open("plikzdanymi.txt", mode='a+') as file:
        file.write('Adres pliku %s z dnia %s.\n' %
            (plikzdanymi, datetime.datetime.now()))
    plikzdanymi.writelines('\n')
    plikzdanymi.close()


#   ODCZYTY PLIKU
def odczytwpisu():
    odczytksiegi = open('plikzdanymi.txt').read()
    print(odczytksiegi)

#   EDYCJA PLIKU
def edycjawpisu():
    text = open('plikzdanymi.txt').read()
    print(text)
    x = input("Podaj słowo do zamiany: ")
    y = input("Na jakie słowo zamienić: ")
    edycjaksiegi = open('plikzdanymi.txt').readlines()
    edytujna = open('plikzdanymi.txt', 'w')
    for z in edycjaksiegi:
     edytujna.write(z.replace((x), (y)))
    edytujna.close()

