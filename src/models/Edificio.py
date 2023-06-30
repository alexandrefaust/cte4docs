class Edificio:
    ID = ''
    IDCliente = ''
    IDEdificio = ''
    IDEndereco = ''
    AreaConstruida = ''
    AreaLocavel = ''
    CNPJ = ''
    Fundo = ''
    GrossAssetValue = ''
    Nome = ''
    Ownership = ''
    StatusOperacao = ''
    StatusPortfolio = ''
    Tipologia = ''
    TipoOcupacao = ''

    def __init__(self, 
                 ID,
                 IDCliente,
                 IDEdificio,
                 IDEndereco,
                 AreaConstruida,
                 AreaLocavel,
                 CNPJ,
                 Fundo,
                 GrossAssetValue,
                 Nome,
                 Ownership,
                 StatusOperacao,
                 StatusPortfolio,
                 Tipologia,
                 TipoOcupacao):
        self.ID = ID
        self.IDCliente = IDCliente
        self.IDEdificio = IDEdificio
        self.IDEndereco = IDEndereco
        self.AreaConstruida = AreaConstruida
        self.AreaLocavel = AreaLocavel
        self.CNPJ = CNPJ
        self.Fundo = Fundo
        self.GrossAssetValue = GrossAssetValue
        self.Nome = Nome
        self.Ownership = Ownership
        self.StatusOperacao = StatusOperacao
        self.StatusPortfolio = StatusPortfolio
        self.Tipologia = Tipologia
        self.TipoOcupacao = TipoOcupacao

    def __str__(self):
        return f"INSERT INTO cte4docs.Edificio ( \
            IDCliente, \
            IDEdificio, \
            IDEndereco, \
            AreaConstruida, \
            AreaLocavel, \
            CNPJ, \
            Fundo, \
            GrossAssetValue, \
            Nome, \
            Ownership, \
            StatusOperacao, \
            StatusPortfolio, \
            Tipologia, \
            TipoOcupacao \
        ) \
        VALUES (\
            {self.IDCliente}, \
            {self.IDEdificio}, \
            {self.IDEndereco}, \
            {self.AreaConstruida}, \
            {self.AreaLocavel}, \
            {self.CNPJ}, \
            {self.Fundo}, \
            {self.GrossAssetValue}, \
            {self.Nome}, \
            {self.Ownership}, \
            {self.StatusOperacao}, \
            {self.StatusPortfolio}, \
            {self.Tipologia}, \
            {self.TipoOcupacao}, \
        );" 