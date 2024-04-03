class DadoEnergia:
    ID                              = "NULL"
    IDEnergia                       = "NULL"
    Comentarios                     = "NULL"
    ComentariosAdicionais           = "NULL"    
    LocalData                       = "NULL"
    Periodo                         = "NULL"    
    DataInicio                      = "NULL"
    DataFinal                       = "NULL"
    Dias                            = "NULL"        
    Status                          = "Recebido"
    StatusChecagem                  = "NULL"    
    CustoMercadoLivreLongoPrazo     = "NULL"
    CompraMercadoLivreLongoPrazo    = "NULL"
    Vencimento                      = "NULL"
    IDDocumento                     = "NULL"
    NumeroNF                        = "NULL"
    BandeiraTarifaria               = "NULL"

    def __init__(self):
        pass

    def __str__(self):
        result = f"INSERT INTO cte4docs.DadoEnergia ( \
            IDEnergia, \
            Comentarios, \
            ComentariosAdicionais, \
            LocalData, \
            Periodo, \
            DataInicio, \
            DataFinal, \
            Dias, \
            Status, \
            StatusChecagem, \
            CustoMercadoLivreLongoPrazo, \
            CompraMercadoLivreLongoPrazo, \
            Vencimento, \
            IDDocumento, \
            NumeroNF, \
            BandeiraTarifaria) \
            VALUES \
            (\
                '{self.IDEnergia}', \
                '{self.Comentarios}', \
                '{self.ComentariosAdicionais}', \
                '{self.LocalData}', \
                '{self.Periodo}', "
        
        if 'NULL' not in self.DataInicio:
            result += f"'{self.DataInicio}',"
        else:
            result += f"NULL,"

        if 'NULL' not in self.DataFinal:
            result += f"'{self.DataFinal}',"
        else:
            result += f"NULL,"

        result += f"{self.Dias}, \
            '{self.Status}', \
            '{self.StatusChecagem}', \
            '{self.CustoMercadoLivreLongoPrazo}', \
            '{self.CompraMercadoLivreLongoPrazo}', \
            '{self.Vencimento}', \
            '{self.IDDocumento}', \
            '{self.NumeroNF}', \
            '{self.BandeiraTarifaria}' \
            );"
        
        return result