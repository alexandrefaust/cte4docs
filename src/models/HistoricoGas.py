from src.models.ItemFaturado import ItemFaturado

class HistoricoGas:
    ID = ''
    IDDadoGas = ''
    Data = ''
    Itens = []

    def __init__(self):
        pass

    def __str__(self):
        return f"INSERT INTO cte4docs.HistoricoGas ( \
            IDDadoGas, \
            Data \
        ) VALUES ( \
            '{self.IDDadoGas}', \
            '{self.Data}' \
        )"