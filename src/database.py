import mysql.connector
from src import messagelog as ml 
from os import path
from mysql.connector import errorcode

class Database:

    BD_ENDERECO      = "localhost"
    BD_USUARIO       = "root"
    BD_SENHA         = "123456"
    BD_NOME          = "cte4docs"

    mydb             = ''
    mycursor         = ''

    def Connect(self):
        try :
            self.mydb = mysql.connector.connect(
                host        = self.BD_ENDERECO,
                user        = self.BD_USUARIO,
                password    = self.BD_SENHA)
            self.mycursor = self.mydb.cursor()
            self.mydb.autocommit = True
            self.CreateDatabase()
            ml.messageLog("Banco de dados conectado!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("A tabela não existe")
            else:
                print(err)
            exit()
        except Exception as e:
            ml.messageLog("Não foi possível conectar, motivo: " + str(e))
            exit()
        

    def CreateDatabase(self):
        self.open()
        if path.exists("src/db/database.sql"):
            f = open("src/db/database.sql", "r")
            self.mycursor.execute(f.read())
            f.close()
        else:
            ml.messageLog("Não foi possível verificar o banco de dados!")
            exit()
        
        self.close()
        self.open()

        i = 1
        while path.exists("src/db/dbup" + str(i) + ".sql"):
            ml.messageLog("Updating database...")
            f = open("src/db/dbup" + str(i) + ".sql", "r")
            self.mycursor.execute(f.read())
            f.close()
            i += 1

        self.close()
        


    def FindById(self, tabela, coluna, valor):
        self.open()
        self.mycursor.execute('Select * from cte4docs.' + str(tabela) + ' where ' + str(coluna) + ' = \'' + str(valor) + '\'')
        result = self.mycursor.fetchone()
        self.close()
        return result
    
    def Find(self, busca):
        self.open()
        self.mycursor.execute(busca)
        result = self.mycursor.fetchone()
        self.close()
        return result == None

    def SaveData(self, data, returnLastID = False):
        try:
            self.open()
            self.mydb.reset_session()
            self.mycursor.execute(str(data))
            lastID = 0
            if returnLastID:
                lastID = self.mycursor._last_insert_id
            self.close()
            return lastID
        except Exception as e:
            ml.messageLog('[ERROR] Não foi possível salvar os dados, motivo: ' + str(e))
            return 0

    def IsNotConnected(self):
        if self.mydb != "":
            self.mydb.reconnect()
        return self.mydb == "" or not self.mydb.is_connected()

    def close(self):
        self.mycursor.close()
        self.mydb.disconnect()

    def open(self):
        self.mydb.connect()
        self.mycursor = self.mydb.cursor()