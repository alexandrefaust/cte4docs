from src.models import Enum

class ItemFaturado:
    ID          = 'NULL'
    IDDadoAgua  = 'NULL'
    IDHistorico = 'NULL'
    Nome        = 'NULL'
    Categoria   = 'NULL'
    Valor       = 'NULL'

    def __init__(self):
        pass

    def __str__(self):
        retorno = f"INSERT INTO cte4docs.ItemFaturado ("
        retorno += f"IDDadoAgua, "
        retorno += f"IDHistorico, "
        retorno += f"Nome, "
        retorno += f"Categoria, "
        retorno += f"Valor "
        retorno += f") VALUES ("        
        retorno += f"{self.IDDadoAgua}, "                                    
        retorno += f"{self.IDHistorico}, "
        retorno += f"'{self.Nome}', "
        retorno += f"'{self.Categoria}', "
        retorno += f"{self.Valor})"
        
        return retorno
    
    def find(self):
        return f"SELECT * FROM cte4docs.ItemFaturado WHERE \
            IDDadoAgua = '{self.IDDadoAgua}' and \
            IDHistorico = '{self.IDHistorico}' and \
            Nome = {self.Nome} and \
            Categoria = {self.Categoria} and \
            Valor = {self.Valor}"
    
    def toEnergyCap(self):
        if not 'NULL' in self.Nome or not 'NULL' in self.Categoria or not 'NULL' in str(self.Valor):
            result = {}

            if "water" in self.Categoria:
                result = {
                    "observationTypeId": Enum.ObservationType.INFO_COST.value, 
                    "valueUnitId": None,
                    "value": None,
                    "costUnitId": Enum.CostUnit.BRL.value,
                    "cost": self.Valor,
                    "caption": "Valor Total Água"
                }
            elif "sewer" in self.Categoria:
                result = {
                    "observationTypeId": Enum.ObservationType.INFO_COST.value,
                    "valueUnitId": None,
                    "value": None,
                    "costUnitId": Enum.CostUnit.BRL.value,
                    "cost": self.Valor,
                    "caption": "Valor Total Esgoto"
                }
            elif "other" in self.Categoria:
                observationID = Enum.ObservationType.INFO_COST.value
                caption = "Valor Outros Débitos"

                if "Fator K" in self.Nome:
                    caption = "Fator K"
                elif "Serviços 1" in self.Nome:
                    caption = "Valor Serviços"
                elif "Multa" in self.Nome:
                    caption = "Valor Multas"
                elif "Crédito" in self.Nome:
                    caption = "Valor Créditos e Devoluções"
                    

                result = {
                    "observationTypeId": observationID,
                    "valueUnitId": None,
                    "value": None,
                    "costUnitId": Enum.CostUnit.BRL.value,
                    "cost": self.Valor,
                    "caption": caption
                }
            return result
            