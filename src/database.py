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
            self.CreateDatabase()
            ml.messageLog("Banco de dados conectado!")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("A tabela não existe")
            else:
                print(err)
            return False
        except:
            ml.messageLog("Não foi possível conectar")
            return False
        

    def CreateDatabase(self):
        if path.exists("src/database.sql"):
            f = open("src/database.sql", "r")
            self.mycursor.execute(f.read())
            f.close()
        else:
            ml.messageLog("Não foi possível verificar o banco de dados!")
            exit()


    def FindById(self, tabela, coluna, valor):
        self.mydb.reconnect()
        self.mycursor.execute('Select * from cte4docs.' + str(tabela) + ' where ' + str(coluna) + ' = \'' + str(valor) + '\'')
        result = self.mycursor.fetchone()
        return result
    
    def Find(self, busca):
        self.mydb.reconnect()
        self.mycursor.execute(busca)
        result = self.mycursor.fetchone()
        return result == None

    def SaveData(self, data):
        try:
            self.mydb.reconnect()
            self.mycursor.execute(str(data))
            self.mydb.commit()
            return self.mycursor.lastrowid
        except:
            ml.messageLog('[ERROR] Não foi possível salvar os seguintes dados: \n' + str(data))
            return 0

    def IsNotConnected(self):
        if self.mydb != "":
            self.mydb.reconnect()
        return self.mydb == "" or not self.mydb.is_connected()
