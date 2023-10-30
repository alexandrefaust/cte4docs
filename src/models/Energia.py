class Energia:
    ID = ''
    IDEnergia = ''
    IDConjunto = ''
    IDEdificio = ''
    Concessionaria = ''
    Comentario = ''
    DataAtivacao = ''
    DataInativacao = ''
    NumeroEquipamento = ''
    Origem = ''
    PavimentoModulo = ''
    Tipo = ''
    
    def __init__(self,
                 ID, 
                 IDEnergia, 
                 IDConjunto, 
                 IDEdificio, 
                 Concessionaria, 
                 Comentario, 
                 DataAtivacao, 
                 DataInativacao, 
                 NumeroEquipamento, 
                 Origem, 
                 PavimentoModulo, 
                 Tipo):
        self.ID = ID
        self.IDEnergia = IDEnergia
        self.IDConjunto = IDConjunto
        self.IDEdificio = IDEdificio
        self.Concessionaria = Concessionaria
        self.Comentario = Comentario
        self.DataAtivacao = DataAtivacao
        self.DataInativacao = DataInativacao
        self.NumeroEquipamento = NumeroEquipamento
        self.Origem = Origem
        self.PavimentoModulo = PavimentoModulo
        self.Tipo = Tipo

    def __str__(self):
        return f"INSERT INTO cte4docs.Energia ( \
            IDEnergia, \
            IDConjunto, \
            IDEdificio, \
            Concessionaria, \
            Comentario, \
            DataAtivacao, \
            DataInativacao, \
            NumeroEquipamento, \
            Origem, \
            PavimentoModulo, \
            Tipo)  \
            VALUES \
            ("