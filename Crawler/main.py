
from Company_Detail import Company_Stock

import mysql.connector as MySQL

import traceback

def getSymbols(Cursor):

    Symbols = []

    Cursor.execute("select Symbol from company_info")

    results = Cursor.fetchall()

    for result in results:

        Symbols.append(result[0])

    return Symbols

def insertData(Database, Symbol):

    Cursor = Database.cursor()

    sql = "insert into company_stock (Symbol, Date, Open, Close, High, Low) values (%s, %s, %s, %s, %s, %s)"

    try:

        Cursor.executemany(sql,Company_Stock(Symbol).getData())

    except Exception as e:

        print(Symbol+": ")
        traceback.print_exc()
            

    Database.commit()

def main():

    db = MySQL.connect(

        host = "localhost",
        user = "Company",
        passwd = "CompanyTest",
        database = "company"
        
    )

    Symbols = getSymbols(db.cursor())

    for Symbol in Symbols:

        insertData(db, Symbol)


main()
