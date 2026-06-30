# Função que exibe o menu
def menu():
    print("-------------------------")
    print("Cadastro de atletas")
    print("1 - Cadastrar ")
    print("2 - Editar ")
    print("3 - Remover ")
    print("4 - Ver lista")
    print("5 - Fechar sistema")
    print("-------------------------")


# Lista onde serão armazenados os atletas
lista = []


# Função para cadastrar um atleta
def cadastrar():
    # Solicita os dados do atleta
    nome = input("Digite o nome do atleta: ")
    esporte = input("Digite o esporte que pratica: ")

    # Cria um dicionário com os dados
    atleta = {
        "nome": nome,
        "esporte": esporte
    }

    # Adiciona o atleta à lista
    lista.append(atleta)

    print("Atleta cadastrado com sucesso!")


# Função para editar um atleta
def editar():
    # Pergunta qual atleta será editado
    nome = input("Digite o nome do atleta que deseja editar: ")

  # Percorre toda a lista procurando o atleta
    
    for atleta in lista:
        if atleta["nome"] == nome:
            # Atualiza os dados
            atleta["nome"] = input("Novo nome: ")
            atleta["esporte"] = input("Novo esporte: ")

            print("Atleta editado com sucesso!")
            return

    # Caso o atleta não exista
    print("Atleta não encontrado.")


# Função para remover um atleta
def remover():
    # Pergunta qual atleta será removido
    nome = input("Digite o nome do atleta que deseja remover: ")

    # Procura o atleta na lista
    for atleta in lista:
        if atleta["nome"] == nome:
            # Remove o atleta da lista
            lista.remove(atleta)

            print("Atleta removido com sucesso!")
            return

    # Caso não encontre
    print("Atleta não encontrado.")


# Função para mostrar todos os atletas
def listar():
    # Verifica se a lista está vazia
    if len(lista) == 0:
        print("Nenhum atleta cadastrado.")

    else:
        print(" ista de atletas:")

        # Mostra todos os atletas cadastrados
        for i, atleta in enumerate(lista, start=1):
            print(f"{i}. Nome: {atleta['nome']} | Esporte: {atleta['esporte']}")


# Laço principal do programa
while True:

    # Exibe o menu
    menu()

    # Lê a opção escolhida
    opcao = int(input("Digite a opção: "))

    # Chama a função correspondente
    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        editar()

    elif opcao == 3:
        remover()

    elif opcao == 4:
        listar()

    elif opcao == 5:
        print("Sistema encerrado.")
        break  # Encerra o programa

    else:
        print("Opção inválida.")