import requests as req
import time

from requests import Request, Session
from src import messagelog as ml 
from src.models.DadoAgua import DadoAgua
from src.models.ItemFaturado import ItemFaturado
from src.models.IntervaloConsumo import IntervaloConsumo
from src.models.Historico import Historico
from src.database import Database 

login           = ''
senha           = ''
quantidade      = 0
tempoRotina     = 10
mysql_endereco  = ''
mysql_usuario   = ''
mysql_senha     = ''

domain          = 'https://console.4docs.cloud'
urllogin        = '/login'
urlrequest      = '/requests/js?customer_id=37&limit=' + str(quantidade) + '&status=SUCCESS'
urljson         = '/json/'
values          = {'email': login, 'password': senha}

session         = req.Session()
cookie          = {}



def init():
    global db, urlrequest, values 
    urlrequest = '/requests/js?customer_id=37&limit=' + str(quantidade) + '&status=SUCCESS'
    values          = {'email': login, 'password': senha}
    db = Database()
    db.BD_ENDERECO  = mysql_endereco
    db.BD_USUARIO   = mysql_usuario
    db.BD_SENHA     = mysql_senha
    db.Connect()
    while True:
      try:
        GetData()
      except:
        ml.messageLog("[ERROR] Ocorreu um erro desconhecido!")  
      ml.messageLog("Rotina finalizada! Aguardando " + str(tempoRotina) + " segundos para nova rotina!")
      time.sleep(tempoRotina)
      
# ____________________________________________________ #

def IsNotAuthenticated():
  try:
    response = session.post(domain + urljson, cookies=cookie)
    return len(cookie) == 0 or "You must login first." in response.text
  except: 
    return True

def Connect():
    while db.IsNotConnected():
      ml.messageLog("Banco de dados não conectado! Verifique os dados de conexão e se o banco de dados está ativo!")
      ml.messageLog("Nova tentativa em 10 segundos...")
      time.sleep(10)
      db.Connect()
    global cookie
    try:
      if IsNotAuthenticated():
        session = req.Session()
        response = session.post(domain + urllogin, data=values)
        cookiesdict = session.cookies.get_dict()
        if cookiesdict:
          cookiesessionname = next(iter(cookiesdict))
          cookiesessionkey = cookiesdict[cookiesessionname]
          cookie = {cookiesessionname: cookiesessionkey}
          ml.messageLog("Autenticado no 4docs!")
        else :
          ml.messageLog("Não foi possível autenticar no 4docs!")
          ml.messageLog("Verifique o estado atual da API ou endereço de acesso!")
          return False
      else: 
        ml.messageLog("Autenticado no 4docs!")
    except:
      ml.messageLog("[ERROR] Não foi possível autenticar no 4docs!")  
    return True

def GetData():
  if Connect():
    if db.IsNotConnected():
      exit()
    response = GetRequest()
    qtde = 0
    for x in response:
      try:
        ml.quickMessageLog(str(qtde) + ' IDs verificados! - Verificando ID: ' + str(x['id']))
        jsonpath = session.get(domain + urljson + str(x['id']) + '.json', cookies=cookie).json()   

        if 'success' in jsonpath and 'message' in jsonpath and 'Extraction failed' in jsonpath['message']:
          print(jsonpath['message'])
        else:
          if ('pipeline' in jsonpath and 'water' in jsonpath['pipeline']) or \
          ('items' in jsonpath and 'water' in str(jsonpath['items'])):
            WaterData(jsonpath, str(x['id']))
          # elif 'items' in jsonpath and 'energy' in str(jsonpath['items']):
            # EnergyData(jsonpath)
      except:
        ml.messageLog("[ERROR] Erro ao tentar acessar o endereço: " + str(jsonpath))
      qtde += 1
    ml.messageLog(str(qtde) + ' IDs verificados!                                       ')
      
def GetRequest():
   return session.get(domain + urlrequest, cookies=cookie).json()['rows']


def WaterData(jsonpath, IDDocumento):
  waterData = DadoAgua()
  waterData.IDDocumento         = IDDocumento
  waterData.IDAgua              = GetAttribute(jsonpath, 'locationNumber')
  waterData.Custo               = GetAttribute(jsonpath, 'total')
  waterData.LeituraAtual        = GetAttribute(jsonpath, 'currentMeterReading')
  waterData.LeituraAnterior     = GetAttribute(jsonpath, 'previousMeterReading')
  waterData.ConsumoFaturado     = GetAttribute(jsonpath, 'billedVolume')
  waterData.ConsumoEfetivo      = GetAttribute(jsonpath, 'measuredVolume')
  waterData.Dias                = GetAttribute(jsonpath, 'days')
  waterData.Vencimento          = GetAttribute(jsonpath, 'dates', 'due')
  waterData.Periodo             = GetAttribute(jsonpath, 'dates', 'month')
  waterData.DataInicio          = GetAttribute(jsonpath, 'dates', 'reading', 'previous')
  waterData.DataFinal           = GetAttribute(jsonpath, 'dates', 'reading', 'current')
  waterData.ICMS                = GetAttribute(jsonpath, 'icms', 'taxable')
  waterData.ICMSTaxa            = GetAttribute(jsonpath, 'icms', 'rate')
  waterData.ICMSValorFinal      = GetAttribute(jsonpath, 'icms', 'value')
  waterData.PIS                 = GetAttribute(jsonpath, 'pis', 'taxable')
  waterData.PISTaxa             = GetAttribute(jsonpath, 'pis', 'rate')
  waterData.PISValorFinal       = GetAttribute(jsonpath, 'pis', 'value')
  waterData.COFINS              = GetAttribute(jsonpath, 'cofins', 'taxable')
  waterData.COFINSTaxa          = GetAttribute(jsonpath, 'cofins', 'rate')
  waterData.COFINSValorFinal    = GetAttribute(jsonpath, 'cofins', 'value')
  waterData.PISCOFINS           = GetAttribute(jsonpath, 'pis_cofins', 'taxable')
  waterData.PISCOFINSTaxa       = GetAttribute(jsonpath, 'pis_cofins', 'rate')
  waterData.PISCOFINSValorFinal = GetAttribute(jsonpath, 'pis_cofins', 'value')
  waterData.TipoFaturamento     = GetAttribute(jsonpath, 'billingType')
  
  result = db.FindById('DadoAgua', 'IDDocumento', waterData.IDDocumento)
  if result == None:
    waterData.ID = db.SaveData(waterData)
    if waterData.ID == 0:
      return
  else:
    return
  
  waterDataID = waterData.ID

  GetItensFaturados(GetAttribute(jsonpath, 'items'), waterDataID)

  ranges = GetAttribute(jsonpath, 'ranges')
  if ranges != 'NULL':
    for item in ranges:
      intervalo = IntervaloConsumo()
      intervalo.IDDadoAgua = waterDataID
      intervalo.Intervalo = GetAttribute(item, 'range')
      intervalo.ConsumoFaturado = GetAttribute(item, 'billed')
      intervalo.CustoFaturado = GetAttribute(item, 'value')
      intervalo.Taxa = GetAttribute(item, 'economies')
      if intervalo.Taxa == 'NULL':
        intervalo.Taxa = GetAttribute(item, 'rate')
      db.SaveData(intervalo)

  historicos = GetAttribute(jsonpath, 'history')
  if historicos != 'NULL':
    for h in historicos:
      historico = Historico()
      historico.IDDadoAgua = waterDataID
      historico.Data = GetAttribute(historicos[h], 'month')
      historico.Dias = GetAttribute(historicos[h], 'days')
      itens = GetAttribute(historicos[h], 'items')
      historicoID = db.SaveData(historico)
      historico.ItensFaturados = GetItensFaturados(itens, historicoID, True)



  
def GetItensFaturados(jsonpath, dadoID, historic = False):
  for item in jsonpath:
    itemFaturado = ItemFaturado()
    if historic:
      itemFaturado.IDHistorico = dadoID
    else:
      itemFaturado.IDDadoAgua = dadoID
    itemFaturado.Categoria = GetAttribute(item, 'type')
    itemFaturado.Nome = GetAttribute(item, 'kind')
    if itemFaturado.Nome == None or 'NULL' in itemFaturado.Nome:
      itemFaturado.Nome = GetAttribute(item, 'text')
    itemFaturado.Valor = GetAttribute(item, 'charge')
    db.SaveData(itemFaturado)

def GetAttribute(jsonpath, attribute, attribute2 = "", attribute3 = ""):
  if attribute in jsonpath \
    and attribute2 in str(jsonpath[attribute]) \
    and attribute3 != "" \
    and attribute3 in str(jsonpath[attribute][attribute2]):
        return jsonpath[attribute][attribute2][attribute3]
  
  if attribute2 != "" \
    and attribute3 == "" \
    and attribute in jsonpath \
    and attribute2 in jsonpath[attribute]:
      return jsonpath[attribute][attribute2]
  
  if attribute in jsonpath and attribute2 == "":
    return jsonpath[attribute]

  return 'NULL'

