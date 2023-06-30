class Endereco:
    ID = ''
    Bairro = ''
    CEP = ''
    Cidade = ''
    Estado = ''
    Logradouro = ''

    def __init__(self,
                 ID,
                 Bairro,
                 CEP,
                 Cidade,
                 Estado,
                 Logradouro):
        self.ID = ID
        self.Bairro = Bairro
        self.CEP = CEP
        self.Cidade = Cidade
        self.Estado = Estado
        self.Logradouro = Logradouro

    def __str__(self):
        return f"INSERT INTO cte4docs.Endereco ( \
            Bairro, \
            CEP, \
            Cidade, \
            Estado, \
            Logradouro \
            ) VALUES ( \
                {self.Bairro}, \
                {self.CEP}, \
                {self.Cidade}, \
                {self.Estado}, \
                {self.Logradouro} \
            )"