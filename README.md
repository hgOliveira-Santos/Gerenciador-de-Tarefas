# Sistema de Gerenciamento de Tarefas em Python

Este projeto consiste em um sistema simples de gerenciamento de tarefas em Python, dividido em três módulos principais: `gerenciador.py`, `main.py` e `tarefa.py`.

## Módulo `gerenciador.py`

O módulo `gerenciador.py` contém funções e a lógica central para manipular uma lista de tarefas, incluindo adicionar tarefas, marcar como concluídas, imprimir a lista e salvar/carregar tarefas de um arquivo.

### Funções disponíveis:

- `adicionar_tarefa(listaTarefas)`: Captura o nome e a prioridade de uma nova tarefa e a adiciona à lista.
- `imprimir_tarefas(listaTarefas)`: Exibe todas as tarefas da lista formatadas.
- `marcar_tarefa_concluída(listaTarefas)`: Permite marcar uma tarefa como concluída, removendo-a da lista.
- `salvar_tarefas(listaTarefas, arquivo)`: Salva a lista de tarefas em um arquivo de texto.
- `carregar_tarefas(arquivo)`: Carrega a lista de tarefas a partir de um arquivo de texto.

## Módulo `main.py`

O módulo `main.py` é responsável pela interação com o usuário e pela execução principal do programa. Ele utiliza as funções definidas no módulo `gerenciador.py` para oferecer um menu interativo ao usuário.

### Funcionalidade principal:

- Exibe um menu para o usuário com opções para adicionar tarefas, marcar como concluídas, imprimir a lista de tarefas e sair do programa.
- Carrega as tarefas de um arquivo existente ou cria um novo arquivo para salvar as tarefas.
- Utiliza as funções do `gerenciador.py` para realizar as operações solicitadas pelo usuário.

## Módulo `tarefa.py`

O módulo `tarefa.py` define a classe `Tarefa`, que representa uma única tarefa dentro do sistema de gerenciamento. Ele também inclui a lógica para definir a prioridade de uma tarefa.
