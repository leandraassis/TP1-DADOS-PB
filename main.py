from datetime import datetime
import os

tarefas = []

def eNumero(numero):
    """Verifica se o valor digitado é um número
        
        parametro:
        numero (int) - numero a ser verificado.

        Retorno:
        boolean
    """
    return numero.isdigit()

def verificarIdTarefa(tarefaLista, id):
    """Verifica se um ID existe na lista de tarefas"""
    for tarefa in tarefaLista:
        if (tarefa['id'] == id):
            return tarefa
    return None

def adicionarTarefa(tarefaLista):
    """Adiciona uma nova tarefa a lista"""
    idDigitado = input("Digite o id da tarefa: ")
    if (eNumero(idDigitado)):
        id = int(idDigitado)
        tarefaPresente = verificarIdTarefa(tarefaLista, id)

        if tarefaPresente:
            print("Uma tarefa com esse id já existe.")
        else:
            nome = input("Nomee a tarefa: ")
            descricao = input("Dê uma descrição para a tarefa: ")
            dataHoje = datetime.now()
            dataCriacao = dataHoje.strftime('%d/%m/%Y')
            status = "A fazer"
            tarefa = {
                "id": id,
                "nome": nome,
                "descricao": descricao,
                "dataCriacao": dataCriacao,
                "status": status
            }
            tarefaLista.append(tarefa)
            os.system('cls')
            print("Tarefa adicionada com sucesso!")
    else: 
        print("ID precisa ser um número.")

def listarTarefas(tarefaLista):
    """Lista todas as tarefas"""
    if (len(tarefaLista) == 0):
        print("Não há tarefas para exibir.")
    else:
        for tarefa in tarefaLista:
            print(f"Tarefa {tarefa['id']}:")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Data de Criação: {tarefa['dataCriacao']}")
            print(f"Status: {tarefa['status']}")
            print("-" * 40)

def tarefasEmAberto(tarefaLista):
    """Filtra as tarefas para pegar as em aberto (status 'A fazer')"""
    tarefasAbertas = []
    for tarefa in tarefaLista:
        if (tarefa['status'] == "A fazer"):
            tarefasAbertas.append(tarefa)
    return tarefasAbertas

def concluirTarefa(tarefaLista, id):
    """Conclui uma tarefa (muda seu status pra 'Concluída')"""
    tarefasAbertas = tarefasEmAberto(tarefaLista)

    print("TAREFAS EM ABERTO:\n")
    listarTarefas(tarefasAbertas)

    tarefaPresente = verificarIdTarefa(tarefasAbertas, id)
    if (tarefaPresente):
        os.system('cls')
        print(f"Tarefa encontrada: {tarefaPresente['nome']}")
        tarefaPresente['status'] = 'Concluída'
        print("Status da tarefa alterado para 'Concluída'.")
    else:
        print("Essa tarefa não existe ou não está em aberto. Verifique o ID.")

def removerTarefa(tarefaLista, id):
    """Remove uma tarefa pela ID"""
    tarefaPresente = verificarIdTarefa(tarefaLista, id)
    if (tarefaPresente):
        tarefaLista.remove(tarefaPresente)
        print("Tarefa excluída com sucesso!")
    else:
        print("Essa tarefa não existe. Verifique o ID.")

def mostrarMenu():
    """Exibe o menu e processa a escolha do usuário"""
    print("BEM VINDO(A) A SEU GERENCIADOR DE TAREFAS!")
    while(True):
        escolhaUser = int(input("\n1 -- Listar tarefas\n2 -- Adicionar tarefa\n3 -- Concluir tarefa\n4 - Remover tarefa\n5 -- SAIR\n"))

        match escolhaUser:
            case 1:
                listarTarefas(tarefas)
            case 2:
                adicionarTarefa(tarefas)
            case 3:
                idDigitado = input("Digite o número da tarefa (ID) que deseja concluir: ")
                if (eNumero(idDigitado)):
                    concluirTarefa(tarefas, int(idDigitado))
                else:
                    print("ID precisa ser um número.")
            case 4:
                idDigitado = input("Digite o número da tarefa (ID) que deseja remover: ")
                if (eNumero(idDigitado)):
                    removerTarefa(tarefas, int(idDigitado))
                else:
                    print("ID precisa ser um número.")
            case 5:
                os.system('cls')
                print("Obrigada por usar o gerenciador de tarefas!")
                break
            case _:
                print("Opção inválida. Opções válidas -- 1, 2, 3, 4 e 5. Digite conforme a ação que deseja realizar.")

mostrarMenu()
