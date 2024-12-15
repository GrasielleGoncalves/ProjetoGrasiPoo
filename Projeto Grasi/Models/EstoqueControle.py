from Models.Estoque import Produto
from Models.Validar import Validador

import sqlite3

class ControleEstoque:
    def __init__(self, banco_dados="estoque.db"):
        self.conn = sqlite3.connect(banco_dados)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """)
        self.conn.commit()

    def adicionar_produto(self, produto):
        self.cursor.execute("""
            INSERT INTO Produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
        """, (produto.nome, produto.quantidade, produto.preco))
        self.conn.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM Produtos")
        return self.cursor.fetchall()

    def atualizar_produto(self, id, quantidade=None, preco=None):
        if quantidade is not None:
            Validador.validar_valor(quantidade)
            self.cursor.execute("""
                UPDATE Produtos
                SET quantidade = ?
                WHERE id = ?
            """, (quantidade, id))
        if preco is not None:
            Validador.validar_valor(preco)
            self.cursor.execute("""
                UPDATE Produtos
                SET preco = ?
                WHERE id = ?
            """, (preco, id))
        self.conn.commit()

    def remover_produto(self, id):
        self.cursor.execute("""
            DELETE FROM Produtos
            WHERE id = ?
        """, (id,))
        self.conn.commit()

    def buscar_produto(self, id=None, nome=None):
        if id is not None:
            self.cursor.execute("""
                SELECT * FROM Produtos
                WHERE id = ?
            """, (id,))
        elif nome is not None:
            self.cursor.execute("""
                SELECT * FROM Produtos
                WHERE nome LIKE ?
            """, (f"%{nome}%",))
        else:
            return None
        return self.cursor.fetchall()