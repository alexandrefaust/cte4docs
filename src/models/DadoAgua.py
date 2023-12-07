from src.models import Enum

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
    NumeroNF = "NULL"

    def __init__(self):
        pass

    def __str__(self):
        result = f"INSERT INTO cte4docs.DadoAgua ( \
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
            IDDocumento, \
            NumeroNF) \
            VALUES \
            (\
                '{self.IDAgua}', \
                '{self.Comentarios}', \
                '{self.ComentariosAdicionais}', \
                {self.ConsumoEfetivo}, \
                {self.ConsumoFaturado}, \
                {self.Custo}, \
                {self.CustoReais},"
        
        if 'NULL' not in self.DataInicio:
            result += f"'{self.DataInicio}',"
        else:
            result += f"NULL,"

        if 'NULL' not in self.DataFinal:
            result += f"'{self.DataFinal}',"
        else:
            result += f"NULL,"

        result += f"{self.Dias}, \
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
                '{self.IDDocumento}', \
                '{self.NumeroNF}' \
            );"
        
        return result
    
    def toEnergyCap(self):
        bodyLines = []

        
        bodyLines.append({
            "observationTypeId": Enum.ObservationType.INFO_USE.value,
            "valueUnitId": Enum.ValueUnit.VOLUME.value,
            "value": ('Null' in self.ConsumoEfetivo if 0.00 else self.ConsumoEfetivo),
            "costUnitId": None,
            "cost": None,
            "caption": "Volume de Esgoto"
        })

        if not 'NULL' in str(self.ConsumoFaturado):
            bodyLines.append({
                "observationTypeId": Enum.ObservationType.INFO_USE.value,
                "valueUnitId": 93,
                "value": self.ConsumoFaturado,
                "costUnitId": None,
                "cost": None,
                "caption": "Volume de Água"
            })

        if not 'NULL' in str(self.Custo):
            bodyLines.append({
                "observationTypeId": 53,
                "valueUnitId": None,
                "value": None,
                "costUnitId": 112,
                "cost": self.Custo,
                "caption": "Valor Total Fatura"
            })

        bodyLines.append({
            "observationTypeId": Enum.ObservationType.INFO_COST.value,
            "valueUnitId": None,
            "value": None,
            "costUnitId": Enum.CostUnit.BRL.value,
            "cost": self.PISCOFINSValorFinal,
            "caption": "Valor Total Tributos"
        })

        return {
            "Id": self.IDAgua,
            "beginDate": self.DataInicio,
            "endDate": self.DataFinal,
            "billingPeriod": self.Periodo.replace('-', '')[:6],
            "dueDate": self.Vencimento,
            "invoiceNumber": self.NumeroNF,
            "meters": [
            {
                "bodyLines": bodyLines
            }
        ],
        "accountBodyLines":  []
    }
