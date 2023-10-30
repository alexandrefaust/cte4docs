class DadoGas:
    ID = "NULL"
    IDGas = "NULL"
    Comentarios = "NULL"
    ComentariosAdicionais = "NULL"
    
    Periodo = "NULL"
    
    DataInicio = "NULL"
    DataFinal = "NULL"
    Dias = "NULL"
        
    Status = "Recebido"
    StatusChecagem = "NULL"

    NumeroNF = "NULL"
    Fornecedor = "NULL"
    ClasseTarifaria = "NULL"
    ValorTotal = "NULL"

    Vencimento = "NULL"
    IDDocumento = "NULL"

    def __init__(self):
        pass

    def __str__(self):
        result = f"INSERT INTO cte4docs.DadoGas ( \
            IDGas, \
            Comentarios, \
            ComentariosAdicionais, \
            DataInicio, \
            DataFinal, \
            Dias, \
            Status, \
            StatusChecagem, \
            Vencimento, \
            NumeroNF, \
            Fornecedor, \
            ClasseTarifaria, \
            ValorTotal, \
            IDDocumento) \
            VALUES \
            (\
                '{self.IDGas}', \
                '{self.Comentarios}', \
                '{self.ComentariosAdicionais}', "
        
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
            '{self.Vencimento}', \
            '{self.NumeroNF}', \
            '{self.Fornecedor}', \
            '{self.ClasseTarifaria}', \
            '{self.ValorTotal}', \
            '{self.IDDocumento}' \
            );"
        
        return result