
class Produto(Validador):
    def _init_(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.validar_valor(quantidade)
        self.validar_valor(preco)