class Recibo:

    def __init__(self, nome):
        self.nome = nome

    def descricao(self, valor):
        self._descricao = valor

    @property
    def valor(self):
        return(self._valor)
        
    @valor.setter
    def valor(self, _valor):
        self._valor = _valor

    def __str__(self):
     
        texto = f'recebemos de {self.nome} a quanto de R$ {self._valor}'
        titulo = 'Recibo'.center(len(texto), '*')
        descricao = f'\nReferente {self._descricao}'
        dados = f' {titulo}\n{texto} {descricao}'
        return(dado)

