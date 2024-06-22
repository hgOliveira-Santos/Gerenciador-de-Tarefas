from gerenciador import * # Importação do módulo gerenciador para o uso das funções que gerenciam a lista de tarefas

def menu():
    print("\n==== Lista de Tarefas ====")
    print("1. Adicionar tarefa")
    print("2. Marcar como concluída")
    print("3. Imprimir lista de tarefas")
    print("0. Sair")

def nome_arquivo():
    nome = input("Digite o nome do arquivo para salvamento: ")
    if not nome.endswith(".txt"):
        nome += ".txt"
    return nome

def main():
    nomeArquivo = nome_arquivo()  # Obtém o nome do arquivo para salvar
    tarefas = carregar_tarefas(nomeArquivo)  # Carrega as tarefas do arquivo
    print(tarefas)  # Exibe as tarefas carregadas (para depuração)

    while True:
        menu()  # Exibe o menu principal
        opção = input("Escolha uma opção: ")

        match opção:
            case "1":
                adicionar_tarefa(tarefas)  # Chama a função para adicionar uma tarefa
                salvar_tarefas(tarefas, nomeArquivo)  # Salva as tarefas atualizadas no arquivo
            case "2":
                imprimir_tarefas(tarefas)  # Exibe todas as tarefas
                marcar_tarefa_concluída(tarefas)  # Marca uma tarefa como concluída
                salvar_tarefas(tarefas, nomeArquivo)  # Salva as tarefas atualizadas no arquivo
            case "3":
                imprimir_tarefas(tarefas)  # Exibe todas as tarefas
            case "0":
                print("\nEncerrando...")  # Mensagem de encerramento
                break  # Sai do loop principal
            case _:
                print("Opção inválida! Tente novamente.")  # Mensagem de opção inválida

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
