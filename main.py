from enums import TipoAtivo
from ativos import cadastrar_ativo, listar_ativos, atualizar_ativo, deletar_ativo

while True:

    print("\n===== SISTEMA DE ATIVOS =====")
    print("1 - Cadastrar ativo")
    print("2 - Listar tipos de ativos")
    print("3 - Listar ativos")
    print("4 - Atualizar ativo")
    print("5 - Deletar ativo")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        cadastrar_ativo()

    elif opcao == "2":

        print("\nTIPOS DE ATIVOS:")

        for tipo in TipoAtivo:
            print(tipo.value, "-", tipo.name)

    elif opcao == "3":

        listar_ativos()

    elif opcao == "4":

        atualizar_ativo()

    elif opcao == "5":

        deletar_ativo()
    
    
    elif opcao == "6":

        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")