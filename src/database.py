import mysql.connector
import time
from src import messagelog as ml 
from os import path
from mysql.connector import errorcode

class Database:

    BD_ENDERECO      = "127.0.0.1"
    BD_USUARIO       = "root"
    BD_SENHA         = "123456"
    BD_NOME          = "cte4docs"

    mydb             = ''
    mycursor         = ''

    def CheckDatabase(self):
        self.Connect()
        if self.mydb.is_connected():
            self.CreateDatabase()
            self.UpdateDatabase()

    def Connect(self):
        try :
            self.mydb = mysql.connector.connect(
                host        = self.BD_ENDERECO,
                user        = self.BD_USUARIO,
                password    = self.BD_SENHA)
            
            self.mydb.autocommit = True
            self.mycursor = self.mydb.cursor()
            self.mydb.is_connected()

            return self.mycursor
            
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
            self.mycursor.execute(f.read(), multi=True)
            f.close()
        else:
            ml.messageLog("Não foi possível verificar o banco de dados!")
            exit()
        
        self.close()
        
    def UpdateDatabase(self):
        self.open()
        i = 2
        while path.exists("src/db/dbup" + str(i) + ".sql"):
            if self.FindById('APIversion', 'ID', i) == None and not self.IsNotConnected():
                ml.messageLog("Updating database with dbup" + str(i) + ".sql...")
                f = open("src/db/dbup" + str(i) + ".sql", "r")
                self.open()
                self.mycursor.execute(f.read(), multi=True)
                f.close()
            else:
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
            self.mycursor.execute(str(data), multi=True)
            lastID = 0
            if returnLastID:
                lastID = self.mycursor._last_insert_id
            self.close()
            return lastID
        except Exception as e:
            ml.messageLog('[ERROR] Não foi possível salvar os dados, motivo: {}'.format(str(e)))
            return 0

    def IsNotConnected(self):
        if self.mydb != "":
            self.mydb.reconnect()
        return self.mydb == "" or not self.mydb.is_connected()

    def close(self):
        self.mycursor.close()
        self.mydb.close()

    def open(self):
        self.mydb.connect()
        self.mycursor = self.mydb.cursor()