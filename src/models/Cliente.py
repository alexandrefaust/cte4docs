class Cliente:
    ID = ''
    Nome = ''

    def __init__(self, ID, Nome):
        self.ID = ID
        self.Nome = Nome

    def __str__(self):
        return f"INSERT INTO cte4docs.DadoAgua (Nome) VALUES ({self.Nome})"