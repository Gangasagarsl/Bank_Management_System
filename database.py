# Database management Banking
import mysql.connector as sql
mydb=sql.connect(
    host="localhost",
    user="root",
    passwd="Ganga@#123",
    database="bank"
)
cursor=mydb.cursor()
def createcustomertable():
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers
               (username VARCHAR(20),
               password VARCHAR(20),
               name VARCHAR(20),
               age INTEGER,
               city VARCHAR(20),
               account_number INTEGER,
               status BOOLEAN)
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()

