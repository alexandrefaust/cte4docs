class IntervaloConsumo:
    ID              = 'NULL'
    IDDadoAgua      = 'NULL'
    Intervalo       = 'NULL'
    ConsumoFaturado = 'NULL'
    CustoFaturado   = 'NULL'
    Taxa            = 'NULL'

    def __init__(self):
        pass

    def __str__(self):
        return f"INSERT INTO cte4docs.IntervaloConsumo ( \
            IDDadoAgua, \
            Intervalo, \
            ConsumoFaturado, \
            CustoFaturado, \
            Taxa \
        ) VALUES ( \
            '{self.IDDadoAgua}', \
            '{self.Intervalo}', \
            {self.ConsumoFaturado}, \
            {str(self.CustoFaturado).replace('.', '').replace(',', '.')}, \
            {self.Taxa} \
        )"
    
    def find(self):
        return f"SELECT * FROM cte4docs.IntervaloConsumo WHERE \
            IDDadoAgua = '{self.IDDadoAgua}' and \
            Intervalo = '{self.Intervalo}' and \
            ConsumoFaturado = {self.ConsumoFaturado} and \
            CustoFaturado = {str(self.CustoFaturado).replace('.', '').replace(',', '.')} and \
            Taxa = {self.Taxa}"