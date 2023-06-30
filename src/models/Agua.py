class Agua:
    ID = ''
    IDAgua = ''
    IDConjunto = ''
    IDEdificio = ''
    Concessionaria = ''
    Comentario = ''
    DataAtivacao = ''
    DataInativacao = ''
    NumeroHidrometro = ''
    Origem = ''
    PavimentoModulo = ''
    Tipo = ''
    

    def __init__(self,
                 ID, 
                 IDAgua, 
                 IDConjunto, 
                 IDEdificio, 
                 Concessionaria, 
                 Comentario, 
                 DataAtivacao, 
                 DataInativacao, 
                 NumeroHidrometro, 
                 Origem, 
                 PavimentoModulo, 
                 Tipo):
        self.ID = ID
        self.IDAgua = IDAgua
        self.IDConjunto = IDConjunto
        self.IDEdificio = IDEdificio
        self.Concessionaria = Concessionaria
        self.Comentario = Comentario
        self.DataAtivacao = DataAtivacao
        self.DataInativacao = DataInativacao
        self.NumeroHidrometro = NumeroHidrometro
        self.Origem = Origem
        self.PavimentoModulo = PavimentoModulo
        self.Tipo = Tipo

    def __str__(self):
        return f"INSERT INTO cte4docs.Agua ( \
            IDAgua, \
            IDConjunto, \
            IDEdificio, \
            Concessionaria, \
            Comentario, \
            DataAtivacao, \
            DataInativacao, \
            NumeroHidrometro, \
            Origem, \
            PavimentoModulo, \
            Tipo)  \
            VALUES \
            ("