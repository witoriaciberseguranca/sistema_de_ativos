from json_utils import carregar_dados, salvar_dados


def cadastrar_ativo():

    dados = carregar_dados()

    if len(dados["ativos"]) == 0:

        id_ativo = 1 

    else:
         
        ultimo_id = dados["ativos"][-1]["id"]
        id_ativo = ultimo_id + 1

    print(f"\nID de cadastro: {id_ativo}")

    hostname = input("Hostname: ")
    responsavel = input("Responsável: ")
    setor = input("Setor: ")
    tipo = input("Tipo do ativo: ")

    novo_ativo = {
        "id": id_ativo,
        "hostname": hostname,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo,
        "vulnerabilidades": []
    }

    dados["ativos"].append(novo_ativo)

    salvar_dados(dados)

    print("\nAtivo cadastrado com sucesso.")


def listar_ativos():

    dados = carregar_dados()

    ativos = dados["ativos"]

    if len(ativos) == 0:
        print("\nNenhum ativo cadastrado.")
        return

    print("\n===== ATIVOS CADASTRADOS =====")

    for ativo in ativos:

        print(f"""
ID: {ativo["id"]}
Hostname: {ativo["hostname"]}
Responsável: {ativo["responsavel"]}
Setor: {ativo["setor"]}
Tipo: {ativo["tipo"]}
""")


def atualizar_ativo():

    dados = carregar_dados()

    try:
        id_ativo = int(input("Digite o ID do ativo: "))

    except ValueError:
        print("ID inválido.")
        return

    for ativo in dados["ativos"]:

        if ativo["id"] == id_ativo:

            print("\nDigite os novos dados:")

            ativo["hostname"] = input("Novo hostname: ")
            ativo["responsavel"] = input("Novo responsável: ")
            ativo["setor"] = input("Novo setor: ")
            ativo["tipo"] = input("Novo tipo: ")

            salvar_dados(dados)

            print("\nAtivo atualizado com sucesso.")
            return

    print("\nAtivo não encontrado.")
    
def deletar_ativo():

    dados = carregar_dados()

    try:
        id_ativo = int(input("Digite o ID do ativo que deseja deletar: "))

    except ValueError:
        print("ID inválido.")
        return

    for ativo in dados["ativos"]:

        if ativo["id"] == id_ativo:

            dados["ativos"].remove(ativo)

            salvar_dados(dados)

            print("\nAtivo removido com sucesso.")
            return

        print("\nAtivo não encontrado.")

def cadastrar_vulnerabilidade():

    dados = carregar_dados()
    
    try:
        id_ativo = int(input("Digite o ID do ativo:"))

    except ValueError:
        print("ID inválido.")
        return
    
    for ativo in dados["ativos"]:
         
        if ativo["id"] == id_ativo:
        
            descricao = input("Descreva a vulmerabilidade : ")
            severidade = input("Severidade:")
            status = input("Status:")

            vulmerabilidade = {
                "descricao": descricao,
                "severidade": severidade,
                "status": status

            }

            ativo["vulnerabilidades"].append(vulmerabilidade)

            salvar_dados(dados)

            print("\nVulnerabilidades cadastrada com sucesso.")
            return
        
def visualizar_vulnerabilidade():
        
    dados = carregar_dados()

    try:
        id_ativo = int(input("Digite o ID do ativo: "))

    except ValueError:
        print("ID inválido. ")
        return
    
    for ativo in dados["ativos"]:

        if ativo["id"] == id_ativo:
            
            vulnerabilidades = ativo["vulnerabilidades"]

            if len(vulnerabilidades) == 0:

                print("\n Este ativo não passui vulnerabilidades.")
                return
            
            for vulnerabilidade in vulnerabilidades:

                print(f"""
Descrição: {vulnerabilidade["descricao"]}
Severidade: {vulnerabilidade["severidade"]}
Status: {vulnerabilidade["status"]}
""")
                return

        print("\nAtivo não encontrado.")

