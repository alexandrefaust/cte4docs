from src.models.ItemFaturado import ItemFaturado

class Historico:
    ID = ''
    IDDadoAgua = ''
    Data = ''
    Dias = ''
    ItensFaturados = []

    def __init__(self):
        pass

    def __str__(self):
        return f"INSERT INTO cte4docs.Historico ( \
            IDDadoAgua, \
            Data, \
            Dias \
        ) VALUES ( \
            '{self.IDDadoAgua}', \
            '{self.Data}', \
            '{self.Dias}' \
        )"