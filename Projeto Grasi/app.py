from Models.EstoqueModels import Produto
from Models.EstoqueControle import ControleEstoque 

def main():
    estoque = ControleEstoque()

    while True:
        print("Menu de Controle de Estoque")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            try:
                produto = Produto(nome, quantidade, preco)
                estoque.adicionar_produto(produto)
                print("Produto adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif escolha == "2":
            produtos = estoque.listar_produtos()
            print("\n=== Produtos no Estoque ===")
            for prod in produtos:
                print(f"ID: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço: R${prod[3]:.2f}")

        elif escolha == "3":
            id = int(input("ID do produto a atualizar: "))
            print("Deixe o campo vazio para não alterar.")
            quantidade = input("Nova quantidade: ")
            preco = input("Novo preço: ")
            try:
                if quantidade:
                    estoque.atualizar_produto(id, quantidade=int(quantidade))
                if preco:
                    estoque.atualizar_produto(id, preco=float(preco))
                print("Produto atualizado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif escolha == "4":
            id = int(input("ID do produto a remover: "))
            estoque.remover_produto(id)
            print("Produto removido com sucesso!")

        elif escolha == "5":
            busca_por = input("Buscar por (1) ID ou (2) Nome? ")
            if busca_por == "1":
                id = int(input("ID do produto: "))
                resultado = estoque.buscar_produto(id=id)
            elif busca_por == "2":
                nome = input("Nome do produto: ")
                resultado = estoque.buscar_produto(nome=nome)
            else:
                print("Opção inválida.")
                continue

            if resultado:
                print("\n=== Resultado da Busca ===")
                for prod in resultado:
                    print(f"ID: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço: R${prod[3]:.2f}")
            else:
                print("Produto não encontrado.")

        elif escolha == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")



if __name__== "__main__":
    main()

