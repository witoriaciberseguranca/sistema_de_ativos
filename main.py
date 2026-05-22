from enums import TipoAtivo

from enums import TipoAtivo


while True:

    print("\n===== SISTEMA DE ATIVOS =====")
    print("1 - Cadastrar ativo")
    print("2 - Listar tipos de ativos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCadastro de ativo em desenvolvimento...")

    elif opcao == "2":

        print("\nTIPOS DE ATIVOS:")

        for tipo in TipoAtivo:
            print(tipo.value, "-", tipo.name)

    elif opcao == "3":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")