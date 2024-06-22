from tarefa import Tarefa # Importação do módulo tarefa para o uso da classe Tarefa

def adicionar_tarefa(listaTarefas):
    nome = input("Descreva sua tarefa: ").capitalize()  # Captura o nome da tarefa
    tarefa = Tarefa(nome)  # Cria um objeto Tarefa
    tarefa.definir_prioridade() # Define a prioridade da tarefa
    listaTarefas.append(tarefa)  # Adiciona a tarefa à lista
    print("Tarefa adicionada!")

def imprimir_tarefas(listaTarefas):
    if len(listaTarefas) == 0:
        print("\nNão há tarefas na lista!")
        return
    print("\n==== Tarefas ====\n")
    for tarefa in listaTarefas:
        print(tarefa.__str__())  # Imprime detalhes formatados de cada tarefa

def marcar_tarefa_concluída(listaTarefas):
    while True:
        tarefa_concluída = input("Digite o nome da tarefa concluída (0 para cancelar): ").capitalize().strip()
        if tarefa_concluída == "0":
            print("\nCancelando operação.\n")
            return
        else:
            tarefa_concluída = f"Tarefa: {tarefa_concluída}"
            if tarefa_concluída in listaTarefas:
                for idx, tarefa in enumerate(listaTarefas):
                    if tarefa == tarefa_concluída:
                        listaTarefas.pop(idx)  # Remove a tarefa da lista
                        listaTarefas.pop(idx)  # Remove a tarefa da lista (prioridade)
                        listaTarefas.pop(idx)  # Remove a tarefa da lista (espaço em branco)
                        print("Tarefa concluída!")
                        return
            else:
                print("Tarefa não encontrada!")
                return

def salvar_tarefas(listaTarefas, arquivo):
    with open(arquivo, "a") as f:
        f.truncate(0)  # Limpa o arquivo antes de escrever
        for tarefa in listaTarefas:
            f.write(tarefa.__str__())  # Escreve cada tarefa no arquivo
            f.write("\n")  # Adiciona quebra de linha entre tarefas

def carregar_tarefas(arquivo):
    try:
        with open(arquivo, "r") as f:
            return f.read().splitlines()  # Lê todas as linhas do arquivo como uma lista
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir