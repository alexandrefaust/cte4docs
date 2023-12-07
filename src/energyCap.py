from src import messagelog as ml 
#import messagelog as ml 

import requests as req
import json

apikey          = "ZWNhcHxQcm9kdWN0aW9u.Y3RlfDEwMjR8MTAyNw==.OGJhNjU4M2MtYjFjNi00ZjM3LWE3MDEtZTkxOTdmN2YzNjE0"
address         = "https://app.energycap.com"
session         = req.Session()
headers         = { 
                    'ECI-ApiKey': apikey,
                    'Content-type':'application/json; charset=utf-8', 
                }
api             = {
                    "meter" : "/api/v3/meter?filter=accountCode like '{}'",
                    "bill": "/api/v3/bill?filter=beginDate equals '{}' and endDate equals '{}'",
                    "billPost": "/api/v3/bill"
                }

# Util
def getAPI(endpoint):
    try:
        result = session.get(address + endpoint, headers=headers)
    except Exception as e:
        ml.messageLog("[ERROR] Erro inesperado: " + str(e))
    return result

def postAPI(endpoint, jsonData):
    try:
        result = session.post(address + endpoint, data=jsonData, headers=headers)
    except Exception as e:
        ml.messageLog("[ERROR] Erro inesperado: " + str(e))
    return result
# Util

def GetBill(bill):
    totalCost = 0.0
    for b in bill['meters'][0]['bodyLines']:
        if 'Valor Total Fatura' in b['caption']:
            totalCost = b['cost']
            break
    response = getAPI(api["bill"].format(bill['beginDate'], bill['endDate']))
    return response.status_code != 200 or bool(response.json())



def CreateBill(dados, bodyLines):
    res = GetMeter(dados['Id'])
    if not any(res):
        ml.messageLog('[AVISO] Bill {} não encontrado em EnergyCap!'.format(dados['Id']))
        return {}
    dados['accountPeriod'] = None
    dados['manualEntry'] = False
    dados['statementDate'] = None
    dados['nextReading'] = None
    dados['controlCode'] = None
    dados['note'] = None
    dados['accountId'] = res['accountId']
    dados['meters'][0]['meterId'] = res['meterId']
    dados['accountBodyLines'] = []
    dados.pop('Id')

    for bl in bodyLines:
        dados['meters'][0]['bodyLines'].append(bl)

    return dados

    
    

#https://app.energycap.com/api/v3/meter?filter=accountCode equals 'MTE0014361'

def GetMeter(accountCode):
    response = getAPI(api["meter"].format(accountCode.replace('.', '').replace('-', '')))
    if not response.json():
        response = getAPI(api["meter"].format(accountCode.replace('.', '').replace('-', '')[:-5]))
    
    if not response.json():
        return {}
    
    meterId = response.json()[0]["meterId"]
    accountId = response.json()[0]['accounts'][0]['accountId']

    for r in response.json():
        if r['accounts'][0]['accountCode'].replace('.', '').replace('/', '').lstrip("0") in accountCode.replace('.', ''):
           accountId = r['accounts'][0]['accountId']


    return { 
        'meterId': meterId, 
        'accountId': accountId
        }

def Save(dados, bodyLines):
    if not CheckDados(dados):
        return
    
    bill = CreateBill(dados, bodyLines)
    if not any(bill) or GetBill(bill):
        return
    
    billJson = json.dumps(bill)

    result = postAPI(api['billPost'], billJson)

    logFile = open("./data/energyCap/datainserted.log",'a')
    logFile.write(result + " /n")
    logFile.close()

    if result.status_code != 200:
        ml.messageLog("[EnergyCap] Ocorreu um erro ao adicionar dado!")
    return result.status_code == 200


def CheckDados(dados):
    check = True
    if not dados['beginDate'] or dados['beginDate'] == 'NULL':
        ml.messageLog('Data inicial vazia! [id: {}]'.format(dados['Id']))
        check = False

    if not dados['endDate'] or dados['endDate'] == 'NULL':
        ml.messageLog('Data fim vazia! [id: {}]'.format(dados['Id']))
        check = False

    return check