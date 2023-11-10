import datetime
import traceback
import smtplib
import sys
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
lock = threading.Lock()

EMAIL_ADDRESS                       = "opsus@cte.com.br"
EMAIL_RECIPIENT                     = "opsus@cte.com.br"
EMAIL_CC                            = ""
EMAIL_PASSWORD                      = "cte@OS22"
EMAIL_SMTP_ADDRESS                  = "smtp-mail.outlook.com"
EMAIL_SMTP_PORT                     = "587"
EMAIL_MESSAGE                       = "Ocorreram os seguintes erros durante a execução:\n\n"
ENVIAR_EMAIL                        = False

####################################################################################################################
##### Método messageLog(message, sendErrorToEmail = False)
#####   - Faz o registro do erro em um arquivo conversor.log e no console, é enviado o e-mail caso pedido
#####   - Recebe como parâmetro a mensagem de erro e se o erro deve ser enviado por e-mail
####################################################################################################################
def messageLog(message, sendErrorToEmail = False):
    try:
        message = "[" + str(datetime.datetime.now()) + "] " + message
        lock.acquire()
        print(message)
        lock.release()
        if message.count("[ERROR]") >= 1:
            message = message + ": " + traceback.format_exc()
            message = message + "\n"
            logFile = open("./data/log/" + str(datetime.datetime.now()).replace("-", "")[:8] + ".log",'a')
            logFile.write(message)
            logFile.close()
        
        if sendErrorToEmail and message.count("[INFO]") < 1:
            global EMAIL_MESSAGE 
            EMAIL_MESSAGE = EMAIL_MESSAGE + message
    except:
        lock.acquire()
        print("[" + str(datetime.datetime.now()) + "] [ERROR] Message: " + traceback.format_exc())
        print("\n")
        lock.release()

def messageLogSL(message, sendErrorToEmail = False):
    try:
        message = "[" + str(datetime.datetime.now()) + "] " + message
        if message.count("[ERROR]") >= 1:
            message = message + ": " + traceback.format_exc()
            logFile = open("./data/log/" + str(datetime.datetime.now()).replace("-", "")[:8] + ".log",'a')
            logFile.write(message + "\n")
            logFile.close()
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        
        if sendErrorToEmail and message.count("[INFO]") < 1:
            global EMAIL_MESSAGE 
            EMAIL_MESSAGE = EMAIL_MESSAGE + message
    except:
        lock.acquire()
        print("[" + str(datetime.datetime.now()) + "] [ERROR] Message: " + traceback.format_exc())
        print("\n")
        lock.release()

def quickMessageLog(message):
    try:
        message = "[" + str(datetime.datetime.now()) + "] " + message
        lock.acquire()
        print(message, end="\r")
        lock.release()
    except:
        lock.acquire()
        print("[" + str(datetime.datetime.now()) + "] [ERROR] Message: " + traceback.format_exc())
        print("\n")
        lock.release()

####################################################################################################################
##### Método sendEmail(subject, message)
#####   - Envio de e-mail, é recebido como parâmetro o Assunto e a mensagem do e-mail
####################################################################################################################
def sendEmail(subject):
    try:
        global EMAIL_MESSAGE
        if ENVIAR_EMAIL and EMAIL_MESSAGE.count("\n") > 2:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_RECIPIENT
            msg['Cc'] = EMAIL_CC
            msg['Subject'] = subject
            
            msg.attach(MIMEText(EMAIL_MESSAGE, 'plain'))
            
            server = smtplib.SMTP(EMAIL_SMTP_ADDRESS + ': ' + EMAIL_SMTP_PORT)
            server.starttls()
            server.login(msg['From'], EMAIL_PASSWORD)
            server.sendmail(msg['From'], [EMAIL_RECIPIENT,EMAIL_CC], msg.as_string())
            server.quit()
            EMAIL_MESSAGE = "Ocorreram os seguintes erros durante a execução:\n\n"
            messageLog("[INFO] E-mail sended!")
    except:
        messageLog("[ERROR] Sending E-mail", ENVIAR_EMAIL)