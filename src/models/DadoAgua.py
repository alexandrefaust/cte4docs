class DadoAgua:
    ID = "NULL"
    IDAgua = "NULL"
    Comentarios = "NULL"
    ComentariosAdicionais = "NULL"
    ConsumoEfetivo = "NULL"
    ConsumoFaturado = "NULL"
    Custo = "NULL"
    CustoReais = "NULL"
    DataInicio = "NULL"
    DataFinal = "NULL"
    Dias = "NULL"
    ICMS = "NULL"
    ICMSTaxa = "NULL"
    ICMSValorFinal = "NULL"
    PIS = "NULL"
    PISTaxa = "NULL"
    PISValorFinal = "NULL"
    COFINS = "NULL"
    COFINSTaxa = "NULL"
    COFINSValorFinal = "NULL"
    PISCOFINS = "NULL"
    PISCOFINSTaxa = "NULL"
    PISCOFINSValorFinal = "NULL"
    LeituraAnterior = "NULL"
    LeituraAtual = "NULL"
    Periodo = "NULL"
    Status = "Recebido"
    StatusChecagem = "NULL"
    Vencimento = "NULL"
    TipoFaturamento = "NULL"
    IDDocumento = "NULL"

    def __init__(self):
        pass

    def __str__(self):
        return f"INSERT INTO cte4docs.DadoAgua ( \
            IDAgua, \
            Comentarios, \
            ComentariosAdicionais, \
            ConsumoEfetivo, \
            ConsumoFaturado, \
            Custo, \
            CustoReais, \
            DataInicio, \
            DataFinal, \
            Dias, \
            ICMS, \
            ICMSTaxa, \
            ICMSValorFinal, \
            PIS, \
            PISTaxa, \
            PISValorFinal, \
            COFINS, \
            COFINSTaxa, \
            COFINSValorFinal, \
            PISCOFINS, \
            PISCOFINSTaxa, \
            PISCOFINSValorFinal, \
            LeituraAnterior, \
            LeituraAtual, \
            Periodo, \
            Status, \
            StatusChecagem, \
            Vencimento, \
            TipoFaturamento, \
            IDDocumento) \
            VALUES \
            (\
                '{self.IDAgua}', \
                '{self.Comentarios}', \
                '{self.ComentariosAdicionais}', \
                {self.ConsumoEfetivo}, \
                {self.ConsumoFaturado}, \
                {self.Custo}, \
                {self.CustoReais}, \
                '{self.DataInicio}', \
                '{self.DataFinal}', \
                {self.Dias}, \
                {self.ICMS}, \
                {self.ICMSTaxa}, \
                {self.ICMSValorFinal}, \
                {self.PIS}, \
                {self.PISTaxa}, \
                {self.PISValorFinal}, \
                {self.COFINS}, \
                {self.COFINSTaxa}, \
                {self.COFINSValorFinal}, \
                {self.PISCOFINS}, \
                {self.PISCOFINSTaxa}, \
                {self.PISCOFINSValorFinal}, \
                {self.LeituraAnterior}, \
                {self.LeituraAtual}, \
                '{self.Periodo}', \
                '{self.Status}', \
                '{self.StatusChecagem}', \
                '{self.Vencimento}', \
                '{self.TipoFaturamento}', \
                '{self.IDDocumento}' \
            );"
