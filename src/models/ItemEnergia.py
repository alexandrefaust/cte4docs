from src import api4docs

class ItemEnergia:
    ID                  = 'NULL'
    IDDadoEnergia       = 'NULL'
    IDHistoricoEnergia  = 'NULL'
    Nome                = 'NULL' #kind
    Categoria           = 'NULL' #Type
    Periodo             = 'NULL' #Period
    Tarifa              = 'NULL' #Rate
    Custo               = 'NULL' #Charge
    MedidaFaturada      = 'NULL' #Billed
    Contratada          = 'NULL' #Contract
    Medida              = 'NULL' #Measured


    def __init__(self):
        pass

    def __str__(self):
        retorno = f"INSERT INTO cte4docs.ItemEnergia ("
        retorno += f"IDDadoEnergia, "
        retorno += f"IDHistoricoEnergia, "
        retorno += f"Nome, "
        retorno += f"Categoria, "
        retorno += f"Periodo, "
        retorno += f"Tarifa, "
        retorno += f"Custo, "
        retorno += f"MedidaFaturada, "
        retorno += f"Contratada, "
        retorno += f"Medida "
        retorno += f") VALUES ("
        retorno += f"{self.IDDadoEnergia}, "
        retorno += f"{self.IDHistoricoEnergia}, "
        retorno += f"'{self.Nome}', "
        retorno += f"'{self.Categoria}', "
        retorno += f"'{self.Periodo}', "
        retorno += f"'{self.Tarifa}', "
        retorno += f"'{self.Custo}', "
        retorno += f"'{self.MedidaFaturada}', "
        retorno += f"'{self.Contratada}', "
        retorno += f"'{self.Medida}');"
        
        return retorno
    
    def find(self):
        return f"SELECT * FROM cte4docs.ItemFaturado WHERE \
            IDDadoEnergia = '{self.IDDadoEnergia}' and \
            IDHistoricoEnergia = '{self.IDHistoricoEnergia}' and \
            Nome = {self.Nome} and \
            Categoria = {self.Categoria} and \
            Valor = {self.Valor}"
    


    def GetItens(self, item, dadoID, historic = False):
        if historic:
            self.IDHistoricoEnergia = dadoID
        else:
            self.IDDadoEnergia = dadoID

        self.Nome = api4docs.GetAttribute(item, 'kind')
        if self.Nome == None or 'NULL' in self.Nome:
            self.Nome = api4docs.GetAttribute(item, 'name')
            if self.Nome == None or 'NULL' in self.Nome:
                self.Nome == 'NULL'

        self.Medida = api4docs.GetAttribute(item, 'billed')
        if self.Medida == None or self.Medida == 0:
            self.Medida = api4docs.GetAttribute(item, 'measured')
            if self.Medida == None:
                self.Medida == 0

        self.Categoria = api4docs.GetAttribute(item, 'type')
        self.Periodo = api4docs.GetAttribute(item, 'period')
        self.Tarifa = api4docs.GetAttribute(item, 'rate')
        self.Custo = api4docs.GetAttribute(item, 'charge')
        self.Contratada = api4docs.GetAttribute(item, 'contract')