from src.task import Task

class ToDoList:
    def __init__(self):
        self.tarefas = []

    def add_task(self, nome, descricao):
        if not nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        tarefa = Task(nome, descricao)
        self.tarefas.append(tarefa)
        return tarefa
