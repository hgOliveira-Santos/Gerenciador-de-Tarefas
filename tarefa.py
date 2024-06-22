class Tarefa:
    PRIORIDADES = {
        1: "Baixa",
        2: "Normal",
        3: "Alta"
    }

    def __init__(self, nome, prioridade=None):
        self.nome = nome  # Nome da tarefa
        self.prioridade = prioridade  # Prioridade da tarefa, opcional
    
    def definir_prioridade(self):
        while True:
            try:
                print("\n1. Baixa\n2. Média\n3. Alta\n")
                nível = int(input("Digite o nível de prioridade da tarefa: "))
                if nível not in self.PRIORIDADES:
                    raise ValueError("Opção inválida! Digite um número de 1 a 3.")
                else:
                    self.prioridade = self.PRIORIDADES[nível]
                    return
            except ValueError as e:
                print(e)
                continue
    
    def __str__(self):
        return f"Tarefa: {self.nome.capitalize()}\nPrioridade: {self.prioridade.capitalize()}\n"