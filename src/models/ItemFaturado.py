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