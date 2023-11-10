from src import api4docs

class ItemGas:
    ID                  = 'NULL'
    IDDadoGas           = 'NULL'
    IDHistoricoGas      = 'NULL'
    Nome                = 'NULL' #Note
    Categoria           = 'NULL' #Type
    MedidorTipo         = 'NULL' #MeterType
    MedidorNumero       = 'NULL' #MeterNumber
    Tarifa              = 'NULL' #Rate
    Custo               = 'NULL' #Charge
    MedidaFaturada      = 'NULL' #Billed
    Medida              = 'NULL' #Measured
    Tributavel          = 'NULL' #Taxable


    def __init__(self):
        pass

    def __str__(self):
        retorno = f"INSERT INTO cte4docs.ItemGas ("
        retorno += f"IDDadoGas, "
        retorno += f"IDHistoricoGas, "
        retorno += f"Nome, "
        retorno += f"Categoria, "
        retorno += f"MedidorTipo, "
        retorno += f"MedidorNumero, "
        retorno += f"Tarifa, "
        retorno += f"Custo, "
        retorno += f"MedidaFaturada, "
        retorno += f"Medida, "
        retorno += f"Tributavel "
        retorno += f") VALUES ("
        retorno += f"{self.IDDadoGas}, "
        retorno += f"{self.IDHistoricoGas}, "
        retorno += f"'{self.Nome}', "
        retorno += f"'{self.Categoria}', "
        retorno += f"'{self.MedidorTipo}', "
        retorno += f"'{self.MedidorNumero}', "
        retorno += f"'{self.Tarifa}', "
        retorno += f"'{self.Custo}', "
        retorno += f"'{self.MedidaFaturada}', "
        retorno += f"'{self.Medida}', "
        retorno += f"'{self.Tributavel}');"
        
        return retorno
    
    def find(self):
        return f"SELECT * FROM cte4docs.ItemFaturado WHERE \
            IDDadoGas = '{self.IDDadoGas}' and \
            IDHistoricoGas = '{self.IDHistoricoGas}' and \
            Nome = {self.Nome} and \
            Categoria = {self.Categoria} and \
            Valor = {self.Valor}"
    


    def GetItens(self, item, dadoID, historic = False):
        if historic:
            self.IDHistoricoGas = dadoID
        else:
            self.IDDadoGas = dadoID        

        self.Nome = api4docs.GetAttribute(item, 'note')        
        if self.Nome == None or 'NULL' in self.Nome:
            self.Nome = api4docs.GetAttribute(item, 'name')

        self.Categoria = api4docs.GetAttribute(item, 'type')
        self.MedidorTipo = api4docs.GetAttribute(item, 'meterType')
        self.MedidorNumero = api4docs.GetAttribute(item, 'meterNumber')
        self.Tarifa = api4docs.GetAttribute(item, 'rate')
        self.Custo = api4docs.GetAttribute(item, 'value')
        if self.Custo == None or 'NULL' in str(self.Custo):
            self.Custo = api4docs.GetAttribute(item, 'charge')
        self.MedidaFaturada = api4docs.GetAttribute(item, 'billed')
        self.Medida = api4docs.GetAttribute(item, 'measured')
        self.Tributavel = api4docs.GetAttribute(item, 'taxable')

            

            