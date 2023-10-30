from src.models.ItemFaturado import ItemFaturado

class HistoricoEnergia:
    ID = ''
    IDDadoEnergia = ''
    Data = ''
    Dias = ''
    Itens = []

    def __init__(self):
        pass

    def __str__(self):
        return f"INSERT INTO cte4docs.HistoricoEnergia ( \
            IDDadoEnergia, \
            Data, \
            Dias \
        ) VALUES ( \
            '{self.IDDadoEnergia}', \
            '{self.Data}', \
            '{self.Dias}' \
        )"